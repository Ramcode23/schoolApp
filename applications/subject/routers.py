from rest_framework import routers, urlpatterns

from .views import SubjectViewSet

router=routers.DefaultRouter()

router.register('Subject',SubjectViewSet)

urlpatterns=  router.urls