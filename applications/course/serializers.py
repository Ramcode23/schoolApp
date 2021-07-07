
from .models import Course, Enrollment
from rest_framework import serializers



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=[
            'descirption',
            'teacher',
            'image'
            ]

class EnrollmentSerializer(serializers.ModelSerializer):
     class Meta:
          model=Enrollment
          fields=[
              'course',
              'student'
                  ]    