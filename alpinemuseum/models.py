from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class user_detail(models.Model):
    description = models.CharField(max_length=500)
    upload = models.ImageField(upload_to =None, height_field=None,width_field=None, max_length=100)
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    year_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=100)
    postcode = models.IntegerField()
    town = models.CharField(max_length=50)
    telephone = models.IntegerField()
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.first_name