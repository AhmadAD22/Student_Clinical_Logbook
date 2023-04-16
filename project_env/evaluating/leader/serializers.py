
from rest_framework import serializers
from action.models import ActionInformation,Action
from .models import EvaluationPeper
# from action.serializers import ActionSerializer

class ActionSerialize(serializers.ModelSerializer):
    class Meta:
        model =Action
        fields ='__all__'
class ActionInformationSerializer(serializers.ModelSerializer):
    Action =ActionSerialize()
    class Meta:
        model =ActionInformation
        fields =['place','patient_type','complexity_level','case_number','Action']
        

        
class EvaluationPeperSerializer(serializers.ModelSerializer):
    class Meta:
        model =EvaluationPeper
        fields ='__all__'
        
        
class EditeEvaluationPeperSerializer(serializers.ModelSerializer):
        actioninfo=ActionInformationSerializer()
        class Meta:
            model =EvaluationPeper
            fields ='__all__'
