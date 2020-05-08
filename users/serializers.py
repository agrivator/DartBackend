from rest_framework import serializers
from .models import *

from rest_auth.registration.serializers import RegisterSerializer

phone_number_regex = RegexValidator(
    regex= "^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$",
    message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
    code="invalid_mobile",
)

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    phone = serializers.CharField(max_length=14, validators=[phone_number_regex])
    first_name = serializers.CharField(max_length=30, label='First Name')
    last_name = serializers.CharField(max_length=30, label='Last Name')
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    user_type = serializers.ChoiceField(choices=USER_CHOICES)


    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.password = self.validated_data.get('passoword', '')
        user.phone= self.validated_data.get('phone', '')
        user.user_type = self.validated_data.get('user_type', '')
        user.save(update_fields=['first_name','last_name','user_type', 'phone'])

class CustomUserDetailsSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('first_name','last_name','phone','user_type')



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=['locality','city','district','state','pincode','latitude','longitude']

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coupon
        fields=['discount','expiry_date','max']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['coupon','time_stamp_order']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=['order','amount','time_stamp_transaction']





class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')
