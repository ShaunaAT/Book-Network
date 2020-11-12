import requests
import xmltodict

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django import forms
from django.shortcuts import get_object_or_404

from .forms import UserRegisterForm, ProfileUpdateForm
from book_project.settings import GOODREADS_API_KEY
from books_1.models import Book
import books_1
from .models import Library, LibraryBook

# Create your views here.

def register(request):
    #user registration view
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.info(request, f'Profile Updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'p_form':p_form}
    return render(request, 'users/profile.html', context)


 
@login_required
def library_view(request):
    # User library view
    my_library_items = []
    for item in LibraryBook.objects.all().filter(user=request.user):
        my_library_items.append(item)
    my_library = reversed(my_library_items)
    context = {
        'library':my_library
    }
    return render(request, 'users/library.html', context)


def search_view(request):

    books = []

    if request.method == 'POST':
        base_url = 'https://www.goodreads.com/search'

        params = {
            'q':request.POST.get('search', 'none'),
           'key':GOODREADS_API_KEY,
        }

        try:
           r = requests.get(base_url, params=params)
           f = xmltodict.parse(r.content)

           for n in range(10): 
                try:
                    temp_book = Book.objects.get(book_id = f["GoodreadsResponse"]["search"]['results']['work'][n]['best_book']['id']['#text'])
                except:
                    temp_book = Book(title=f["GoodreadsResponse"]["search"]['results']['work'][n]['best_book']['title'], 
                                     author=f["GoodreadsResponse"]["search"]['results']['work'][n]['best_book']['author']['name'],
                                     image_url=f["GoodreadsResponse"]["search"]['results']['work'][n]['best_book']['image_url'], 
                                     book_id=f["GoodreadsResponse"]["search"]['results']['work'][n]['best_book']['id']['#text'])
                    temp_book.save()
                books.append(temp_book)
            
        except:
            messages.info(request, f'Here is what we found for that search')

        if len(books) == 0:
            messages.info(request, f'No results found')

    context = {
        "books": books,
    }

    return render(request, 'users/search.html', context)


class BookDisplayView(DetailView):
    
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Book_add_Form()
        return context

class Book_add_Form(forms.Form):
    note = forms.CharField()

class AddBook(SingleObjectMixin, FormView):
    template_name = 'books_1/book_detail.html'
    form_class = Book_add_Form
    model = Book

    def post(self, request, *args, **kwargs):
        form_class = Book_add_Form
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        book = self.get_object()
        library_item, created = LibraryBook.objects.get_or_create(book=book, 
                                                                  user=request.user, 
                                                                  in_library=False)
        library_qs = Library.objects.filter(user=request.user)
        library = library_qs[0]
        if library.library_book.filter(book_id = book.book_id).exists():
            messages.info(request, f'Book already in Library')
        else:
            library.library_book.add(library_item)
            messages.success(request, f'Book added to Library')
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        self.object = self.get_object()
        return reverse('book-detail', kwargs={'pk': self.object.pk})

class BookDetailView(View):

    def get(self, request, *args, **kwargs):
        view = BookDisplayView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = AddBook.as_view()
        return view(request, *args, **kwargs)