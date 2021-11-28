from django.db import models
from datetime import datetime

# Create your models here.
class Observer(models.Model):
    observer_id=models.AutoField(primary_key=True)
    observer_username=models.CharField(max_length = 100)
    observer_password=models.CharField(max_length=100)
    observer_email=models.EmailField(max_length=100)

class Tasks(models.Model):
    task_id = models.AutoField(primary_key = True)
    task_title = models.CharField(max_length = 100, default = "Sample Task")
    task_description = models.TextField(default = None)
    added_on = models.TimeField(null = True)
    updated_on = models.TimeField(null = True)

class Participants(models.Model):
    participant_id = models.AutoField(primary_key = True)
    participant_email = models.EmailField(max_length = 100)
    participant_name= models.CharField(max_length = 100, null = True)
    participant_age= models.CharField(max_length = 100, null = True)
    participant_gender= models.CharField(max_length = 100, null = True)
    participant_active = models.BooleanField(default = True) 
    added_on = models.TimeField(null = True)

class Connections(models.Model):
    connection_id = models.AutoField(primary_key = True)
    tasks = models.ForeignKey(Tasks, on_delete = models.CASCADE, default = None)
    participants = models.ForeignKey(Participants, on_delete = models.CASCADE, default = None)
    status = models.IntegerField(default = 0)

class Recordings(models.Model):
    recording_id = models.AutoField(primary_key = True)
    recording_path = models.CharField(max_length = 100)
    created_on = models.TimeField(null = True)
    connections = models.ForeignKey(Connections, on_delete = models.CASCADE, default = None)
    notes = models.TextField(null = True)

# class Notes(models.Model):
#     notes_id = models.AutoField(primary_key = True)
#     notes_path = models.CharField(max_length = 100)
#     recordings = models.ForeignKey(Recordings, on_delete = models.CASCADE)

class Emails(models.Model):
    id = models.AutoField(primary_key = True)
    connections = models.ForeignKey(Connections, on_delete = models.CASCADE, default = None)
    isInvited = models.BooleanField(default = False)