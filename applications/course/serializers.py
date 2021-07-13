
from .models import Course, Enrollment
from rest_framework import serializers
from ..user.serializers import UserSerializer


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
    image = serializers.ImageField()
        


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

