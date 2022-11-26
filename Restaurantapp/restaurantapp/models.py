from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class newregister(models.Model):
    firstname=models.CharField(max_length=130)
    lastname=models.CharField(max_length=130)
    email=models.CharField(max_length=130)
    password1=models.CharField(max_length=130)
    password2=models.CharField(max_length=130)
    date=models.DateField()
    
class newregister1(models.Model):
    firstname=models.CharField(max_length=130)
    lastname=models.CharField(max_length=130)
    email=models.CharField(max_length=130)
    password1=models.CharField(max_length=130)
    password2=models.CharField(max_length=130)
    date=models.DateField()
    
class newregister2(models.Model):
    
    username=models.CharField(max_length=130,default=False)
    firstname=models.CharField(max_length=130)
    lastname=models.CharField(max_length=130)
    email=models.CharField(max_length=130)
    password=models.CharField(max_length=130)
    date=models.DateField()


class feedback(models.Model):
    fullname=models.CharField(max_length=130)
    email=models.CharField(max_length=130)
    textarea=models.TextField()
    date=models.DateField()

    def __str__(self):
       return  self.fullname