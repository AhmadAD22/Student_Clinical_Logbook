from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import UserProfile
from django.contrib.auth.models import User, Group
from .models import UserProfile
from .serializers import UserProfileSerializer,CraeteUserSerializer,ListUserSerializer
from rest_framework import status


class UserProfileViewSet(GenericViewSet,mixins.UpdateModelMixin):
    serializer_class = UserProfileSerializer
    queryset=UserProfile.objects.all()
    
    def update(self, request, *args, **kwargs):
        query_dict = request.data.copy() 
        group_name=query_dict.pop("group", None)
        group=Group.objects.filter(name=group_name).first()
        if group:
            user=User.objects.filter(id=kwargs['pk']).first()
            user_profile=UserProfile.objects.filter(user=user).first()
            serializer = self.get_serializer(user_profile, data=query_dict, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            user.groups.set([group])
            data = serializer.data
            data['group'] =group.name
            return Response(data)
        else:
            return Response("the group "+group_name+" is not exist")

    def retrive(self, request, *args, **kwargs):

        user=User.objects.filter(id=kwargs['pk']).first()
        if user:    
            user_profile=UserProfile.objects.filter(user=user).first()
            serializer = self.get_serializer(user_profile)
            group=user.groups.all().first()
            if group:
                data = serializer.data
                data['group'] =group.name
                return Response(data)
            else:
                data = serializer.data
                data['group'] =" "
                return Response(data)
        else:
             return Response("User does not exists!!!")
         
    def destroy(self, request, *args, **kwargs):
        user=User.objects.filter(id=kwargs['pk']).first()
        user_profile=UserProfile.objects.filter(user=user).first()
        user_profile.delete()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def set_password(self, request, *args, **kwargs):
        user=User.objects.filter(id=kwargs['pk']).first()
        if user:
            user.set_password(self.request.data.get("new_password"))
            user.save()
            return Response({"new_password":self.request.data.get("new_password")})
        else:
            return Response("User does not exists!!!")        
    
class ListUsers(GenericViewSet):
    queryset=UserProfile.objects.all()
    def list(self,request):
        queryset=UserProfile.objects.all()
        serializer=ListUserSerializer(queryset,many=True)
        return Response(serializer.data)
         
class CreateUser(mixins.CreateModelMixin,GenericViewSet):

    queryset =User.objects.all()
    serializer_class=CraeteUserSerializer
    
    def create(self, serializer):
        
        test_id=UserProfile.objects.filter(academic_id=self.request.data.get("academic_id"))
        if(test_id):
                return Response("Id  already exists")
        try:
            group = Group.objects.get(name=self.request.data.get("group"))
        except Group.DoesNotExist:
            return Response("the group is not exists")         
           
        test_user=User.objects.filter(username=self.request.data.get("username"))
        if (test_user):
            return Response("Username  already exists")
        else:
            new_user = User.objects.create(username=self.request.data.get("username"),
                                       first_name=self.request.data.get("first_name"),
                                       last_name=self.request.data.get("last_name"),
                                       )
            new_user.set_password(self.request.data.get("password"))
            group.user_set.add(new_user)
            new_user.save()
            new_profile=UserProfile.objects.create(user=new_user,academic_id=self.request.data.get("academic_id") )                                    
            new_profile.save()
            return Response({
                "id": new_user.id,
                "usrename":new_user.username,
                "password":self.request.data.get("password"),
                "group": group.name
            })
#Get permission by Group
def getgroup(user):
        if user.groups.filter(name='Supervisor').exists():
            return 'Supervisor'
        elif user.groups.filter(name='Evaluation Offiser').exists():
            return 'Evaluation Offiser'
        else :
            return 'Leader'

class CustomAuthToken(ObtainAuthToken):
  
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        #Get permission
        permission=getgroup(user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'permission':permission,
           
        })
        