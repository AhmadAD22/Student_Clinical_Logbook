from django.urls import path
from . import views

urlpatterns = [
    #add leaders to students(students group leded by leader)
    path('leaders/add/',views.ListLeadersViewset.as_view({'get':'list_leaders'})),
    path('leaders/add/students/',views.ListStudents.as_view({'get':'without_leader'})),
    path('leaders/add/students/<int:leader_id>/',views.SelectStudents.as_view({'post':'select'})),
    #Retrive and edit students group
    path('leaders/edit',views.ListLeadersViewset.as_view({'get':'all_leaders'})),
    path('leaders/edit/students/<int:leader_id>/',views.ListStudents.as_view({'get':'specific_leader'})),
    path('leaders/edit/students/<int:leader_id>/unselect',views.SelectStudents.as_view({'post':'unselect'})),
    
]



