from django.urls import path, include, re_path
from . import views
from .views import books_list
from rest_framework import routers


urlpatterns = [
    path("rest/book/", views.books_list.as_view(), name="books_api"),
]
