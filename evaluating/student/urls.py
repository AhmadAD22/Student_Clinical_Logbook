from django.urls import path
from . import views


urlpatterns = [
    path('',views.StudentViewset.as_view({'get':'list'})),
    path('byyear/<int:academic_year>',views.StudentViewset.as_view({'get':'listbyclass'})),
    path('<int:pk>',views.DetaledStudentMixins.as_view(),name='mds'),
]
