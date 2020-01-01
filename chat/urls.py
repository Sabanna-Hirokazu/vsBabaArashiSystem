# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vs/', views.vs, name='room'),
    path('parents/', views.parents, name='room'),
]