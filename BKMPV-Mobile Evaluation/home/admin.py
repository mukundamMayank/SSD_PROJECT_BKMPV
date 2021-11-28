from django.contrib import admin

# Register your models here.
from home.models import Observer, Tasks, Participants, Recordings, Emails 
admin.site.register(Observer)
admin.site.register(Tasks)
admin.site.register(Participants)
admin.site.register(Recordings)
admin.site.register(Emails)