import re
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import hashlib

from home.models import Observer, Participant,Tasks,Recording

from django.contrib.auth import authenticate
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

def observer_home(request):
    return render(request,'observer_home.html')

def login_home(request):
    return render(request,'login_home.html')

def add_home(request):
    return render(request,'add_home.html')

def signup(request):
    if request.method == 'POST':
        id=request.POST.get('observer_id')
        email=request.POST.get('observer_email')
        # password=hashlib.md5(request.POST.get('observer_password'))
        password=request.POST.get('observer_password')
        result=Observer.objects.raw('select * from home_observer where observer_id=%s ',[id])
        if len(result)!=0:
            return render(request,'add_home.html',{'error':'Id already exist.'})
        Observer(observer_id=id,observer_email=email,observer_password=password).save()
        return render(request,'add_home.html',{'success':'Account Created Successfully'})
    else:
        return render(request,'add_home.html',{'error':'POST req not found.'})

def login(request):
    if request.method=='POST':
        id=request.POST.get('observer_id')
        password=request.POST.get('observer_password')
        result=Observer.objects.raw('select * from home_observer where observer_id=%s and observer_password=%s',[id,password])
        # print('RESULT',len(result))
        if len(result)==0:
            return render(request,'login_home.html',{'error':'Username/Password Incorrect'})
        else:
            request.session['id']=id
            result_task=Tasks.objects.raw('select * from home_tasks')
            if len(result_task)==0:
                return render(request,'observer_login.html',{'observer_id':request.session.get('id',""),'task_msg':'No Task found'})
            else:
                tasks=list()
                for i in result_task:
                    tasks.append(i.task_name)
                return render(request,'observer_login.html',{'observer_id':request.session.get('id',""),'task_list':tasks})

def logout(request):
    request.session['id']=id
    return render(request,'login_home.html')

# def observer_home(request):
#     result_task=Tasks.objects.raw('select * from home_tasks')
#     if len(result_task)==0:
#         return render(request,'observer_login.html',{'observer_id':global_userid,'task_msg':'No Task found'})
#     else:
#         tasks=list()
#         for i in result_task:
#             tasks.append(i.task_name)
#         return render(request,'observer_login.html',{'observer_id':global_userid,'task_list':tasks})
def get_tasks():
    tasks=list()
    result_task=Tasks.objects.raw('select * from home_tasks')
    if len(result_task)!=0:
        for i in result_task:
            tasks.append(i.task_name)
    return tasks

def add_task(request):
    task_n=request.POST.get('task_name')
    result_task=Tasks.objects.raw('select * from home_tasks where task_name=%s',[task_n])
    if len(result_task)==0:
        Tasks(task_name=task_n).save()
        msg='Added Successfully'
    else:
        msg='Task already exist'
    tasks=get_tasks()
    if len(tasks)==0:
        return render(request,'observer_login.html',{'add_task_msg':msg,'observer_id':request.session.get('id',""),'task_msg':'No Task found'})
    else:
        return render(request,'observer_login.html',{'add_task_msg':msg,'observer_id':request.session.get('id',""),'task_list':tasks})
    
def participant_activity(request):
    participant_task=request.POST.getlist('participant_tasks')
    participant_email=request.POST.get('participant_email')
    participant_name=request.POST.get('participant_name')
    participant_age=request.POST.get('participant_age')
    participant_gender=request.POST.get('participant_gender')
    tasks=get_tasks()
    result_participant=Participant.objects.raw('select * from home_participant where participant_email=%s',[participant_email])
    if len(result_participant)!=0:
        # result_recording=Recording.objects.raw('select * from home_recording where recording_id like \'%s\' ',[participant_email+'%'])
        result_recording=Recording.objects.raw('select * from home_recording')
        # f=False
        if len(result_recording)!=0:
            for i in result_recording:
                task_id_=i.recording_id.split(',')
                participant_email_=task_id_[0]
                task_id_=task_id_[1]
                if task_id_ in participant_task and participant_email==participant_email_:
                    return render(request,'observer_login.html',{'perform_activity_msg':"Please select only those task(s) which are not performed by participant.",'observer_id':request.session.get('id',""),'task_list':list(get_tasks())})
        for i in participant_task:
            # Recording(participant_id=request.POST.get('participant_email'),task_id=i,recording_url="",notes_url="").save()
            Recording(recording_id=participant_email+','+i,recording_url="",notes_url="").save()
        request.session['participant_email']=participant_email
        return render(request,'participant_activity.html',{'tasks':participant_task})       
    else:
        request.session['participant_email']=participant_email
        Participant(participant_email=participant_email,participant_age=participant_age,participant_gender=participant_gender,participant_name=participant_name).save()
        for i in participant_task:
            # Recording(participant_id=request.POST.get('participant_email'),task_id=i,recording_url="",notes_url="").save()
            Recording(recording_id=participant_email+','+i,recording_url="",notes_url="").save()
        return render(request,'participant_activity.html',{'tasks':participant_task})

def perform_task(request):
    task_name=request.POST.get('task_name')
    return render(request,'perform_activity.html',{'participant_id':request.session.get('participant_email',""),'task_id':task_name})
#task addition
#replace participant with observer
#register Task model