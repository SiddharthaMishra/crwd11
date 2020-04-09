from django.db import models
from django.utils import timezone
# from django_mysql.models import JSONField, Model
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.

import jsonfield

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='bookpics', blank='True')
    pub_date = models.DateTimeField(default=timezone.now)
    json = jsonfield.JSONField(default={"tags":{}, "reviews":[]})

    def __str__(self):
        return self.title
