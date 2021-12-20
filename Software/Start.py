# -*- coding: utf-8 -*-
"""
Created on Wed Nov 3 14:10:00 2021

@author: Ralf
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from IndiaWorkshop_MainWindow import MainWindow
from StepperMotorClass import StepperMotor
from LedClass import LED
from CameraPreviewClass import CameraPreview


steppermotor = StepperMotor()
led = LED()
preview = CameraPreview()

app = QApplication([])
start_window = MainWindow()
start_window.show()
app.exit(app.exec_())