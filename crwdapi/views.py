from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from books.models import Book
from django.utils import timezone
from datetime import datetime as dt
from datetime import date

# Create your views here.


class books_list(APIView):
    # queryset = registerCamera.objects.all()
    # serializer_class = CameraSerializer

    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
