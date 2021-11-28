from django.shortcuts import render, HttpResponse
from .models import Notes
user = ""
task = ""

# Create your views here.
def index(request):
    return HttpResponse("Home Page")


def get_user_details(request):
    return render(request, "user_details.html")


def add_notes(request):
    global user
    user = request.POST.get("user")
    global task
    task = request.POST.get("task")
    data = Notes.objects.all()
    video_url = ""
    for record in data:
        if record.user_id == user and record.task_id == task:
            video_url = record.rec_url

    context = {
        'path': video_url
    }
    return render(request, "notes.html", context)


def notes_submission(request):
    global user,task
    descr = request.POST.get("feedback")
    print(descr)
    path = ""
    path += str(user) + '_' + str(task) + ".txt"
    f = open(path, "w")
    f.write(descr)
    f.close()

    notes_info = Notes(user_id=user, task_id=task, notes_path=path, notes_descr=descr)
    user=""
    task=""
    notes_info.save()
    return render(request, "notes_submission.html")
