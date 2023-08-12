
from rest_framework import serializers
from action.models import ActionInformation,Action
from .models import EvaluationPeper
from student.serializers import StudentSerializer
from evaluation.serializers import EvaluationSerializer,ScientificAbstractSerializer
from django.contrib.auth.models import User
from auth_users.models import UserProfile

class ActionSerialize(serializers.ModelSerializer):
    class Meta:
        model =Action
        fields ='__all__'
        
class ActionInformationSerializer(serializers.ModelSerializer):
    Action =ActionSerialize()
    class Meta:
        model =ActionInformation
        fields =['id','place','patient_type','complexity_level','case_number','Action']
             
class EvaluationPeperSerializer(serializers.ModelSerializer):
    class Meta:
        model =EvaluationPeper
        fields ='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    academic_id=serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','first_name','last_name', 'academic_id',]
        
    def get_academic_id (self, obj):
        user_profile=UserProfile.objects.get(user=obj)
        return (user_profile.academic_id)    
             
class ListEvaluationPeperSerializer(serializers.ModelSerializer):
        actioninfo=ActionInformationSerializer()
        student=StudentSerializer()
        evaluation=EvaluationSerializer()
        abstract=ScientificAbstractSerializer()
        leader=UserSerializer()
        class Meta:
            model =EvaluationPeper
            fields ='__all__'
