from rest_framework import serializers
from books.models import Book
from rest_framework.response import Response

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'link', 'author', 'picture', 'pub_date', "json")
