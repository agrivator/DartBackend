from django.contrib.auth.base_user import BaseUserManager
from .models import *

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
 
        return self._create_user(email, password, **extra_fields)
        
class CustomerManager(BaseUserManager):
 
    def create_customer(self, first_name, last_name, email, cart_id, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        customer = Customer(first_name=first_name, last_name=last_name, 
                          email=self.normalize_email(email),
                          cart_id=cart_id)
        customer.set_password(password)
        customer.save()
        return customer
 
 
class ShopKeeperManager(BaseUserManager):
 
    def create_shopkeeper(self, first_name, last_name, email, shop_id, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        shopkeeper = ShopKeeper(first_name=first_name, last_name=last_name, 
                            email=self.normalize_email(email),
                            shop_id=shop_id)
        shopkeeper.set_password(password)
        shopkeeper.save()
        return shopkeeper

class RiderManager(BaseUserManager):
 
    def create_rider(self, first_name, last_name, email, rider_id, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        rider = Rider(first_name=first_name, last_name=last_name, 
                            email=self.normalize_email(email),
                            rider_id=rider_id)
        rider.set_password(password)
        rider.save()
        return rider