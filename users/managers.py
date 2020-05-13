from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):
    use_in_migrations = True
    def get_by_natural_key(self, email):
        return self.get(email=email)
 
 
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