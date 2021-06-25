from django.db.models import fields
from .models import Subject
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
     class Meta:
          model=Subject
          fields=['description','course']