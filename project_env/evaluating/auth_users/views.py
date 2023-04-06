from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import CraeteUserSerializer
from .models import UserProfile
from django.contrib.auth.models import Group







class CreateUser(mixins.CreateModelMixin,GenericViewSet):

    queryset =User.objects.all()
    serializer_class=CraeteUserSerializer
    
    def create(self, serializer):
        
        test_id=UserProfile.objects.filter(user_id=self.request.data.get("userid"))
        if(test_id):
                return Response("Id  already exists")
           
        test_user=User.objects.filter(username=self.request.data.get("username"))
        
        if (test_user):
            return Response("Username  already exists")
        else:
            new_user = User.objects.create(username=self.request.data.get("username"),
                                       first_name=self.request.data.get("first_name"),
                                       last_name=self.request.data.get("last_name"),
                                       )
            new_user.set_password(self.request.data.get("password"))
            group = Group.objects.get(name=self.request.data.get("group"))
            group.user_set.add(new_user)
            new_user.save()
            
            new_profile=UserProfile.objects.create(user_name=new_user,user_id=self.request.data.get("userid") )
                                                   
            new_profile.save()
            return Response("Ok")


#Get permission by Group
def getgroup(user):
        if user.groups.filter(name='Admins').exists():
            return 'Admin'
        elif user.groups.filter(name='Supervisors').exists():
            return 'Supervisor'
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
            'permission':permission,
           
        })
        

   