import re
import hashlib
import os
from datetime import datetime

from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage

from django.http.response import Http404, StreamingHttpResponse
from streamvideo.camera import VideoCamera
from django.http import FileResponse
import imageio
import cv2

to_record = False
cam = VideoCamera()
resume = True
temp_file = './streamvideo/temp/temp.mp4'


from home.models import Observer, Participants, Connections
from home.models import Tasks, Recordings, Emails

# Create your views here.
def index(request):
    return render(request,'index.html')

def participant_index(request):
    return render(request,'participant_login.html')

def participant_home(request):
    return render(request,'participant_home.html')

@require_http_methods(["POST"])
def login_observer(request):
    if request.method == 'POST':
        email = request.POST.get('observer_email')
        password = request.POST.get('observer_password')
        print(email)
        print(password)

        result = Observer.objects.raw('Select * from home_observer where observer_email = %s and observer_password = %s',[email, password])
        if len(result) == 0:
            return render(request,'index.html',{'error':'Username/Password Incorrect'})

        tasks_list = Tasks.objects.all()
        plist = Participants.objects.all()
        clist = Connections.objects.all()
        return render(request,'dashboard.html', {"tasks": tasks_list, "plist": plist,
                                                "clist": clist})

def dashboard(request):
    tasks_list = Tasks.objects.all()
    plist = Participants.objects.all()
    clist = Connections.objects.all()
    return render(request,'dashboard.html', {"tasks": tasks_list, "plist": plist,
                                            "clist": clist})

def observer_tasks(request):
    if request.method == 'POST':
        title = request.POST.get('task-title')
        description = request.POST.get('task-description')

        task_obj = Tasks(task_title = title, task_description = description, 
                        added_on = datetime.now(), updated_on = datetime.now())
        task_obj.save()

        tasks_list = Tasks.objects.all()

        plist = Participants.objects.all()
        clist = Connections.objects.all()
        return render(request, 'dashboard.html', {"tasks": tasks_list, "plist": plist,
                                                    "clist": clist})
    elif request.method == 'GET':
        tasks_list = Tasks.objects.all()
        plist = Participants.objects.all()
        clist = Connections.objects.all()
        return render(request, 'dashboard.html', {"tasks": tasks_list, "plist": plist,
                                                    "clist": clist})

@require_http_methods(["POST"])
def edit_observer_task(request):
    task_id = request.POST.get('task-id')
    task_title = request.POST.get('task-title')
    task_description = request.POST.get('task-description')

    try:
        result = Tasks.objects.get(task_id = task_id)
    except Tasks.DoesNotExist:
        result = None

    if result != None:
        result.task_title = task_title
        result.task_description = task_description
        result.updated_on = datetime.now()
        result.save()      

    tasks_list = Tasks.objects.all()
    plist = Participants.objects.all()
    clist = Connections.objects.all()
    return render(request, 'dashboard.html', {"tasks": tasks_list, "plist": plist,
                                                "clist": clist})

@require_http_methods(["POST"])
def remove_observer_task(request):
    task_id = request.POST.get('task-id')
    print(task_id)
    Tasks.objects.filter(task_id = task_id).delete()

    tasks_list = Tasks.objects.all()
    plist = Participants.objects.all()
    clist = Connections.objects.all()
    return render(request, 'dashboard.html', {"tasks": tasks_list, "plist": plist,
                                                "clist": clist})   


@require_http_methods(["POST"])
def add_participant(request):
    participant_email = request.POST.get('participant-email') 
    participant_name = request.POST.get('participant-name')
    participant_age = request.POST.get('participant-age')
    participant_gender = request.POST.get('participant-gender')

    try:
        result = Participants.objects.get(participant_email = participant_email)
    except Participants.DoesNotExist:
        result = None

    if result == None:
        participant_obj = Participants(participant_email = participant_email, 
                                        participant_name = participant_name,
                                        participant_age = participant_age,
                                        participant_gender = participant_gender, 
                                        added_on = datetime.now())
        participant_obj.save()

        tasks_list = Tasks.objects.all()
        plist = Participants.objects.all()
        clist = Connections.objects.all()

        return render(request, 'dashboard.html', {"tasks": tasks_list, "plist": plist,
                                                    "clist": clist})

@require_http_methods(["POST"])
def add_connection(request):
    participant_id = request.POST.get('c-participant-id') 
    task_id = request.POST.get('c-task-id')

    try:
        result = Connections.objects.get(participants_id = participant_id,
                                        tasks_id = task_id)
    except Connections.DoesNotExist:
        connection_obj = Connections(tasks_id = task_id, participants_id = participant_id)
        connection_obj.save()

    tasks_list = Tasks.objects.all()
    plist = Participants.objects.all()
    clist = Connections.objects.all()

    return render(request, 'dashboard.html', {"tasks": tasks_list, 
                                                "plist": plist, "clist": clist})
