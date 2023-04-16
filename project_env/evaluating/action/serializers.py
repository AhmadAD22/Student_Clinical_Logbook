from rest_framework import serializers
from .models import Action,ActionInformation

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Action
        fields ='__all__'
        
class ActionInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model =ActionInformation
        fields ='__all__'
        
class AddActionInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model =ActionInformation
        fields =['id','place','patient_type','complexity_level',]