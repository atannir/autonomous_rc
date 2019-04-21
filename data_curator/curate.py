#!/usr/bin/env python3

# import qtpy # not qt, nor pyqt, qt5, pyqt5...
# Could have just said 'cutie pie' -> qtpy
# Actually qtpy is a layer for PyQT5, PySide2, PyQt4, and PySide
# https://github.com/spyder-ide/qtpy
# PyQt5 used by default unless the QT_API is set.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# Clean up once we know which parts we want

import os

startdir = os.getcwd()
now = QDate.currentDate()

#print(startdir)

# Layout should be graphic on the right and file list on the left.
# There will be a small bar under the graphic with play and stop
# Depending on layout, might change modify buttons to be under file list
# Or have all controls and modify be on the left side.

# Create window
# Make setup
# Get file list based on filter

app = QApplication([]) # set up the framework
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Exit')
#button.clicked.connect(QApplication.quit())
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec_()

# app.exec_()
