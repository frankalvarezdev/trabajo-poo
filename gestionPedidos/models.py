from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
    category = models.CharField(max_length=150)
    status = models.IntegerField(default=100)
    date = models.BigIntegerField(default=0)
    quantity = models.IntegerField(default=0)
    updated = models.BooleanField(default=False)
    update_date = models.BigIntegerField(default=0)
    sales = models.BigIntegerField(default=0)
    earnings = models.FloatField(default=0)