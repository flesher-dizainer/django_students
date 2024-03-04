from django.db import models

TYPE_PRODUCT_CHOICES = [
    ("ENDURO", "enduro"),
    ("PITBIKE", "pitbike"),
]
class Product(models.Model):
    brand_name = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    date_release = models.DateTimeField()
    type_products = models.CharField(max_length=200, choices=TYPE_PRODUCT_CHOICES)
