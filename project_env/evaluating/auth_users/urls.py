from django.urls import path
from . import views

urlpatterns = [
    path('',views.CustomAuthToken.as_view()),
    path('signup/',views.CreateUser.as_view({'post':'create'})),
    path('users/',views.ListUsers.as_view({'get':'list'})),
    path('users/<int:pk>',views.UserProfileViewSet.as_view({'put':'update','get':'retrive',"delete":"destroy"})),
]
