#stepper motor class

import time
import sys
from threading import Thread
import RPi.GPIO as GPIO

class StepperMotor():
    def __init__(self):
        
        #Use BCM GPIO references
        GPIO.setmode(GPIO.BCM)

        #Define GPIO signals to use

        self.M0Pins = [24,25,18,23]
        #self.M1Pins = [4,25,24,23]
        self.M2Pins = [19,26,6,13]
        self.M3Pins = [12,16,20,21]

        #Set all pins as output
        for pin in self.M0Pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, 0)

        #for pin in self.M1Pins:
            #GPIO.setup(pin,GPIO.OUT)
            #GPIO.output(pin, 0)

        for pin in self.M2Pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, 0)

        for pin in self.M3Pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, 0)   

        #Define step sequence
        self.seqZ = [[1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1],
               [1,0,0,1]]
        
        #Define reversed step sequence
        self.seqZreversed = [[1,0,0,1],
                       [0,0,0,1],
                       [0,0,1,1],
                       [0,0,1,0],
                       [0,1,1,0],
                       [0,1,0,0],
                       [1,1,0,0],
                       [1,0,0,0]]
        
        #Define step sequence for xy
        self.seqXY = [[0,1,0,1],
               [0,1,1,0],
               [1,0,1,0],
               [1,0,0,1]]
        
        #Define reversed step sequence for xy
        self.seqXYreversed = [[1,0,0,1],
               [1,0,1,0],
               [0,1,1,0],
               [0,1,0,1]]
        
       # self.steps = 200
        
    
    def XMoveLeftStart(self, stepNumberXL):
        self.xlstopped = False
        self.stepNumberXLeft = stepNumberXL
        xl = Thread(target=self.XMoveLeft, args=())
        xl.daemon = True
        xl.start()
        return self        
    
    def XMoveLeft(self):       
        if self.xlstopped:
            return      
        for i in range (self.stepNumberXLeft):
            for halfstep in range(4):
                for pin in range(4):
                    GPIO.output(self.M0Pins[pin], self.seqXY[halfstep][pin])
                    time.sleep(0.005)
        for pin in self.M0Pins:
            GPIO.output(pin, 0)
        self.xlstopped = True
        
    def XMoveRightStart(self, stepNumberXR):
        self.xrstopped = False
        self.stepNumberXRight = stepNumberXR
        xr = Thread(target=self.XMoveRight, args=())
        xr.daemon = True
        xr.start()
        return self 
        
    def XMoveRight(self):      
        if self.xrstopped:
            return
        for i in range (self.stepNumberXRight):
            for halfstep in range(4):
                for pin in range(4):
                    GPIO.output(self.M0Pins[pin], self.seqXYreversed[halfstep][pin])
                    time.sleep(0.005)
        for pin in self.M0Pins:
            GPIO.output(pin, 0)
        self.xrstopped = True
        
    def YMoveUpStart(self, stepNumberYU):
        self.yustopped = False
        self.setpNumberYUp = stepNumberYU
        yu = Thread(target=self.YMoveUp, args=())
        yu.daemon = True
        yu.start()
        return self

    def YMoveUp(self):        
        if self.yustopped:
            return
        for i in range (self.stepNumberYUp):
            for halfstep in range(4):
                for pin in range(4):
                    GPIO.output(self.M2Pins[pin], self.seqXY[halfstep][pin])
                    time.sleep(0.005)
        for pin in self.M2Pins:
            GPIO.output(pin, 0)
        self.yustopped = True
        
    def YMoveDownStart(self, stepNumberYD):
        self.ydstopped = False
        self.stepNumberYDown = stepNumberYD
        yd = Thread(target=self.YMoveDown, args=())
        yd.daemon = True
        yd.start()
        return self
        
    def YMoveDown(self):        
        if self.ydstopped:
            return
        for i in range (self.stepNumberYDown):
            for halfstep in range(4):
                for pin in range(4):
                    GPIO.output(self.M2Pins[pin], self.seqXYreversed[halfstep][pin])
                    time.sleep(0.005)
        for pin in self.M2Pins:
            GPIO.output(pin, 0)
        self.ydstopped = True
        
    def ZMoveUpStart(self, stepNumberZU):
        self.zustopped = False
        self.stepNumberZUp = stepNumberZU
        zu = Thread(target=self.ZMoveUp, args=())
        zu.daemon = True
        zu.start()
        return self
        
    def ZMoveUp(self):
        if self.zustopped:
            return
        for i in range (self.stepNumberZUp):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M3Pins[pin], self.seqZ[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M3Pins:
            GPIO.output(pin, 0)
        self.zustopped = True
        
    def ZMoveDownStart(self, stepNumberZD):
        self.zdstopped = False
        self.setpNumberZDown = stepNumberZD
        zd = Thread(target=self.ZMoveDown, args=())
        zd.daemon = True
        zd.start()
        return self
        
    def ZMoveDown(self):
        if self.zdstopped:
            return
        for i in range (self.stepNumberZDown):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M3Pins[pin], self.seqZreversed[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M3Pins:
            GPIO.output(pin, 0)
        self.zdstopped = True