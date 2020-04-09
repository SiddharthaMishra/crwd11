from django.shortcuts import render
from books.models import Book
from .serializers import BookSerializer
from .variables import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from books.models import Book
from django.utils import timezone
from datetime import datetime as dt
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests

# Create your views here.


class books_list(APIView):
    # queryset = registerCamera.objects.all()
    # serializer_class = CameraSerializer

    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def review_book(request):
    #res = requests.post(settings["verify-url"])

    if True:
        #email = res.json()['email']
        email="abc@xyz"
        print(request.POST)
        book_id = int(request.POST['book_id'])
        
        book = Book.objects.get(id=book_id)
        book_info = book.json
        print(book_info)

        for review in book_info['reviews']:
            if review["email"] == email:
                review["rating"] = request.POST["rating"]
                review["review"] = request.POST["review"]
                break
        else:
            book_info["reviews"].append({
                                "email": email,
                                "rating": request.POST["rating"],
                                "review": request.POST["review"]
                                })
            
        book.json = book_info
        book.save()

        return JsonResponse({"msg":"ok"})

    else:
        return JsonResponse({"error":"Invalid Token"}, status=401)