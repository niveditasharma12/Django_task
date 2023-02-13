from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255, default='')
    description=models.TextField(default='')
    price=models.DecimalField(max_digits = 5,
                         decimal_places = 2)

    def __str__(self):
        return self.name







