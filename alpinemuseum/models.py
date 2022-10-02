from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class user_detail(models.Model):
    description = models.CharField(max_length=500,null=True,blank=True)
    upload = models.ImageField(upload_to =None, height_field=None,width_field=None, max_length=100,null=True,blank=True)
    surname = models.CharField(max_length=50,null=True,blank=True)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    year_of_birth = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    postcode = models.IntegerField(null=True,blank=True)
    town = models.CharField(max_length=50,null=True,blank=True)
    telephone = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True,max_length=200)

    def __str__(self):
        return self.first_name or "Blank"