from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    image_url = models.CharField(max_length=2083, default='')

