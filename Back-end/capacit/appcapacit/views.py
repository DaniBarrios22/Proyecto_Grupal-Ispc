from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializer import CourseSerializer, UserSerializer, TeacherSerializer
from .models import Course, User, Teacher


class CourseViewSet(viewsets.ModelViewSet):
 queryset=Course.objects.all()
 serializer_class= CourseSerializer

class UserViewSet(viewsets.ModelViewSet):
 queryset=User.objects.all()
 serializer_class= UserSerializer

class TeacherViewSet(viewsets.ModelViewSet):
 queryset=Teacher.objects.all()
 serializer_class= TeacherSerializer 