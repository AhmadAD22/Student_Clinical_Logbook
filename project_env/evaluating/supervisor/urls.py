from django.urls import path
from . import views



urlpatterns = [
    path('leaders',views.UserViewset.as_view({'get':'list'})),
    path('leaders/<int:leader_id>/',views.SelectStudents.as_view({'post':'create'})),
]



