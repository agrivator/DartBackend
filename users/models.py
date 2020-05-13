from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings

from .managers import UserManager,CustomerManager,RiderManager,ShopKeeperManager


phone_number_regex = RegexValidator(
    regex= "^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$",
    message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
    code="invalid_mobile",
)



class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True, unique=True)
    phone = models.CharField(validators=[phone_number_regex],max_length=14)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone']
    
    objects = UserManager()
 
    @property
    def token(self):
        dt = datetime.now() + timedelta(days=days)
        token = jwt.encode({
            'id': user_id,
            'exp': int(time.mktime(dt.timetuple()))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')
 
    def get_full_name(self):
        return (self.first_name+' '+self.last_name)
 
    def get_short_name(self):
        return self.first_name
 
    def natural_key(self):
        return (self.first_name, self.last_name)
 
    def __str__(self):
        return self.email


class Customer(User, PermissionsMixin):
    cart_id = models.CharField(max_length=50,db_index=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','phone']
 
    objects = CustomerManager()
 
    def __str__(self):
        return self.first_name


class ShopKeeper(User, PermissionsMixin):
    shop_id = models.CharField(max_length=50,db_index=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','phone']
 
    objects = ShopKeeperManager()
 
    def __str__(self):
        return self.first_name


class Rider(User, PermissionsMixin):
    shop_id = models.CharField(max_length=50,db_index=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','phone']
 
    objects = RiderManager()
 
    def __str__(self):
        return self.first_name




    









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
