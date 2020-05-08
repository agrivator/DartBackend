from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewset)

router.register(r'Address',views.AddressViewSet)

router.register(r'Coupon',views.CouponViewset)

router.register(r'Order',views.OrderViewset)

router.register(r'Transaction',views.TransactionViewSet)

urlpatterns = router.urls
