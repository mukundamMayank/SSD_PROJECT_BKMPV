from django.db import models

# Create your models here.
class Notes(models.Model):
    user_id = models.CharField(max_length=100,primary_key=True)
    task_id = models.CharField(max_length=100)
    notes_path = models.CharField(max_length=100)
    notes_descr = models.CharField(max_length=2000)