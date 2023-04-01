from django.urls import path
from . import views


urlpatterns = [
    path('',views.ActionViewset.as_view({'get':'list'})),
    path('bytype/<str:type>',views.ActionViewset.as_view({'get':'listbyclass'})),
    path('<int:pk>',views.DetaledActionMixins.as_view(),name='mda'),
    path('info',views.ActionInfornationViewset.as_view({'get':'list'})),
    path('info/add/<int:student_pk>/<int:action_pk>',views.ActionInfornationViewset.as_view({'post':'addactioninfo'})),
    
    
]
