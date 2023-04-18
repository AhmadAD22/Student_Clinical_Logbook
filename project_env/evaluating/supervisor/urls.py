from django.urls import path
from . import views

urlpatterns = [
    #add and remove leaders to students(students group leded by leader)
    path('leaders/<int:supervisor_id>',views.ListLeadersViewset.as_view({'get':'list_leaders'})),
    path('leaders/students/',views.ListStudents.as_view({'get':'without_leader'})),
    path('leaders/students/<int:leader_id>/',views.ListStudents.as_view({'get':'specific_leader'})),
    path('leaders/students/<int:leader_id>/select',views.SelectStudents.as_view({'post':'select'})),
    path('leaders/tudents/<int:leader_id>/unselect',views.SelectStudents.as_view({'post':'unselect'})),
    #Show the Evaluations
     path('show/evaluate/student/<int:student_id>/',views.ShowEvaluationsiewset.as_view({'get':'list'})),
   
  
    
]



