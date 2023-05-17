from PyQt5 import QtCore
import pyautogui
import time
import keyboard
import sys

from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect


# version = "1.0.1"

class MesageEmptyPlace(QDialog):
    def __init__(self):
        super().__init__()

        self.width_window = 350
        self.height_window = 150

        x, y = pyautogui.size()
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("Внимание")
        self.setGeometry(QRect((x-self.width_window)//2, (y-self.height_window)//2, self.width_window, self.height_window))
        self.setFixedSize(self.width(), self.height())

        self.initText()

    def initText(self):
        self.label = QLabel(self)
        self.label.resize(self.width_window, self.height_window)
        self.label.setText("Вы ввели некоректные значения,\nПроверьте их попробуйте снова")
        self.label.setStyleSheet("""
        background: rgb(25, 25, 25);
        color: rgb(0, 120, 212);
        position: absolute;

        width: 100%;
        height: 100%;
        font-weight: bold;
        text-align: center;
        """)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width_window = 400
        self.height_window = 450

        # this is step for inputs-lines
        self.step = self.height_window//5

        self.setWindowTitle(f"SPAM")
        x, y = pyautogui.size()
        self.setGeometry(QRect((x-self.width_window)//2, (y-self.height_window)//2, self.width_window, self.height_window))
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon("logo.png"))

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.resize(self.width_window, self.step)
        self.label.setText("\tВведите необходимы значения")
        self.label.setStyleSheet("""
        background: rgb(35, 35, 35);
        color: rgb(255, 255, 255);
        position: absolute;

        width: 100%;
        height: 100%;
        font-weight: bold;
        text-align: center;
        """)

        self.line_message = QLineEdit(self)
        self.line_message.move(0, self.step*1 - 5)
        self.line_message.resize(self.width_window, self.step)
        self.line_message.setPlaceholderText("\tMessage for spam")
        self.line_message.setStyleSheet("""
        background: rgb(50, 50, 50);
        color: rgb(200, 200, 200);
        border: 0%;
        """)

        self.line_count = QLineEdit(self)
        self.line_count.move(0, self.step*2 - 5)
        self.line_count.resize(self.width_window, self.step)
        self.line_count.setPlaceholderText("\tNumber of spam messages")
        self.line_count.setStyleSheet("""
        background: rgb(50, 50, 50);
        color: rgb(200, 200, 200);
        border: 0%;
        """)

        self.line_timer = QLineEdit(self)
        self.line_timer.move(0, self.step*3 - 5)
        self.line_timer.resize(self.width_window, self.step)
        self.line_timer.setPlaceholderText("\tDelay before spam")
        self.line_timer.setStyleSheet("""
        background: rgb(50, 50, 50);
        color: rgb(200, 200, 200);
        border: 0%;
        """)

        self.button = QPushButton(self)
        # -5 px for new position of button
        self.button.move(0, self.step*4-25)
        self.button.resize(self.width_window, int(self.step*1.5))
        self.button.clicked.connect(self.start_send_message)
        self.button.setText("START SPAM")
        self.button.setStyleSheet('background: rgb(145, 5, 4);\
                                  color: rgb(255,255, 255);\
                                  font-weight: bold;\
                                  border: 0%;')

    def start_send_message(self):
        try:
            message = self.line_message.text().encode('utf-8')
            amount = int(self.line_count.text())
            time.sleep(int(self.line_timer.text()))

            while amount > 0:
                if keyboard.is_pressed("esc"):
                    break
                else:
                    amount -= 1
                    pyautogui.typewrite(message.decode('utf-8').strip())
                    pyautogui.press("enter")
            self.line_count.clear()
            self.line_message.clear()
            self.line_timer.clear()
        except ValueError:
            self.line_count.clear()
            self.line_message.clear()
            self.line_timer.clear()
            ex = MesageEmptyPlace()
            ex.exec_()
    


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())
