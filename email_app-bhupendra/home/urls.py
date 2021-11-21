from django.contrib import admin
from django.urls import path,include

from home import views

urlpatterns = [
    path('', views.index , name='home'),
    path('send', views.send , name='send'),
    path('participants', views.participant_home,name='participant'),
    path('participants/add_home', views.add_home,name='participantAdd'),
    path('participants/login_home', views.login_home,name='participantLogin'),
    path('participants/add', views.add,name='participantAdd'),
    path('participants/login', views.login,name='participantLogin'),
]