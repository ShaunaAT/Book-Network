from django.http import HttpResponse
from django.shortcuts import render
from Groups.models import Group

# Create your views here.

def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:    
        context = {'groups' : Group.objects.all().filter(user=request.user)}
        return render(request, "home.html", context)
    else:
        return render(request, "home.html")


def about_view(request):
    return render(request, "about.html")
