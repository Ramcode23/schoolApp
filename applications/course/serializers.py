

from .models import Course, Enrollment
from rest_framework import serializers
from ..user.serializers import UserSerializer
from rest_framework import pagination


class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()
    class Meta:
        model = Course
        fields = ['id',
                  'descirption',
                  'teacher',
                  'image'
                  ]

class CourseUpsertSerializer(serializers.Serializer):
    descirption = serializers.CharField()
    image = serializers.ImageField( required=False )
        
class EnrollmentSerializer(serializers.ModelSerializer):
    student = UserSerializer()

    class Meta:
        model = Enrollment
        fields = [
            'course',
            'student'
        ]

class EnrollmentUpsertSerializer(serializers.Serializer):
    course = serializers.IntegerField()

class CustomPagination(pagination.PageNumberPagination):
    PAGE_SIZE = 2
    page_size_query_param = 'page_size'
    max_page_size = 6
  
    
class PaginationSerializer(pagination.PageNumberPagination):
     page_size=2
     page_size_query_param = 'page_size'
     max_page_size=10
     page_query_param = 'p'
        
    
