from time import sleep
import sys
from threading import Thread, Event
from picamera import PiCamera

class CameraPreview():
    def __init__(self):
        
        self.width = 800
        self.height = 600
        self.frames = 10
        self.interval = 10
        self.File = "/home/pi/"
            
    def ChangeNumberOfFrames(self,frames):
        self.frames = frames
        return self

    def ChangeInterval(self,interval):
        self.interval = interval
        return self
    
    def ChangeFile(self,file):
        self.File = str(file)
        return self
        
    def StartPreviewThread(self):
        self.pstopped = False
        self.stop = False
        p = Thread(target=self.StartPreview, args=())
        p.daemon = True
        p.start()
        return self
        
    def StartPreview(self):
        if self.pstopped:
            return
        self.camera = PiCamera()
        self.camera.resolution = (self.width,self.height)
        self.camera.start_preview(fullscreen=False, window=(300,100,900,700))
        FramesTaken = 0
        while self.stop == False:
            FramesTaken = FramesTaken + 1           
        else:
            self.camera.stop_preview()
            self.camera.close()
            
    def StopPreview(self):
        self.stop = True
        
    def GrabImage(self, filename):
        if self.pstopped:
            return
        if self.stop:
            return
        self.camera.capture(filename + ".jpg")