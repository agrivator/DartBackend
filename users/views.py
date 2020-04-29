from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):  
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)