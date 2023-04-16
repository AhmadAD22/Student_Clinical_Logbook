from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from action.models import Action,ActionInformation,ActionToStudent
from action.serializers import AddActionInformationSerializer,ActionSerializer
from evaluation.serializers import EvaluationSerializer,ScientificAbstractSerializer
from .serializers import EvaluationPeperSerializer,EditeEvaluationPeperSerializer
from student.models import Student
from .models import EvaluationPeper
from django.http import QueryDict
from .functions import handle_student_to_action,get_case_num

#List Actions that isn't done and the case number less than 4 for spceific Student 
class ListActions (GenericViewSet):
    serializer_class=ActionSerializer
    queryset=Action.objects.all()
    def list_actions(self, request, *args, **kwargs):
       filtered_actions=[]
       student=Student.objects.filter(pk=kwargs['student_id']).first()
       for action in self.queryset:
          action_to_student = ActionToStudent.objects.filter(action=action, student=student).first()#Get relationship between Studen and Action Models.
          if action_to_student :
               if action_to_student.case_num< 4 and (action_to_student.done == False):
                  print(action_to_student.case_num)
                  filtered_actions.append({"id": action.id, "name": action.name, "type": action.type, "case_num": action_to_student.case_num})
          else:
                  filtered_actions.append({"id": action.id, "name": action.name, "type": action.type, "case_num":0})
         
       return Response(filtered_actions)
                            
class ActionInfoView(GenericViewSet,mixins.UpdateModelMixin):
    
    queryset=ActionInformation.objects.all()
    serializer_class=AddActionInformationSerializer
    
    def create_actioninfo (self, request, *args, **kwargs):
        action_obj=Action.objects.filter(id=kwargs['action_id']).first()
        case_num=get_case_num(kwargs['student_id'],kwargs['action_id'])       
        new_actioninfo=ActionInformation.objects.create(place=self.request.data.get("place"),
                                                        patient_type=self.request.data.get("patient_type"),
                                                        complexity_level=self.request.data.get("complexity_level"),
                                                        case_number=case_num,
                                                        Action=action_obj
                                                        )
        new_actioninfo.save()
        return Response({"id":new_actioninfo.pk})
    def update_actioninfo(self, request, *args, **kwargs):
        actioninfo=ActionInformation.objects.get(pk=kwargs["pk"])
        serializer = self.get_serializer(actioninfo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    def retrive_actioninfo (self, request, *args, **kwargs):
        actioninfo=ActionInformation.objects.get(pk=kwargs["pk"])
        serializer = self.get_serializer(actioninfo)
        return Response(serializer.data)
    def delete_actioninfo(self, request, *args, **kwargs):    
        actioninfo=ActionInformation.objects.get(pk=kwargs["pk"])
        actioninfo.delete()
        return Response("deleted done!!!")
             
class EvaluationViewSet(GenericViewSet):
    serializer_class = EvaluationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return Response({'id': instance.id}) 
    
class EvaluationViewSet(GenericViewSet):
    serializer_class = EvaluationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return Response({'id': instance.id}) 
    
class ScientificAbstractViewSet(GenericViewSet):
    serializer_class = ScientificAbstractSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return Response({'id': instance.id}) 
    
class EvaluationPeperViewSet(GenericViewSet):
    serializer_class = EvaluationPeperSerializer

    def create(self, request, *args, **kwargs):
        handle_student_to_action(kwargs['student_id'],kwargs['action_id'],kwargs['evaluation_id'])            
        data={}
        data["leader"]=str(kwargs['leader_id'])
        data["student"]=str(kwargs['student_id'])
        data["actioninfo"]=str(kwargs['actioninfo_id'])
        data["evaluation"]=str(kwargs['evaluation_id'])
        data["abstract"]=str(kwargs['abstruct_id'])
        data["date"]=request.data.get("date")
        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)
        serializer = self.get_serializer(data=query_dict)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        query_dict.clear()
        return Response(serializer.data) 
        
        
#test
        

class ActionInfornationViewset(GenericViewSet):
    
    queryset =EvaluationPeper.objects.all()
    serializer_class= EditeEvaluationPeperSerializer

   # authentication_classes = [authentication.TokenAuthentication]
    def list(self,request):
        queryset =EvaluationPeper.objects.all()
        serializer=EditeEvaluationPeperSerializer(queryset,many=True)
        return Response(serializer.data)
    