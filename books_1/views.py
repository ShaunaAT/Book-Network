from django.shortcuts import render
from .models import Book
from .forms import BookForm


def book_create_view(request):
    
    context = {}

    return render(request, "books_1/book_create.html", context)


def book_detail_view(request):
    obj = Book.objects.get(id=1)
    context = {
        "object":obj
    }
    return render(request, "books_1/book_detail.html", context)
