from django.urls import path
from . import views


urlpatterns = [
    path('',views.CustomAuthToken.as_view()),
    path('api',views.hello_world),
]
