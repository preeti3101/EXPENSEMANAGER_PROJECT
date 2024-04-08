from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    is_manager = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'user'