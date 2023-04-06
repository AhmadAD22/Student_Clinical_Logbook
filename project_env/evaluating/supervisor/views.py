from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer,StudentSerializer
from student.models import Student



#Get All Leaders
class UserViewset(GenericViewSet):
    
    queryset =User.objects.all()
   # authentication_classes = [authentication.TokenAuthentication]
   
    def list(self,request):
        queryset =User.objects.filter(groups__name='Leaders')
        serializer= UserSerializer(queryset,many=True)
        return Response(serializer.data)
    
#Select n students to be in Leader's group
class SelectStudents(GenericViewSet):
     queryset =Student.objects.all()
     serializer_class=StudentSerializer
     def create(self,serializer,leader_id):
         #MAXIMUM NUMBER OF STUDENT YOU CAN ADD TO LEADER'S GROUP
         MAX_STUDENT=5
         selected_students=self.request.data.get("students_id")
         leader_obj=User.objects.filter(id=leader_id).first()
         count=Student.objects.filter(leader=leader_obj).count()
         student_can_add=MAX_STUDENT-count
         if(len(selected_students)>student_can_add):
             return Response("You can't Add ,This Leader has " +str(MAX_STUDENT) +" students")
         else:
             for student_id in selected_students:
                 student_obj=Student.objects.filter(id=student_id).first()
                 student_obj.leader=leader_obj
                 student_obj.save()
             count=Student.objects.filter(leader=leader_obj).count()
             student_can_add=5-count
             return Response("You can add "+str(student_can_add)+" students")
                      