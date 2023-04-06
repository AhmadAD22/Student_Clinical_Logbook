from django.urls import path
from . import views


urlpatterns = [
     path('<int:pk>',views.DetaledEvaluationMixins.as_view(),name='mde'),
     path('abstract/<int:pk>',views.DetaledScientificAbstractMixins.as_view(),name='mdsa'),
 
]
