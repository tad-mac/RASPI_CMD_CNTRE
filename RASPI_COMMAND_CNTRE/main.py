#!/usr/bin/env python


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from TimeToScrapper import TimeTo
from WeatherScrapper import temperature, conditions


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(self.style_from_file("style.qss"))
        self.init_ui()

    def init_ui(self):
        self.title = QLabel("COMMAND CENTER")
        self.width = 640
        self.height = 480
        self.top = 10
        self.left = 10
        self.showTime = QLabel("")
        self.StartLocation1 = "New York"
        self.EndLocation1 = "San Fransico"
        self.StartLocation2 = "London,UK"
        self.EndLocation2 = "Paris,France"
        self.TimeToWorkSlot1 = QLabel(
            TimeTo(self.StartLocation1, self.EndLocation1))
        self.TimeToWorkSlot2 = QLabel(
            TimeTo(self.StartLocation2, self.EndLocation2))
        self.LocalWeather = QLabel(conditions())
        self.LocalTemp = QLabel(temperature())

        timer = QTimer(self)
        timer.timeout.connect(self.timing)
        timer.start(1000)

        weatherTimer = QTimer(self)
        weatherTimer.timeout.connect(self.updateWeather)
        weatherTimer.start(18000000)

        self.timing()
        self.updateWeather()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.showTime)
        self.layout.addWidget(self.TimeToWorkSlot1)
        self.layout.addWidget(self.TimeToWorkSlot2)
        self.layout.addWidget(self.LocalTemp)
        self.layout.addWidget(self.LocalWeather)
        self.setLayout(self.layout)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle("CMD CNTR")
        self.show()

    def style_from_file(self, path):
        self.setObjectName("MainWidget")
        with open(path, 'r') as f:
            content = f.read()
        return content

    def timing(self):
        """ Updates any labels which relate to time """
        time = QTime.currentTime().toString('hh:mm:ss')
        self.showTime.setText(time)
        self.TimeToWorkSlot1.setText(
            TimeTo(self.StartLocation1, self.EndLocation1))
        self.TimeToWorkSlot2.setText(
            TimeTo(self.StartLocation2, self.EndLocation2))

    def updateWeather(self):
        """ Updates any labels which relate to weather """
        self.LocalWeather.setText(conditions())
        self.LocalTemp.setText(temperature())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
