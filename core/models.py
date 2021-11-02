from django.db import models

from django.contrib.auth.models import UserManager

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField('Zip Code', max_length=50)
    phone = models.CharField('Contact Phone', max_length=50)
    web = models.URLField('Website Address', max_length=50)
    email_address = models.EmailField('Email address')

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('User Email')