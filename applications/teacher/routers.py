
from rest_framework import routers, urlpatterns
from .views import TeacherViewSet
router=routers.DefaultRouter()
router.register('teacher',TeacherViewSet)
urlpatterns=  router.urls