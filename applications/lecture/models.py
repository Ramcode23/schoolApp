from django.db import models
from ..course.models import Course
# Create your models here.


class Lecture(models.Model):

    description = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Lecture")
        verbose_name_plural = ("Lectures")

    def __str__(self):
        return self.description


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='course/files', max_length=100,blank=True)
    text = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Lesson")
        verbose_name_plural = ("Lessons")

    def __str__(self):
        return self.name
