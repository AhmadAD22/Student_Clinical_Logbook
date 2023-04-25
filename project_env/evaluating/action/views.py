from rest_framework import mixins
from rest_framework import generics
from .models import Action,ActionInformation
from .serializers import ActionSerializer,ActionInformationSerializer,AddActionInformationSerializer,UpdateActionSerializer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status



#Action
class ActionViewset(GenericViewSet):
    queryset =Action.objects.all()
   # authentication_classes = [authentication.TokenAuthentication]
   
    def list(self,request ,*args, **kwargs):
        serializer= ActionSerializer(self.queryset,many=True)
        return Response(serializer.data)

    def listbyclass(self,request,type):
        queryset =Action.objects.filter(type=type)
        serializer= ActionSerializer(queryset,many=True)
        return Response(serializer.data)
    
class DetaledActionMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset=Action.objects.all()
    serializer_class=UpdateActionSerializer

    def get (self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put (self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

#Actin Information
class ActionInfornationViewset(GenericViewSet):
    
    queryset =ActionInformation.objects.all()
    serializer_class= AddActionInformationSerializer

   # authentication_classes = [authentication.TokenAuthentication]
    def list(self,request):
        queryset =ActionInformation.objects.all()
        serializer= ActionInformationSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def addactioninfo(self,request,student_pk,action_pk):
        action=Action.objects.filter(pk=action_pk).first()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(Action=action)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    