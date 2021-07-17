
from rest_framework import routers, urlpatterns
from .views import LessonViewSet,LectureViewSet


router=routers.DefaultRouter()

router.register('lesson',LessonViewSet)
router.register('lecture',LectureViewSet)

urlpatterns=  router.urls