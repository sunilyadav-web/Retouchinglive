from email import message
from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import IntegerField

class Contact(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField(blank=True)
    email=models.CharField(max_length=50)
    query=models.CharField(max_length=20)
    message=models.CharField(max_length=400)
    datetime = models.DateTimeField(auto_now=True)