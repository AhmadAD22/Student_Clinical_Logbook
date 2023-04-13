from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields =['id','academic_number','first_name','mid_name','last_name','academic_year']