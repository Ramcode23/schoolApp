from .serializers import SchoolSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Shool
from rest_framework import viewsets

# Create your views here.
class ShoolViewSet(viewsets.ModelViewSet):
    queryset = Shool.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[TokenAuthentication]



