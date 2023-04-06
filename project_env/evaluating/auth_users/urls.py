from django.urls import path
from . import views


urlpatterns = [
    path('',views.CustomAuthToken.as_view()),
    path('signup/',views.CreateUser.as_view({'post':'create'})),
]
