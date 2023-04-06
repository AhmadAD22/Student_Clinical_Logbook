from django.contrib.auth.models import User
from rest_framework import serializers



class CraeteUserSerializer(serializers.ModelSerializer):
    # subjets=serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username','password',]
        # extra_kwargs = {'password': {'write_only': True}}
