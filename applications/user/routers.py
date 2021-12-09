from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf.urls import url
from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user-list')
router.register('login', views.LoginView, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('account/logout/', views.LogoutView.as_view(), name='logout'),
      url(r'^signin', views.UserLoginView.as_view()),
]