@require_http_methods(["POST"])
def send(request):
    id = request.POST.get('participant-id')
    email = {request.POST.get('participant-email')}
    body = "You have been invited for mobile testing." 
    response=send_mail('Meeting Scheduled',body,settings.EMAIL_HOST_USER,email,fail_silently=False)
    context= {'email':email , 'body':body , 'response': response}
    tasks_list = Tasks.objects.all()
    plist = Participants.objects.all()
    clist = Connections.objects.all()
    return render(request,'dashboard.html', {"tasks": tasks_list, 
                                            "plist": plist, "clist": clist,
                                            "context" : context})

@require_http_methods(["POST"])
def participant_login(request):
    email = request.POST.get('participant_email')
    password = request.POST.get('participant_password')

    result = Participants.objects.raw('Select * from home_participants where participant_email = %s and participant_password = %s and participant_active = 1',[email, password])
    if len(result) == 0:
        return render(request,'participant_login.html',{'error':'Username/Password Incorrect'})

    tasks_list = []
    try:
        clist = list(Connections.objects.filter(participants_id = result[0], status = 0))

        for conn in clist:
            tasks_list.append(Tasks.objects.get(task_id = conn.tasks_id))
    except Participants.DoesNotExist:
        clist = None


    return render(request,'participant_home.html', {"tasks": tasks_list, "clist": clist, "pid":{"pid":result[0].participant_id}})

def gen():
    while True:
        frame,raw = cam.get_frame()
        if(to_record and resume):
            writer.append_data(raw)

        else:
            pass
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    
    return StreamingHttpResponse(gen(),
                    content_type='multipart/x-mixed-replace; boundary=frame')


def saved_vid(request):
    vid = open(temp_file,'rb')
    return FileResponse(vid)

def download_vid(request):
    connection_id = request.GET.get('connection_id')

    try:
        result = Connections.objects.get(connection_id = int(connection_id))
    except Connections.DoesNotExist:
        result = None
        
    if result != None:
        try:
            result = Recordings.objects.get(connections_id = int(connection_id))
            vid = open(result.recording_path,'rb')
            return FileResponse(vid)
        except Recordings.DoesNotExist:
            result = None
        


def toggle(request):
    if request.is_ajax() and request.method == "POST":
        global to_record
        global writer
        print(to_record)
        if(to_record):
            to_record = False
            writer.close()
            resume = True
            return JsonResponse({'result':'false'})
        else:
            writer = imageio.get_writer(temp_file, fps=25)
            to_record = True
            return JsonResponse({'result':'true'})
    else:
        return Http404

def pause_vid(request):
    if request.is_ajax() and request.method == "POST":
        global resume
        if(resume):
            resume = False
        else:
            resume = True
        return JsonResponse({'result':'done'})
    else:
        return Http404
    

@require_http_methods(["POST"])
def upload(request):
    task_id = request.POST.get('task_id')
    participant_id = request.POST.get('participant_id')
    created_on = datetime.now()
    try:
        cwd = os.getcwd()
        temp_dir = cwd + "/streamvideo/temp/"
        uploaded_file_url = "rec-" + participant_id + "-" + task_id + ".mp4"
        temp_file_url = cwd + "/streamvideo/temp/temp.mp4"
        os.rename(temp_file_url, uploaded_file_url)
        
        result = Connections.objects.get(participants_id = int(participant_id), tasks_id = int(task_id))
        result.status = 1
        result.save()

        recording_obj = Recordings(recording_path = uploaded_file_url, connections_id = result.connection_id, created_on = created_on)
        recording_obj.save()
    
    except Participants.DoesNotExist:
        result = None
    
    tasks_list = []
    if (result != None):
        try:
            clist = list(Connections.objects.filter(participants_id = int(participant_id), status = 0))

            for conn in clist:
                tasks_list.append(Tasks.objects.get(task_id = conn.tasks_id))
        except Participants.DoesNotExist:
            clist = None

    return render(request,'participant_home.html', {"tasks": tasks_list, "clist": clist, "pid":participant_id})

@require_http_methods(["POST"])
def get_notes(request):
    connection_id = request.POST.get('connection_id')


    try:
        result = Connections.objects.get(connection_id = int(connection_id))
    except Connections.DoesNotExist:
        result = None
        
    if result != None:
        try:
            result = Recordings.objects.get(connections_id = int(connection_id))

            return JsonResponse({'notes':result.notes})
        except Recordings.DoesNotExist:
            result = None

@require_http_methods(["POST"])
def add_notes(request):
    connection_id = request.POST.get('connection_id')
    notes = request.POST.get('notes')

    try:
        result = Connections.objects.get(connection_id = int(connection_id))
    except Connections.DoesNotExist:
        result = None
        
    if result != None:
        try:
            result = Recordings.objects.get(connections_id = int(connection_id))

            result.notes = notes

            result.save()

            return JsonResponse({"response":"notes saves successfully"})
        except Connections.DoesNotExist:
            result = None
    else:
        return JsonResponse({"response":"failed to save notes"})