from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer,StudentSerializer1
from student.models import Student
from student.serializers import StudentSerializer

#MAXIMUM NUMBER OF STUDENT YOU CAN ADD TO LEADER'S GROUP
MAX_NUM_OF_STUDENT=5
#list leaders
class ListLeadersViewset(GenericViewSet):
    queryset =User.objects.all()
   # authentication_classes = [authentication.TokenAuthentication]
   #Get All Leaders
    def list_leaders(self,request):
        leaders =User.objects.filter(groups__name='Leaders')
        filtered_leaders=[]
        for leader in leaders:
            count=Student.objects.filter(leader=leader).count()
            filtered_leaders.append({"id":leader.pk,
                                         "first_name":leader.first_name,
                                         "last_name":leader.last_name,
                                         "count":count
                                         })
        return Response(filtered_leaders)
    #list all leaders
    def all_leaders(self,request):
        leaders=User.objects.all()
        serializer=UserSerializer(leaders,many=True)
        return Response(serializer.data)
    
class ListStudents (GenericViewSet):
    queryset =Student.objects.all()
    #Get all students that aren't belong to group
    def without_leader(self,request):
        queryset =Student.objects.filter(leader=None)
        serializer= StudentSerializer(queryset,many=True)
        return Response(serializer.data)  
    #List all students that have specific leader      
    def specific_leader(self,request,leader_id):
        leader=User.objects.filter(id=leader_id).first()
        print(leader)
        students=Student.objects.filter(leader=leader)
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)  
#Select n students to be in Leader's group
class SelectStudents(GenericViewSet):
     queryset =Student.objects.all()
     serializer_class=StudentSerializer1
     def select(self,serializer,leader_id):

         selected_students=self.request.data.get("students_id")
         leader_obj=User.objects.filter(id=leader_id).first()
         count=Student.objects.filter(leader=leader_obj).count()
         student_can_add=MAX_NUM_OF_STUDENT-count
         if(len(selected_students)>student_can_add):
             return Response("You can't Add ,This Leader has " +str(MAX_NUM_OF_STUDENT) +" students")
         else:
             for student_id in selected_students:
                 student_obj=Student.objects.filter(id=student_id).first()
                 student_obj.leader=leader_obj
                 student_obj.save()
             count=Student.objects.filter(leader=leader_obj).count()
             student_can_add=5-count
             return Response("You can add "+str(student_can_add)+" students")
     def unselect (self,request,leader_id):
           student=Student.objects.get(id=request.data.get('student_id'))
           student.leader=None
           student.save()
           return Response('The student has been deleted from this group')
           