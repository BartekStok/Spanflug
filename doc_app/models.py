from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Document(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    path = models.FileField(upload_to='documents/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Attributes(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
