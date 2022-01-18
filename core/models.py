from django.db import models
class Customer(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)

