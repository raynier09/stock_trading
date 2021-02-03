from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from .serializers import *
from .models import *
# Create your views here.

class StockCreateView(generics.CreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer