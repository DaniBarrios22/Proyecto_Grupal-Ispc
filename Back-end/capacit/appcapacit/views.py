from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializer import CourseSerializer, UserSerializer, TeacherSerializer, StudentSerializer
from .models import Course, User, Teacher, Student


class CourseViewSet(viewsets.ModelViewSet):
 queryset=Course.objects.all()
 serializer_class= CourseSerializer

class UserViewSet(viewsets.ModelViewSet):
 queryset=User.objects.all()
 serializer_class= UserSerializer

class TeacherViewSet(viewsets.ModelViewSet):
 queryset=Teacher.objects.all()
 serializer_class= TeacherSerializer 
 
class StudentViewSet(viewsets.ModelViewSet):
 queryset=Student.objects.all()
 serializer_class= StudentSerializer 