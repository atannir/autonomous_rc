#!/usr/bin/env python3

# More from Rapid GUI Prototyping in Python with Qt
# We are using Python 3 and Qt5, so some changes made.

# https://pythonspot.com/category/pyqt5/
# Another helpful link
#
# For converting the signaling code
# https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html
# https://stackoverflow.com/questions/46876880/correct-way-to-convert-old-signal-and-slot-to-new-style
# https://stackoverflow.com/questions/44936202/to-pyqt5-connect-conversion
#
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLineEdit.html

# In original, from __future__ import division
import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QApplication, QTextBrowser, QLineEdit, QVBoxLayout
from PyQt5.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None): # window parent, not class parent
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and hit Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout() # vertical box layout, handles resizing etc
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        # self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUi)
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            # text = unicode(self.lineedit.text())
            text = self.lineedit.text()
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
            self.lineedit.setText('') # for convenience, not cleared on error
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec()
