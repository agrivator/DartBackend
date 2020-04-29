from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):

    farmer = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    
    class Meta:
        model   =  Product
        fields  =  ('__all__')
