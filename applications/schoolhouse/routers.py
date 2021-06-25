from rest_framework import routers, urlpatterns
from .views import ShoolViewSet
router=routers.DefaultRouter()
router.register('school',ShoolViewSet)
urlpatterns=  router.urls