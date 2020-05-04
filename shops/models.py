from django.db import models
from django.core.validators import  MaxValueValidator,MinValueValidator
CATEGORIES = [
    ('Fruits and Vegetables', 'Fruits and Vegetables'),
    ('Medicine', 'Medicine'),
    ('Meat and Fish', 'Meat and Fish'),('Electronics','Electronics'),('Stationary','Stationary'),('Grocery','Grocery'),('Pet Foods','Pet Foods')]
# Create your models here.
class Shop(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORIES,max_length=100)
    openstatus=models.BooleanField(default=False)
    address=models.TextField()
    pincode=models.IntegerField(default=691005,validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    image_url = models.CharField(max_length=2048, null=True)
    latitude=models.DecimalField(max_digits=8, decimal_places=6,default=0)
    longitude=models.DecimalField(max_digits=9, decimal_places=6,default=0)
