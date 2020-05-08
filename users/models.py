from django.db import models

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

class Cart(models.Model):
    Userid = models.ForeignKey(User,on_delete=models.CASCADE)#key needs to be created in user
    Pid = models.ForeignKey(Product,on_delete=models.CASCADE)#key needs to be created in product
    Quantity = models.FloatField()
    Total = models.FloatField()
    