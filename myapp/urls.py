from django.urls import path
from .views import delete_view, home, read, search

urlpatterns = [
    path('home/', home , name= 'twitter-home'),
    path('delete/<int:id>', delete_view, name='twitter-delete'),
    path('read/<int:id>', read, name='twitter-read'),
    path('search/', search, name='twitter-search')
]