from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Tutorial
from .serializer import TutorialSerializer
from .pagination import (
  CustomPageNumberPagination,
  CustomLimitOffsetPagination,
  CustomCursorPagination
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

class TutorialMVS(ModelViewSet):
  queryset = Tutorial.objects.all()
  serializer_class = TutorialSerializer
  
  #? pagination
  # pagination_class = CustomPageNumberPagination
  # pagination_class = CustomLimitOffsetPagination
  # pagination_class = CustomCursorPagination
  
  #? filter
  filter_backends =[DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_fields = ["id", "title"]
  
  #? search
  search_fields = ["title"]
  # search_fields=['^title']  #* baş harfine göre arama yapmak için,
  # ordering_fields = ['id']  #* filter boxta hangi seçenekler çıksın istiyorsanız onu yazıyorsunuz
  # ordering = ['-title']  #* default olarak ilk açıldığında buraya yazdığımıza göre sıralıyor