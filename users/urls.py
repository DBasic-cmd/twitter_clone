from django.urls import path
from .views import landing,register,login

urlpatterns = [
    path('',landing, name='twitter-landing'),
    path('register/', register, name='register'),

    path('login/', login , name='login'),
]