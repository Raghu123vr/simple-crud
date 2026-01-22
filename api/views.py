from django.shortcuts import render
from .models import Restapi
from .serializers import Restserializer
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.
class Employee(viewsets.ModelViewSet):
    queryset = Restapi.objects.all()
    serializer_class = Restserializer
    pagination_class=LimitOffsetPagination