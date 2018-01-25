import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        # self.style_from_file()
        self.init_ui()

    def init_ui(self):
        self.title = QLabel("RASPI")
        self.showTime = QLabel("")
        timer = QTimer(self)
        timer.timeout.connect(self.timing)
        timer.start(1000)

        self.timing()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.showTime)
        self.setLayout(self.layout)
        self.setWindowTitle("RASPI CMD CNTR")
        self.show()

    def style_from_file(path):
        self.setObjectName("MainWidget")
        with open(path, 'r') as f:
            content = f.read()
        return content

    def timing(self):
        time = QTime.currentTime().toString('hh:mm:ss')
        self.showTime.setText(time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
