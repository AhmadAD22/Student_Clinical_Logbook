from django.urls import path,register_converter
from . import views
from supervisor.views import ListStudents
from evaluation import views as evaluation_views
from .converters import DateConverter

register_converter(DateConverter, 'date')

urlpatterns = [
#Show Evaluations
 path('show/<int:student_id>/<date:today>',views.ShowEvaluationsiewset.as_view({'get':'list'})),
#Edite Evaluation Info during Evaluation process
 path('edite/actioninfo/<int:pk>',views.ActionInfoView.as_view({'put':'update_actioninfo','get':'retrive_actioninfo','delete':'delete_actioninfo'})),
 path('edite/evaluation/<int:pk>',evaluation_views.DetaledEvaluationMixins.as_view(),name='mde'),
 path('edite/abstract/<int:pk>',evaluation_views.DetaledScientificAbstractMixins.as_view(),name='mdsa'),
#Add Evaluate 
 path('evaluate/<int:leader_id>/',ListStudents.as_view({'get':'specific_leader'})),
 path('evaluate/<int:leader_id>/<int:student_id>/',views.ListActions.as_view({'get':'list_actions'})),
 path('evaluate/<int:leader_id>/<int:student_id>/<int:action_id>/',views.ActionInfoView.as_view({'post':'create_actioninfo'})),
 path('evaluate/<int:leader_id>/<int:student_id>/<int:action_id>/<int:actioninfo_id>/',views.EvaluationViewSet.as_view({'post':'create'})),
 path('evaluate/<int:leader_id>/<int:student_id>/<int:action_id>/<int:actioninfo_id>/<int:evaluation_id>/',views.ScientificAbstractViewSet.as_view({'post':'create'})),
 path('evaluate/<int:leader_id>/<int:student_id>/<int:action_id>/<int:actioninfo_id>/<int:evaluation_id>/<int:abstruct_id>',views.EvaluationPeperViewSet.as_view({'post':'create'})),
#Delete Evaluate
 path('<int:peper_id>',views.DeleteEvaluationPeper.as_view({'delete':'delete'})),

]
