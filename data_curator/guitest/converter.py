#!/usr/bin/env python3
#
# Currency converter

import sys
#import urllib3
import requests

#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QGridLayout

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.getdata()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QtWidgets.QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")

        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

        #Qt4 code
        # self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        # self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        # self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        # self.setWindowTitle("Currency")
        #pass
        # TODO add above as below to connect the components

    def updateUi(self):
            # to = unicode(self.toComboBox.currentText())
            # from_ = unicode(self.fromComboBox.currentText()) # need _ since from is reserved
            # amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
            # self.toLabel.setText("%0.2f" % amount)
        pass

    def getdata(self):
        # Idea from Python Cookbook, as listed in Rapid GUI Programming
        self.rates = {}
        try:
            date = "Unknown"
#            fh = urllib3.urlopen("http://www.bankofcanada.ca/"
#                                 "en/markets/csv/exchange_eng.csv")
            # string can be broken without newline because it is in parens
            #fh = requests.get("http://www.bankofcanada.ca/"
            #                  "en/markets/csv/exchange_eng.csv")
            #fh = requests.get("https://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/csv?start_date=2017-01-03")
            # These are not the rates we are looking for...
            # Also not in the right format.
            #print(fh.content)

            fx_lines = """
            
            """

            
            for line in fx_lines:
                #print(line)
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing ")):
                    continue
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass
            return "Exchange Rates Date: " + date
        except Exception as e:
            return "Failed to download:\n%s" % e


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

