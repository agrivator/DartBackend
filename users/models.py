from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    unit = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    image_url = models.CharField(max_length=2048, null=True)
    in_stock = models.BooleanField(null=True)

    def __str__(self):
        return self.name
