
from django.urls.conf import path
from rest_framework import routers, urlpatterns
from .views import CourseListAPIView, CouseViewSet,EnrollmentViewSet


router=routers.DefaultRouter()

router.register('course',CouseViewSet)
router.register('enrollment',EnrollmentViewSet)

urlpatterns=[  path('course-list', CourseListAPIView.as_view(), name='course-lists')] + router.urls