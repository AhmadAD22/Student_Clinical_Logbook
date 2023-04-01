
from rest_framework import mixins
from rest_framework import generics
from .models import Student
from rest_framework.viewsets import GenericViewSet
from .serializers import StudentSerializer
from rest_framework.response import Response

class StudentViewset(GenericViewSet):
    
    queryset =Student.objects.all()
   # authentication_classes = [authentication.TokenAuthentication]
   
    def list(self,request):
        queryset =Student.objects.all()
        serializer= StudentSerializer(queryset,many=True)
        return Response(serializer.data)

    def listbyclass(self,request,academic_year):
        queryset =Student.objects.filter(academic_year=academic_year)
        serializer= StudentSerializer(queryset,many=True)
        return Response(serializer.data)
    



class DetaledStudentMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get (self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put (self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def post (self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def delete (self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)