from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed',views.video_feed,name='video_feed'),
    path('toggle',views.toggle,name='toggle'),
    path('saved_vid',views.saved_vid,name='saved_vid'),
    path('pause_vid',views.pause_vid,name='pause_vid'),
    path('upload',views.upload,name='upload')
]