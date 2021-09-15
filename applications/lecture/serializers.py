
from .models import Lecture,Lesson
from ..course.serializers import CourseSerializer
from rest_framework import serializers



class LectureSerializer(serializers.ModelSerializer):
     course=CourseSerializer()
     class Meta:
          model=Lecture
          fields=[
               'id',
              'description',
              'course'
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
    
          
class LessonSerializer(serializers.ModelSerializer):
     lecture=LectureSerializer()
     class Meta:
          model=Lesson
          fields=[
              'title',
              'file',
              'text',
              'lecture'
          ] 
          
          
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
          
          

class LessonUpsertSerializer(serializers.Serializer):
      lecture = serializers.IntegerField()
      title=serializers.CharField()
      text=serializers.CharField()
      file=serializers.FileField()
      
                       