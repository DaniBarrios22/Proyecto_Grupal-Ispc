from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializer import CourseSerializer, UserSerializer
from .models import Course, User


class CourseViewSet(viewsets.ModelViewSet):
 queryset=Course.objects.all()
 serializer_class= CourseSerializer

class UserViewSet(viewsets.ModelViewSet):
 queryset=User.objects.all()
 serializer_class= UserSerializer