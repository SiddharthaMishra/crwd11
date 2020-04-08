from django.db import models
from django.utils import timezone
# from django_mysql.models import JSONField, Model
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.


class Book(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=100, primary_key=True)
    link = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='bookpics', blank='True')
    pub_date = models.DateTimeField(default=timezone.now)
   # json = JSONField()

    def __str__(self):
        return self.title
