
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Course, Enrollment
from ..user.models import User
from .serializers import( CourseSerializer, 
                         CourseUpsertSerializer, CustomPagination, 
                         EnrollmentSerializer,
                         EnrollmentUpsertSerializer, 
                         PaginationSerializer)
from ..user.permission import IsAdminStudent, IsAdminTeacher
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000



class CouseViewSet(viewsets.ModelViewSet):
   
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        queryset = Course.objects.filter(teacher=self.request.user)
        serializer = CourseSerializer(queryset, many=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CourseUpsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

     
        course = Course.objects.create(
        descirption=serializer.validated_data['descirption'],
        teacher=self.request.user)
        if serializer.validated_data.get('image'):       
         course.image=serializer.validated_data['image'] 
        course.save()
        return Response(serializer.data) 
    

    def update(self, request, pk=None):
        serializer = CourseUpsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    

        course = Course.objects.get(pk=pk)
        course.descirption=serializer.validated_data['descirption']
        if serializer.validated_data.get('image'):       
          course.image=serializer.validated_data['image'] 
        course.teacher=self.request.user
        course.save() 
        return Response(serializer.data) 

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminTeacher]
        elif self.action == 'list':
             permission_classes = [IsAdminTeacher]
        elif self.action == 'retrieve':
            permission_classes = [IsAdminTeacher]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
  
class CourseListAPIView(ListAPIView):
      queryset = Course.objects.all()
      serializer_class = CourseSerializer
      pagination_class=StandardResultsSetPagination
      authentication_classes = [JSONWebTokenAuthentication]

 
class CourseRetrieveAPIView(RetrieveAPIView):
     queryset = Course.objects.all()
     serializer_class = CourseSerializer
     authentication_classes = [JSONWebTokenAuthentication]
    
 
 
      
      
 
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    authentication_classes = [JSONWebTokenAuthentication]
    pagination_class = StandardResultsSetPagination
    
    
    def list(self, request):
         
         queryset =Enrollment.objects.filter(student__id=self.request.user.id)
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
 
 

 
 