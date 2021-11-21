from django.db import models

# Create your models here.
class participants(models.Model):
    participant_id=models.CharField(max_length=100,primary_key=True)
    participant_password=models.CharField(max_length=100)
    participant_email=models.CharField(max_length=100)
    task_id=models.CharField(max_length=100)
    recording_url=models.CharField(max_length=100)
    notes_url=models.CharField(max_length=100)