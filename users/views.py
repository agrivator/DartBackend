from django.shortcuts import render
from django_filters import rest_framework as filters

from rest_auth.registration.views import RegisterView


from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class CustomRegisterView(RegisterView):
        queryset = User.objects.all()
        serializer_class = CustomRegisterSerializer


class ProductFilter(filters.FilterSet):

    category = filters.CharFilter(lookup_expr='icontains')
    name = filters.CharFilter(lookup_expr='icontains')
class ProductViewset(viewsets.ModelViewSet):  
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def perform_create(self, serializer):
        serializer.save()

    '''def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        product = Product.objects.filter(category=params['pk'])
        serializer = ProductSerializer(product, many=True)
        return Response(serailizer.data)
    '''