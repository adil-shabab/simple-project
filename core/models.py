from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_cost_price = models.IntegerField()
    product_selling_price = models.IntegerField()
    product_image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
