from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


from .managers import UserManager


phone_number_regex = RegexValidator(
    regex= "^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$",
    message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
    code="invalid_mobile",
)

USER_CHOICES = [
    ("customer","customer"),
    ("shopkeeper","shopkeeper"),
    ("rider","rider")
]


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    phone = models.CharField(max_length=14, validators=[phone_number_regex])
    user_type = models.CharField(choices=USER_CHOICES,max_length=50)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','user_type','phone']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
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

class Cart(models.Model):
    Userid = models.ForeignKey(User,on_delete=models.CASCADE)#key needs to be created in user
    Pid = models.ForeignKey(Product,on_delete=models.CASCADE)#key needs to be created in product
    Quantity = models.FloatField()
    Total = models.FloatField()
    