
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Course, Enrollment
from ..user.models import User
from .serializers import CourseSerializer, EnrollmentSerializer, EnrollmentUpsertSerializer
from ..user.permission import IsAdminStudent, IsAdminTeacher


class CouseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminTeacher]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    authentication_classes = [TokenAuthentication]
    
    def list(self, request):
         queryset =Enrollment.objects.all()
         serializer = EnrollmentSerializer(queryset, many=True)
         return Response(serializer.data)
          

    def create(self, request):
        serializer = EnrollmentUpsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        enrolment = Enrollment.objects.create(
        course=Course.objects.get(pk=serializer.validated_data['course']),
        student=self.request.user)
        enrolment.save()
        return Response(serializer.data) 

  

    def retrieve(self, request, pk=None):
        queryset =  queryset =Enrollment.objects.all()
        enrolment =get_object_or_404(queryset, pk=pk)
        serializer = EnrollmentSerializer(enrolment)
        return Response(serializer.data)
        

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
 


    
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminStudent]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAdminStudent]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
 