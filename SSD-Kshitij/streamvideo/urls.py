from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed',views.video_feed,name='video_feed'),
    # path('video_capture',views.video_capture,name='video_capture'),
    path('saved_vid',views.saved_vid,name='saved_vid'),
    path('toggle',views.toggle,name='toggle')
]