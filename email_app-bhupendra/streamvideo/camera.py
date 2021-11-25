import cv2
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        frame_width = int(self.video.get(3))
        frame_height = int(self.video.get(4))
        self.size = (frame_width, frame_height)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        
        ret, jpeg = cv2.imencode('.jpg', image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return jpeg.tobytes(),image
    
