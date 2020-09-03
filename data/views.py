from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User_data, Period
# Create your views here.

class User_dataListView(generics.ListAPIView):
    queryset = User_data.objects.all()
    serializer_class = ListSerializer

class PeriodListView(generics.ListAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer