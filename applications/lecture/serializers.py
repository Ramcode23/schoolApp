
from .models import Lecture,Lesson
from ..course.serializers import CourseSerializer
from rest_framework import serializers

class LessonSerializer(serializers.ModelSerializer):
       
     class Meta:
          model=Lesson
          fields=[
               'id',
              'title',
              'file',
              'text',
              'lecture'
          ] 
          

class LectureSerializer(serializers.ModelSerializer):
     course=CourseSerializer()
     lessons_lecture=LessonSerializer(many=True)
     class Meta:
          model=Lecture
          fields=[
               'id',
              'description',
              'course',
              'lessons_lecture',
              ]
          
class LectureListSerializer(serializers.ModelSerializer):
    
     class Meta:
          model=Lecture
          fields=[
               'id',
              'description',
              ]
                    
          
class LectureInsertSerializer(serializers.Serializer):
      course = serializers.IntegerField()
      description = serializers.CharField()
    
class LectureUpdatetSerializer(serializers.Serializer):
      description = serializers.CharField()
    
          

          
class LessonListSerializer(serializers.ModelSerializer):
     lecture=LectureListSerializer()
     class Meta:
          model=Lesson
          fields=[
                'id',
              'title',
              'text',
              'lecture'
          ] 
          
          

class LessonInsertSerializer(serializers.Serializer):
      lecture = serializers.IntegerField()
      title=serializers.CharField()
      text=serializers.CharField()
      file=serializers.FileField()
      
  
class LessonUpdateSerializer(serializers.Serializer):
      lecture = serializers.IntegerField()
      title=serializers.CharField()
      text=serializers.CharField()
      file=serializers.FileField()
      
                                            