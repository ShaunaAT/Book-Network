from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, DeleteView
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Group, GroupList, Post
from .forms import GroupCreationForm, JoinGroupForm, CreatePostForm



@login_required
def create_group_view(request):
    
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            new_group_name = form.cleaned_data.get('group_name')
            try:
                new_group = Group.objects.get(group_name=new_group_name)
                messages.info(request, f'Group name taken.')
            except:
                password = form.cleaned_data.get('group_password')
                new_group = Group(group_name=new_group_name, 
                                  group_password=password)
                new_group.save()
                new_group.user.add(request.user)
                group_qs = GroupList.objects.filter(user=request.user)
                group_list = group_qs[0]
                group_list.groups.add(new_group)
                messages.success(request, f'Group Created!')
                return redirect('home')
    else:
        form = GroupCreationForm()
    return render(request, 'Groups/create_group.html', {'form':form})


@login_required
def join_group_view(request):
    if request.method == 'POST':
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            groupname = form.cleaned_data.get('group_to_join')
            print(groupname)
            password = form.cleaned_data.get('group_password')
            try:
                group_to_join_qs = Group.objects.filter(group_name=groupname)
                group_to_join = group_to_join_qs[0]
                print(group_to_join.group_name)
                if password == group_to_join.group_password:
                    grouplist_qs = GroupList.objects.filter(user=request.user)
                    group_list = grouplist_qs[0]
                    group_list.groups.add(group_to_join)
                    group_to_join.user.add(request.user)
                    messages.success(request, f'Successfully joined the group!')    
                else:
                    messages.info(request, f'Wrong Password')
            except:
                messages.info(request, f'Group does not exist.')
    else:
        form = JoinGroupForm()
    return render(request, 'Groups/join_group.html', {'form':form})


class group_view(LoginRequiredMixin, DetailView):
    model = Group
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = reversed(Post.objects.filter(group_posted=self.object))
        context['posts'] = posts
        context['group'] = self.object
        return context

@login_required
def group_options_view(request):
    return render(request, 'Groups/group_options.html')


class create_post_group_view(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'Groups/create_post.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm()
        return context
        

class CreatingPost(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'Groups/create_post.html'
    form_class = CreatePostForm
    model = Group

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        self.object = self.get_object()
        content = form.cleaned_data.get('description')
        new_post = Post(description=content, group_posted=self.object, 
                        user=self.request.user)
        new_post.save()
        messages.info(self.request, f'Post Created!')
        return super(CreatingPost, self).form_valid(form)

    def get_success_url(self):
        return reverse('group', kwargs={'pk': self.object.pk})


class CreatePostView(View):

    def get(self, request, *args, **kwargs):
        view = create_post_group_view.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CreatingPost.as_view()
        return view(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False