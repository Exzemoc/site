from django.urls import path
from . import views

urlpatterns = [
    path('str1', views.str1, name='index'),
    path('str2/', views.str2, name='home'),
    path('str3/', views.str3, name='dom')
]