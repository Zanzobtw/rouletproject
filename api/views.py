from django.shortcuts import render
from rest_framework import generics
from .models import Check_List
from .serializers import Check_List_Serializer

class CheckList_List_create(generics.ListCreateAPIView):
    queryset = Check_List.objects.all()
    serializer_class = Check_List_Serializer
