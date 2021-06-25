from django.db import models

# Create your models here.
class Course(models.Model):
    descirption=models.CharField( max_length=50)
    adress=models.CharField( max_length=50)
    

    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.name

