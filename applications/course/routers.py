
from rest_framework import routers, urlpatterns
from .views import CouseViewSet,EnrollmentViewSet


router=routers.DefaultRouter()

router.register('course',CouseViewSet)
router.register('enrollment',EnrollmentViewSet)

urlpatterns=  router.urls