
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
   path("",views.index, name="home"),
   path("user_details",views.get_user_details, name = "user_details"),
   path("notes", views.add_notes, name="notes"),
   path("notes_submission", views.notes_submission, name="notes_submission")

]
