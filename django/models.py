from django.db import models


class Product(models.model):
    type = models.CharField(max_length=60)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, defualt="", blank=True)
    price = models.DecimalField(defualt=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default='', blank=True)
