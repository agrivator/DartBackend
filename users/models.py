from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


phone_number_regex = RegexValidator(
    regex= "^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$",
    message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
    code="invalid_mobile",
)

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, validators=[phone_number_regex])
    cart_id  = models.IntegerField(null=True) #REWORK: After Cart Model is Built
    








# TODO: Add correct categories.
CATEGORIES = [
    ('Fruits and Vegetables', 'Fruits and Vegetables'),
    ('Medicine', 'Medicine'),
    ('Meat and Fish', 'Meat and Fish'),
]


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    unit = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)
    category = models.CharField(choices=CATEGORIES, max_length=50)
    image_url = models.CharField(max_length=2048, null=True)

    def __str__(self):
        return self.name
