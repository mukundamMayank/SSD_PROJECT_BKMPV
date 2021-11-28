from django.contrib import admin
from django.urls import path,include

from home import views

urlpatterns = [
    path('', views.index , name='home'),
    path('dashboard.html', views.dashboard, name = 'observerDashboard'),
    path('login', views.login_observer,name = 'observerLogin'),
    path('observer/tasks', views.observer_tasks, name = 'observerTasks'),
    path('observer/tasks/edit', views.edit_observer_task, name = 'editObserverTasks'),
    path('observer/tasks/remove', views.remove_observer_task, name = 'removeObserverTasks'),
    path('participant/add', views.add_participant,name='participantAdd'),
    path('connection/add', views.add_connection,name='connectionAdd'),
    path('email/send', views.send , name='send'),
    path('participant/login', views.participant_login,name = 'participantLogin'),
    path('participant_login.html', views.participant_index , name='participant_home'),
    path('participant_home.html', views.participant_home, name = 'participantDashboard'),
    path('video_feed',views.video_feed,name='video_feed'),
    path('toggle',views.toggle,name='toggle'),
    path('saved_vid',views.saved_vid,name='saved_vid'),
    path('pause_vid',views.pause_vid,name='pause_vid'),
    path('upload',views.upload,name='upload'),
    path('download',views.download_vid,name='download_vid'),
    path('notes',views.get_notes,name='getNotes'),
    path('notes/add', views.add_notes, name = 'addNotes'),
]