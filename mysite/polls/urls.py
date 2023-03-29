from django.urls import path
from . import views

urlpatterns = [
    path('', views.indeh, name='index'),
    path('home/', views.home, name='home'),
    path('dom/', views.dom, name='dom'),
    path('tut/', views.index, name='tut'),

]