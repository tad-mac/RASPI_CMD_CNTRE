from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Page(QWidget):
    def __init__(self, parent=None):
        super(Page, self).__init__(parent)

        self.my_label = QLabel("RASPI")
        self.showTime = QLabel("")
        timer = QTimer(self)
        timer.timeout.connect(self.timing)
        timer.start(1000)

        self.timing()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.my_label)
        self.layout.addWidget(self.showTime)
        mainLayout = QGridLayout()
        mainLayout.addLayout(self.layout, 0, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("RASPI CMD CNTR")

    def timing(self):
        time = QTime.currentTime().toString('hh:mm:ss')
        self.showTime.setText(time)


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)

    window = Page()
    window.show()

    sys.exit(app.exec_())
