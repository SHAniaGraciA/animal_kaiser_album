from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.CharField(max_length=255)
    #role =models.CharField(max_length=255,default="Stealth Assassin")
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    amount = models.IntegerField()
    
class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    hobby = models.TextField()
    department = models.charField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)



    