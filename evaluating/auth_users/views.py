from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

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
        

   