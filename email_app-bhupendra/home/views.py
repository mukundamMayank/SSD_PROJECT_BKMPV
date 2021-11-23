import re
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import hashlib
from home.models import participants
from home.models import Tasks
from django.contrib.auth import authenticate
from home.models import participants
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    context= {'email':'NULL' , 'body':'NULL' , 'response':'NULL'}
    return render(request,'index.html',context)
    #return HttpResponse("Home Page")
def send(request):
    if request.method == "POST":
        email=request.POST.get('to_email')
        email=list(email.split(','))
        body=request.POST.get('email_body')
        response=send_mail('Meeting Scheduled',body,settings.EMAIL_HOST_USER,email,fail_silently=False)
        context= {'email':email , 'body':body , 'response': response}
        return render(request,'index.html',context)
    context= {'email':'NULL' , 'body':'NULL'}
    return render(request,'index.html',context)

def participant_home(request):
    return render(request,'participant_home.html')

def login_home(request):
    return render(request,'login_home.html')

def add_home(request):
    return render(request,'add_home.html')

def add(request):
    if request.method == 'POST':
        id=request.POST.get('participant_id')
        email=request.POST.get('participant_email')
        # password=hashlib.md5(request.POST.get('participant_password'))
        password=request.POST.get('participant_password')
        participants(participant_id=id,participant_email=email,participant_password=password).save()
        return render(request,'add_home.html',{'success':'Account Created Successfully'})
    else:
        return render(request,'add_home.html',{'error':'POST req not found.'})

def login(request):
    if request.method=='POST':
        id=request.POST.get('participant_id')
        password=request.POST.get('participant_password')
        result=participants.objects.raw('select * from home_participants where participant_id=%s and participant_password=%s',[id,password])
        print('RESULT',len(result))
        if len(result)==0:
            return render(request,'login_home.html',{'error':'Username/Password Incorrect'})
        else:
            task_list = []
            for i in range(1, 10):
            	task_list.append("task " + str(i))
            	Tasks(task_name=task_list[i-1])
            return render(request,'participant_login.html',{'participant_id':id, 'task_list':task_list})