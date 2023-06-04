from rest_framework import serializers
from .models import Course, User, Teacher, Student

class CourseSerializer(serializers.ModelSerializer):
 class Meta:
  model= Course
  fields='__all__'
  #fields=('nombre','observacion')

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model= User
  fields='__all__'
  #fields=('nombre','observacion')

class TeacherSerializer(serializers.ModelSerializer):
 class Meta:
  model= Teacher
  fields='__all__'
  #fields=('nombre','observacion')

class StudentSerializer(serializers.ModelSerializer):
 class Meta:
  model= Student
  fields='__all__'
  #fields=('nombre','observacion')