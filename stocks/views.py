from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.db.models import Sum
# Create your views here.

class StockCreateView(generics.CreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)


class StockTotalValueView(generics.GenericAPIView):

    queryset = Stocks.objects.all()

    def get(self, request):
        user = self.request.user
        query = Stocks.objects.filter(user=user)
        serializer = StocksTotalSerializer(query, many=True)
        get_sum = query.aggregate(total=Sum(F('price')*F('quantity')))
        return Response({'sum':get_sum,'data':serializer.data})