# -*- coding: utf-8 -*-
"""
Created on Wed Nov 3 14:12:00 2021

@author: Ralf
"""
import sys
import time 
import numpy as np
import RPi.GPIO as GPIO

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, QTimer, QVariant
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QSlider, QMessageBox, QDialog, QFileDialog

from IndiaWorkshopUI import Ui_MainWindow
from StepperMotorClass import StepperMotor
from LedClass import LED
from CameraPreviewClass import CameraPreview


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.steppermotor = StepperMotor()
        self.led = LED()
        self.preview = CameraPreview() #change all parts after this!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        self.largeSteps = 5
        self.smallSteps = 1
        self.largeStepsZ = 50
#StepperMotorsSignals############################################################################################
        
        self.LargeLeftButton.clicked.connect(self.LargeLeft)
        self.SmallLeftButton.clicked.connect(self.SmallLeft)
        
        self.LargeRightButton.clicked.connect(self.LargeRight)
        self.SmallRightButton.clicked.connect(self.SmallRight)
        
        self.LargeTopButton.clicked.connect(self.LargeYUp)
        self.SmallTopButton.clicked.connect(self.SmallYUp)
        
        self.LargeBottomButton.clicked.connect(self.LargeYDown)
        self.SmallBottomButton.clicked.connect(self.SmallYDown)
        
        self.LargeUpButton.clicked.connect(self.LargeZUp)
        self.SmallUpButton.clicked.connect(self.SmallZUp)
        
        self.LargeDownButton.clicked.connect(self.LargeZDown)
        self.SmallDownButton.clicked.connect(self.SmallZDown)

#LEDSignals############################################################################################
        
        self.AllLEDButton.clicked.connect(self.led.LEDon)
        
        self.BrightnessValue.valueChanged['int'].connect(self.LEDchange)

#CameraPreview and Save############################################################################################
        
        self.StartCameraButton.clicked.connect(self.preview.StartPreviewThread)
        self.ExitButton.clicked.connect(self.preview.StopPreview)
        
        self.SaveImageButton.clicked.connect(self.ImageGrab)
        
#StepperMotorsMethods###############################################################################################
    
    def LEDchange(self):
        LEDbright = self.BrightnessValue.value()
        self.led.LEDbrightness(LEDbright)
        
    def ImageGrab(self):
        NewName = self.FilenameEdit.text()
        self.preview.GrabImage(NewName)
    
    def SmallLeft(self):
        smallLeft = self.smallSteps
        self.steppermotor.XMoveLeftStart(smallLeft)

    def LargeLeft(self):
        largeLeft = self.largeSteps
        self.steppermotor.XMoveLeftStart(largeLeft)

    def SmallRight(self):
        smallRight = self.smallSteps
        self.steppermotor.XMoveRightStart(smallRight)

    def LargeRight(self):
        largeRight = self.largeSteps
        self.steppermotor.XMoveRightStart(largeRight) 

    def SmallYUp(self):
        smallYUp = self.smallSteps
        self.steppermotor.YMoveUpStart(smallYUp)

    def LargeYUp(self):
        largeYUp = self.largeSteps
        self.steppermotor.YMoveUpStart(largeYUp) 

    def SmallYDown(self):
        smallYDown = self.smallSteps
        self.steppermotor.YMoveDownStart(smallYDown)

    def LargeYDown(self):
        largeYDown = self.largeSteps
        self.steppermotor.YMoveDownStart(largeYDown)        

    def SmallZUp(self):
        smallZUp = self.smallSteps
        self.steppermotor.ZMoveUpStart(smallZUp)

    def LargeZUp(self):
        largeZUp = self.largeStepsZ
        self.steppermotor.ZMoveUpStart(largeZUp) 

    def SmallZDown(self):
        smallZDown = self.smallSteps
        self.steppermotor.ZMoveDownStart(smallZDown)

    def LargeZDown(self):
        largeZDown = self.largeStepsZ
        self.steppermotor.ZMoveDownStart(largeZDown) 

        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exit(app.exec_())       
        
        
        
        
        
        
        
        
        
        
        
        