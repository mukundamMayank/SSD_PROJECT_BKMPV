from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http.response import Http404, StreamingHttpResponse
from streamvideo.camera import VideoCamera
from django.http import FileResponse
import imageio
import cv2

to_record = False
cam = VideoCamera()
resume = True
temp_file = './streamvideo/templates/filename.mp4'
# result = cv2.VideoWriter('./streamvideo/templates/filename.mp4', 
#                              cv2.VideoWriter_fourcc(*'avc1'),
#                              25, cam.size)

writer = imageio.get_writer(temp_file, fps=25)

def index(request):
    return render(request, 'home.html')

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
    