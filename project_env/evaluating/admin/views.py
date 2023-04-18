from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User
from leader.serializers import UserSerializer
from rest_framework.response import Response
from auth_users.models import UserProfile 

#MAXIMUM NUMBER OF LEADERS YOU CAN ADD TO EVALUATION OFFUSER'S GROUP
MAX_NUM_OF_LEADERS=5

class ListEvaluationOffiser(GenericViewSet):
    queryset=User.objects.filter(groups__name='Evaluation Offiser')
    
    def list (self,request,*args, **kwargs):
        filtered_evaluation_offiser=[]
        for evaluation_offiser in self.queryset:
            count=UserProfile.objects.filter(evaluation_offiser=evaluation_offiser).count()
            filtered_evaluation_offiser.append({"id":evaluation_offiser.pk,
                                         "first_name":evaluation_offiser.first_name,
                                         "last_name":evaluation_offiser.last_name,
                                         "count":count
                                         })
        return Response(filtered_evaluation_offiser)

class ListLeaders (GenericViewSet):
    queryset =User.objects.filter(groups__name='Leaders')
    #Get all leaders that aren't belong to group
    def without_evaluation_offiser(self,request,*args, **kwargs):
        filtered_leaders=[]
        for leader in self.queryset:
            leader_profile=UserProfile.objects.filter(user=leader).first()
            print(leader)
            print(leader_profile)
            if leader_profile.evaluation_offiser is None:
                filtered_leaders.append({"id":leader.pk,
                                         "first_name":leader.first_name,
                                         "last_name":leader.last_name,
                                         "academic_id":leader_profile.academic_id,
                                         })
                
        return Response(filtered_leaders)  
    # List all Leaders that have specific evaluation offiser      
    def specific_evaluation_offiser(self,request,*args, **kwargs):
        filtered_leaders=[]
        evaluation_offiser=User.objects.filter(id=kwargs['evaluation_offiser_id']).first()
        if evaluation_offiser:
            leader_profiles=UserProfile.objects.filter(evaluation_offiser=evaluation_offiser)
            print(leader_profiles)
            for  leader_profile in leader_profiles:
                filtered_leaders.append({"id":leader_profile.user.pk,
                                            "first_name":leader_profile.user.first_name,
                                            "last_name":leader_profile.user.last_name,
                                            "academic_id":leader_profile.academic_id,
                                            })
                    
            return Response(filtered_leaders)
        else:
            return Response("The evaluation offiser not exists")
     
#Select n Leaders to be in Evaluation Offiser's group
class SelectLeaders(GenericViewSet):
     queryset =User.objects.all()
     def select(self,request,*args, **kwargs):

         selected_leaders=self.request.data.get("leaders_id")
         evaluation_offiser_obj=User.objects.get(id=kwargs['evaluation_offiser_id'])
         count=UserProfile.objects.filter(evaluation_offiser=evaluation_offiser_obj).count()
         leaders_can_add=MAX_NUM_OF_LEADERS-count
         if(len(selected_leaders)>leaders_can_add):
             return Response("You can't Add ,This Evaluation Offiser has " +str(MAX_NUM_OF_LEADERS) +" Leaders")
         else:
             for leader_id in selected_leaders:
                 leader_obj=self.queryset.filter(id=leader_id).first()
                 leader__profile_obj=UserProfile.objects.filter(user=leader_obj).first()
                 leader__profile_obj.evaluation_offiser=evaluation_offiser_obj
                 leader__profile_obj.save()
             count=UserProfile.objects.filter(evaluation_offiser=evaluation_offiser_obj).count()
             leaders_can_add=5-count
             return Response("You can add "+str(leaders_can_add)+" Leader/s")
     def unselect (self,request,*args, **kwargs):
         leader_obj=self.queryset.filter(id=self.request.data.get("leader_id")).first()
         leader_profile_obj=UserProfile.objects.filter(user=leader_obj).first()
         leader_profile_obj.evaluation_offiser=None
         leader_profile_obj.save()
         return Response('The Leader has been deleted from this group')