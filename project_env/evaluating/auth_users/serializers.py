from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserProfile

class CraeteUserSerializer(serializers.ModelSerializer):
    # subjets=serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username','password',]
        # extra_kwargs = {'password': {'write_only': True}}

class DeleteUserSerializer(serializers.ModelSerializer):
    # subjets=serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields ='__all__'
        
class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    
    class Meta:
        model = UserProfile
        fields = ('id','academic_id','username','first_name','last_name',)
    
    def update(self, instance, validated_data):
        # Update the UserProfile instance
        instance.academic_id = validated_data.get('academic_id', instance.academic_id)
        instance.save()

        # Update the related User instance
        user_data = validated_data.pop('user', {})
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()

        return instance
               
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields =['name',]

class ListUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    group = GroupSerializer(many=True, source='user.groups')
    
    class Meta:
        model = UserProfile
        fields = ('id','academic_id','username','first_name','last_name','group')
   
    