from django.db import models

# Create your models here.

class recording(models.Model):
    user_id = models.CharField(max_length=100,primary_key=True)
    task_id = models.CharField(max_length=100)
    rec_id = models.CharField(max_length=100)

def upload(request):
    if request.method=='POST':
        user_id = request.POST.get('user_id')
        task_id = request.POST.get('task_id')
        rec_id = request.POST.get('rec_id')
        recording(user_id=user_id,task_id=task_id,rec_id=rec_id)
        return render(request,'add_home.html',{'success':'Recording Uploaded Successfully'})
    else:
        return render(request, 'add_home.html', {'error': 'POST req not found.'})