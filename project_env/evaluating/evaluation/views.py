from rest_framework import mixins
from rest_framework import generics
from .models import Evaluation,ScientificAbstract
from rest_framework.viewsets import GenericViewSet
from .serializers import EvaluationSerializer,ScientificAbstractSerializer
#from rest_framework.response import Response


# Create your views here.
class DetaledEvaluationMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset=Evaluation.objects.all()
    serializer_class=EvaluationSerializer

    def get (self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put (self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def post (self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def delete (self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
    
    
class DetaledScientificAbstractMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset=ScientificAbstract.objects.all()
    serializer_class=ScientificAbstractSerializer

    def get (self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put (self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def post (self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def delete (self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)