from rest_framework import serializers
from .models import Shool


class SchoolSerializer(serializers.ModelSerializer):
     class Meta:
          model=Shool
          fields=[
              'name',
              'country',
              'city',
              'address',
              'address',
              'logo',
              
          ]