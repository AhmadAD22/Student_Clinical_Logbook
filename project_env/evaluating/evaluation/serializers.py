from rest_framework import serializers
from .models import Evaluation ,ScientificAbstract

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Evaluation
        fields ='__all__'
        
class ScientificAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model =ScientificAbstract
        fields =['final_level','summary_report']