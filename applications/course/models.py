from django.db import models
from ..user.models import User  
# Create your models here.
class Course(models.Model):
    descirption=models.CharField( max_length=50)
    teacher=models.ForeignKey(User, on_delete=models.CASCADE)
    image =models.ImageField( upload_to='images/courses', height_field=None, width_field=None, max_length=None)
   
    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.descirption


class Enrollment(models.Model):
    courses=models.ForeignKey(Course, on_delete=models.CASCADE)
    students=models.ForeignKey(User, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Enrollment")
        verbose_name_plural = ("Enrollments")

