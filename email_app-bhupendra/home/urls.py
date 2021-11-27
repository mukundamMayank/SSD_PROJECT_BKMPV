from django.contrib import admin
from django.urls import path,include

from home import views

urlpatterns = [
    path('', views.index , name='home'),
    path('send', views.send , name='send'),
    path('observer', views.observer_home,name='observer'),
    path('observer/add_home', views.add_home,name='observerAddHome'),
    path('observer/login_home', views.login_home,name='observerLoginHome'),
    path('observer/signup', views.signup,name='observerSignup'),
    path('observer/login', views.login,name='observerLogin'),
    path('observer/add_task', views.add_task,name='observerAddTask'),
    path('observer/logout', views.logout,name='observerLogout'),
    path('participant/activity', views.participant_activity,name='participantActivity'),
    path('participant/perform_task', views.perform_task,name='participantPerformTask'),
]