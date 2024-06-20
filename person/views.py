from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializres import PoetSerializers


class ListPoet(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PoetSerializers