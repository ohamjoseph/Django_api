from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
# Create your views here.

class DepartementsViewSet(viewsets.ModelViewSet):

    queryset=Departements.objects.all()
    serializer_class=DepartementsSerializer

class ProvincesViewSet(viewsets.ModelViewSet):

    queryset=Provinces.objects.all()
    serializer_class = ProviencesSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset=Region.objects.all()
    serializer_class=RegionSerializer
