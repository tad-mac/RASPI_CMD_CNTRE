import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Scrapper import Slot1, Slot2


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(self.style_from_file("style.qss"))
        self.init_ui()

    def init_ui(self):
        self.title = QLabel("RASPI")
        self.showTime = QLabel("")
        self.TimeToWorkSlot1 = QLabel(Slot1())
        self.TimeToWorkSlot2 = QLabel(Slot2())
        timer = QTimer(self)
        timer.timeout.connect(self.timing)
        timer.start(1000)

        self.timing()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.showTime)
        self.layout.addWidget(self.TimeToWorkSlot1)
        self.layout.addWidget(self.TimeToWorkSlot2)
        self.setLayout(self.layout)
        self.setWindowTitle("RASPI CMD CNTR")
        self.show()

    def style_from_file(self, path):
        self.setObjectName("MainWidget")
        with open(path, 'r') as f:
            content = f.read()
        return content

    def timing(self):
        time = QTime.currentTime().toString('hh:mm:ss')
        self.showTime.setText(time)
        self.TimeToWorkSlot1.setText(Slot1())
        self.TimeToWorkSlot2.setText(Slot2())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
