from rest_framework import serializers

from .models import Course

from django.contrib.auth.models import User

class CourseSerializer(serializers.ModelSerializer):
 class Meta:
  model= Course
  fields='__all__'
  #fields=('nombre','observacion')

#User 
class UserSerializer (serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

#Register

class RegisterSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'], validated_data['password'])
        
        return user
