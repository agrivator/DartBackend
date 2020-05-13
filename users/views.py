from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_auth.registration.views import RegisterView, APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from .renderers import UserJSONRenderer
# Create your views here.

class CustomerRegistration(APIView):

    @classmethod
    def get_extra_actions(cls):
        return []


    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = CustomerRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 
class ShopKeeperRegistration(APIView):

    @classmethod
    def get_extra_actions(cls):
        return []

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = ShopKeeperRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RiderRegistration(APIView):

    @classmethod
    def get_extra_actions(cls):
        return []

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RiderRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 
class CustomerLogin(APIView):


    @classmethod
    def get_extra_actions(cls):
        return []

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = CustomerLoginSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ShopKeeperLogin(APIView):

    @classmethod
    def get_extra_actions(cls):
        return []

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = ShopKeeperLoginSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RiderLogin(APIView):

    @classmethod
    def get_extra_actions(cls):
        return []

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RiderLoginSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




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