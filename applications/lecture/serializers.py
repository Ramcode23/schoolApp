
from .models import Lecture,Lesson
from ..course.serializers import CourseSerializer
from rest_framework import serializers



class LectureSerializer(serializers.ModelSerializer):
     course=CourseSerializer()
     class Meta:
          model=Lecture
          fields=[
              'description',
              'course'
              ]
          
class LectureUpsertSerializer(serializers.Serializer):
      course = serializers.IntegerField()
      description = serializers.CharField()
    
          
class LessonSerializer(serializers.ModelSerializer):
     lecture=LectureSerializer()
     class Meta:
          model=Lesson
          fields=[
              'title',
              'file',
              'lecture'
          ] 

class LessonUpsertSerializer(serializers.Serializer):
      lecture = serializers.IntegerField()
      title=serializers.CharField()
      file=serializers.FileField()
      
                       