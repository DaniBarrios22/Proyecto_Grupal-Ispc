#from django.shortcuts import render
#Create yuor views here.

#importar curso aqui model  curso

from rest_framework import viewsets

#from .serializer import CourseSerializer
from .models import Course

#--user
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import CourseSerializer, UserSerializer, RegisterSerializer
#--User
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class CourseViewSet(viewsets.ModelViewSet):
  queryset=Course.objects.all()
  serializer_class= CourseSerializer

# --------API usuario
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
    "user": UserSerializer(user, context=self.get_serializer_context()).data,
    "token": AuthToken.objects.create(user)[1]
    })

class LoginAPI(KnoxLoginView):
  permission_classes = (permissions.AllowAny,)

  def post (self, request, format=None):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.isvalid(raises_exception=True)
    user = serializer.validated_data['user']
    login(request,user)
    return super(LoginAPI, self).post(request, format=None)