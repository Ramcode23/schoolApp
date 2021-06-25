from ..course.models import Course
from django.db import models

# Create your models here.
class Teacher(models.Model):
    
    name=models.CharField( max_length=50)
    email =models.EmailField( max_length=254)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Teacher")
        verbose_name_plural = ("Teachers")

    def __str__(self):
        return self.name

  