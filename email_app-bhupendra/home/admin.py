from django.contrib import admin

# Register your models here.
from home.models import Observer,Tasks,Participant,Recording
admin.site.register(Observer)
admin.site.register(Tasks)
admin.site.register(Participant)
admin.site.register(Recording)