from ..course.models import Course
from django.db.models import Count
from rest_framework.generics import  get_object_or_404

from ..user.permission import IsAdminStudent,IsAdminTeacher,IsAdminUser
from .serializers import( LectureSerializer,
                         LectureInsertSerializer,
                         LectureUpdatetSerializer, LessonInsertSerializer, LessonListSerializer, 
                         LessonSerializer, LessonUpdateSerializer, 
                        )
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
         obj=Lecture.objects.filter(course__id=request.headers['courseid'])
         queryset =Lecture.objects.filter(course__id=request.headers['courseid'])
         serializer = LectureSerializer(queryset, many=True)
         return Response(serializer.data)
          

    def create(self, request):
        serializer = LectureInsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        lecture = Lecture.objects.create(
        course=Course.objects.get(pk=serializer.validated_data['course']),
        description= serializer.validated_data['description'] )
        lecture.save()
        return Response(serializer.data) 

  

    def retrieve(self, request, pk=None):
        queryset =  queryset =Lecture.objects.all()
        lecture =get_object_or_404(queryset, pk=pk)
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)
        

    def update(self, request, pk=None):
         serializer = LectureUpdatetSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         lecture = Lecture.objects.get(pk=pk)
         lecture.description=serializer.validated_data['description']
         lecture.save() 
         return Response(serializer.data) 

 
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
         """ Lesson  order by Lecture """
         queryset =Lesson.objects.filter(lecture__course__id=request.headers['courseId']).annotate(Count('lecture')).order_by('lecture')
         serializer = LessonListSerializer(queryset, many=True)
         return Response(serializer.data)
          

    def create(self, request):
        serializer = LessonInsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        lesson = Lesson.objects.create(
            
        lecture=Lecture.objects.get(pk=serializer.validated_data['lecture']),
        title= serializer.validated_data['title'] ,
        file= serializer.validated_data['file'] ,
        text=serializer.validated_data['text']
        )
        lesson.save()
        return Response(serializer.data) 

    def update(self, request, pk=None):
         serializer = LessonUpdateSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         lesson = Lesson.objects.get(pk=pk)
         lesson.title=serializer.validated_data['title']
         lesson.file=serializer.validated_data['file']
         lesson.text=serializer.validated_data['text']
         lesson.save() 
         return Response(serializer.data) 

    def retrieve(self, request, pk=None):
        queryset =  queryset =Lesson.objects.all()
        lesson =get_object_or_404(queryset, pk=pk)
        serializer = LessonSerializer(lesson)
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
  
  


