# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 500, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):
        # creating a QDateTimeEdit widget
        datetime = QDateTimeEdit(self)

        # setting geometry left, top, width, height
        datetime.setGeometry(100, 100, 200, 35)

        datetime.setDisplayFormat("yyyy MM dd hh:mm:ss")

        now = QtCore.QDateTime.currentDateTime()

        datetime.setDateTime(now)

        # creating a label
        label = QLabel("GeeksforGeeks", self)

        # setting geometry to the label
        label.setGeometry(100, 160, 400, 60)

        # making label multi line
        label.setWordWrap(True)

        # adding action to the datetime
        datetime.dateTimeChanged.connect(lambda: dt_method())

        # method called by the datetime
        def dt_method():
            # getting current datetime
            value = datetime.dateTime()

            # setting text to the label
            label.setText("Current date time : " + str(value))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
