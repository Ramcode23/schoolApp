
from django.urls.conf import path
from rest_framework import routers, urlpatterns
from .views import CourseListAPIView, CourseRetrieveAPIView, CouseViewSet,EnrollmentViewSet


router=routers.DefaultRouter()

router.register('course',CouseViewSet)
router.register('enrollment',EnrollmentViewSet)

urlpatterns=[  
    path('course-list', CourseListAPIView.as_view(), name='course-lists'),
    path('course-details/<int:pk>', CourseRetrieveAPIView.as_view(), name='course-details'),

] + router.urls