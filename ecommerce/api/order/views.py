from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

# Create your views here.
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer