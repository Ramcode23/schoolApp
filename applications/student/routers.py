from rest_framework import routers, urlpatterns
from .views import StudentViewSet
router=routers.DefaultRouter()
router.register('student',StudentViewSet)
urlpatterns=  router.urls