from django.db import models

# Create your models here.
class Observer(models.Model):
    observer_id=models.CharField(max_length=100,primary_key=True)
    observer_password=models.CharField(max_length=100)
    observer_email=models.CharField(max_length=100)
    task_id=models.CharField(max_length=100)
    recording_url=models.CharField(max_length=100)
    notes_url=models.CharField(max_length=100)

class Tasks(models.Model):
	task_name = models.CharField(max_length = 50, primary_key=True)

class Participant(models.Model):
    participant_email=models.CharField(max_length=50,primary_key=True)
    participant_name=models.CharField(max_length=50)
    participant_age=models.CharField(max_length=10)
    participant_gender=models.CharField(max_length=10)

class Recording(models.Model):
    recording_id=models.CharField(max_length=100,primary_key=True)
    # Participant_id=models.CharField(max_length=50,primary_key=True)
    # task_id=models.CharField(max_length=50)
    recording_url=models.CharField(max_length=100)
    notes_url=models.CharField(max_length=100)
    # class Meta:
    #     unique_together = (( 'recording_id'),)