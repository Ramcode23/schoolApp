from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from .permission import  IsLoggedInUserOrAdmin, IsAdminOrAnonymousUser
from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_authenticators(self):
       if  self.request.method!='POST':
          self.authentication_classes.append(TokenAuthentication)
       return [auth() for auth in self.authentication_classes]

    def get_permissions(self):
        permission_classes = []    
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class LoginView(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().as_view()(request=request._request)


class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
    
    