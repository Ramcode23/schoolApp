
from django.db import models
from ..course.models import Course

# Create your models here.
class Subject(models.Model):
    description=models.CharField( max_length=50)
    course= models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name =("Subject")
        verbose_name_plural = ("Subjects")

    def __str__(self):
        return self.name

 
