
from rest_framework import routers, urlpatterns
from .views import CouseViewSet,EnrollmentViewSet,CourseList


router=routers.DefaultRouter()

router.register('course',CouseViewSet)
router.register('updatecourse',CourseList,basename='course-list')
router.register('enrollment',EnrollmentViewSet)

urlpatterns=  router.urls