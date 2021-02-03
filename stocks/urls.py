from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('stocks/',StockCreateView.as_view(), name='stock-view'),
    path('total/', StockTotalValueView.as_view(), name='stock-total'),
]
