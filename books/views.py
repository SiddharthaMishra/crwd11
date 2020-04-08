from django.shortcuts import render
from .models import Book

# Create your views here.


def BookListView(request):
    BookList = Book.objects.all()

    context = {
        'books': BookList
    }
    return render(request, 'books/bookslist.html', context)
