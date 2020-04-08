from django.urls import path
from .views import (
    BookListView,
)
from . import views

urlpatterns = [
    path('book/booklist/',BookListView, name='books-home'),
]
