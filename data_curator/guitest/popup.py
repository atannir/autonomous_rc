#!/usr/bin/env python3
import sys
import time
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
# https://stackoverflow.com/questions/46554746/pyqt4-to-pyqt5-how


# Taken from Chapter 4 of Rapid GUI Prototyping with Python and Qt
# Using Qt5 and Python 3 instead of Qt4 and Python 2
#

app = QApplication(sys.argv)
# This provides access to some global information taken from the environment

try:
    due = QTime.currentTime()
    message = "Alert!"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock


# https://www.programcreek.com/python/example/82618/PyQt5.QtWidgets.QLabel

while QTime.currentTime() < due:
    time.sleep(20)
    label = QtWidgets.QLabel("<font color=red size=60><b>" + message + "</b></font>") 
    label.setWindowFlags(Qt.SplashScreen)
    label.show()
    QTimer.singleShot(60000, app.quit) # 1 minute of millis
    app.exec_()
