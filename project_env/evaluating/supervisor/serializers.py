from django.contrib.auth.models import User
from rest_framework import serializers
from student.models import Student

class UserSerializer(serializers.ModelSerializer):
    # subjets=serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['id','first_name','last_name', 'username']
            
class StudentSerializer1(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields =['leader']
