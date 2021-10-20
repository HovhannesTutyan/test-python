from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0, null=True, blank=True)
    # pages=models.IntegerField(default=0, null=True, blank=True)

from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    # pages = serializers.IntegerField()
    id = serializers.IntegerField()
