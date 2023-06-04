from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializer import CourseSerializer
from .models import Course


class CourseViewSet(viewsets.ModelViewSet):
 queryset=Course.objects.all()
 serializer_class= CourseSerializer