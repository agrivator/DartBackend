from rest_framework import serializers
from .models import *
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import authenticate


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)
 
    class Meta:
        model = Customer
        fields = '__all__'
 
    def create(self, validated_data):
        return Customer.objects.create_student(**validated_data)
 
class ShopKeeperRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)
 
    class Meta:
        model = ShopKeeper
        fields = '__all__'
 
    def create(self, validated_data):
        return ShopKeeper.objects.create_employee(**validated_data)

class RiderRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)
 
    class Meta:
        model = Rider
        fields = '__all__'
 
    def create(self, validated_data):
        return Rider.objects.create_employee(**validated_data)



class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
 
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)


        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
 
    
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            userObj = Customer.objects.get(email=user.email)
        except Customer.DoesNotExist:
            userObj = None       
 
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {
            'email': user.email,
            'token': user.token
        }

class ShopKeeperLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
 
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)


        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
 
    
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            userObj = ShopKeeper.objects.get(email=user.email)
        except ShopKeeper.DoesNotExist:
            userObj = None       
 
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {
            'email': user.email,
            'token': user.token
        }

class RiderLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
 
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)


        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
 
    
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            userObj = Rider.objects.get(email=user.email)
        except Rider.DoesNotExist:
            userObj = None       
 
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {
            'email': user.email,
            'token': user.token
        }


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')