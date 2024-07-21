from django.db import models

class Category(models.Model):
    name = models.CharField()


class ProductDay(models.Model):
    name = models.CharField(max_length=244)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    img = models.ImageField()
    price = models.FloatField()
