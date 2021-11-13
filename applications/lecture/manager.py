from _typeshed import Self
from django.db import models
from .models import Lecture
from django.db.models import Count


class LessonManage(models.Manager):

     def lessonByCourse(self, courseId):
            return self.filter(lecture__course__id=courseId).annotate(Count('lecture')).order_by('lecture')
