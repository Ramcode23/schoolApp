from ..course.models import Course
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404

from ..user.permission import IsAdminStudent,IsAdminTeacher,IsAdminUser
from .serializers import LectureSerializer, LectureUpsertSerializer, LessonSerializer, LessonUpsertSerializer
from .models import Lecture, Lesson
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    authentication_classes=[TokenAuthentication]
    
    
    def list(self, request):
         print(request.headers['courseId'])
         queryset =Lecture.objects.filter(course__id=request.headers['courseId'])
         serializer = LectureSerializer(queryset, many=True)
         return Response(serializer.data)
          

    def create(self, request):
        serializer = LectureUpsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        lecture = Lecture.objects.create(
        course=Course.objects.get(pk=serializer.validated_data['course']),
        description= serializer.validated_data['description'] )
        lecture.save()
        return Response(serializer.data) 

  

    def retrieve(self, request, pk=None):
        print(pk,'*********')
        queryset =  queryset =Lecture.objects.all()
        lecture =get_object_or_404(queryset, pk=pk)
        serializer = LectureSerializer(lecture)
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
            permission_classes = [IsAdminTeacher]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminTeacher]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    authentication_classes=[TokenAuthentication]
    
    def list(self, request):
         queryset =Lesson.objects.filter(lecture__id=request.data['lecture'])
         serializer = LessonSerializer(queryset, many=True)
         return Response(serializer.data)
          

    def create(self, request):
        serializer = LessonUpsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        lesson = Lesson.objects.create(
            
        lecture=Lecture.objects.get(pk=serializer.validated_data['lecture']),
        title= serializer.validated_data['title'] ,
        file= serializer.validated_data['file'] 
        
        )
        lesson.save()
        return Response(serializer.data) 

  

    def retrieve(self, request, pk=None):
        print(pk,'*********')
        queryset =  queryset =Lesson.objects.all()
        lesson =get_object_or_404(queryset, pk=pk)
        serializer = LectureSerializer(lesson)
        return Response(serializer.data)
    
    
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminTeacher]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminTeacher]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
  
  


