
from rest_framework import routers, urlpatterns
from .views import CouseViewSet


router=routers.DefaultRouter()

router.register('course',CouseViewSet)

urlpatterns=  router.urls