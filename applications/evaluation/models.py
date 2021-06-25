
from django.db import models
from ..subject.models import Subject
from ..student.models import Student

# Create your models here.
class Evaluation(models.Model):
    estudent=models.ForeignKey(Student,  on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,  on_delete=models.CASCADE)
    score=models.FloatField()
    

    class Meta:
        verbose_name = ("Evaluation")
        verbose_name_plural = ("Evaluations")

    def __str__(self):
        return self.name


