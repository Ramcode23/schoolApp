from .serializers import EvaluationSerializer
from django.shortcuts import render
from .models import Evaluation
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from ..user.permission  import IsAdminUser, IsAdminStudent
# Create your views here.
class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = [IsAuthenticated,IsAdminStudent]
    authentication_classes=[TokenAuthentication]


