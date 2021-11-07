from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from streamvideo.camera import VideoCamera
from django.http import FileResponse
import cv2

to_record = False
cam = VideoCamera()
result = cv2.VideoWriter('./streamvideo/templates/filename.mp4', 
                             cv2.VideoWriter_fourcc(*'H264'),
                             25, cam.size)

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home.html')

def gen(camera,writer,record):
    while True:
        frame,raw = camera.get_frame()
        if(record):
            writer.write(raw)
        else:
            pass
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    
    return StreamingHttpResponse(gen(cam,result,to_record),
                    content_type='multipart/x-mixed-replace; boundary=frame')

def video_capture(request):
    # cam = VideoCamera()
    # result = cv2.VideoWriter('filename.avi', 
    #                          cv2.VideoWriter_fourcc(*'MJPG'),
    #                          30, cam.size)
    global to_record
    to_record = True
    return render(request, 'home.html')

def saved_vid(request):
    vid = open('./streamvideo/templates/filename.mp4','rb')
    return FileResponse(vid)


def toggle(request):
    global to_record
    global result
    print(to_record)
    if(to_record):
        to_record = False
        result.release()
        return render(request, 'home.html')
    else:
        result = cv2.VideoWriter('./streamvideo/templates/filename.mp4', 
                             cv2.VideoWriter_fourcc(*'H264'),
                             25, cam.size)
        to_record = True
        return render(request, 'home2.html')
    