
from django.urls import path
from . import views

urlpatterns = [
    path('evaluationofficer',views.ListEvaluationOffiser.as_view({'get':'list'})),
    path('evaluationofficer/leaders',views.ListLeaders.as_view({'get':'without_evaluation_offiser'})),
    path('evaluationofficer/leaders/<int:evaluation_offiser_id>',views.ListLeaders.as_view({'get':'specific_evaluation_offiser'})),
    path('evaluationofficer/leaders/<int:evaluation_offiser_id>/select',views.SelectLeaders.as_view({'post':'select'})),
    path('evaluationofficer/leaders/<int:evaluation_offiser_id>/unselect',views.SelectLeaders.as_view({'post':'unselect'})),
   
]
