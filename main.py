import pyautogui
import time
import keyboard
import sys

from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spamer")
        x, y = pyautogui.size()
        self.setGeometry(QRect(x//2, y//2, 350, 280))
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon("logo.png"))
        self.initUI()

    def initUI(self):
        self.line_message = QLineEdit(self)
        self.line_message.move(0, 50)
        self.line_message.resize(350, 50)
        self.line_message.setPlaceholderText("Message for spam")

        self.line_count = QLineEdit(self)
        self.line_count.move(0, 100+1)
        self.line_count.resize(350, 50)
        self.line_count.setPlaceholderText("Number of spam messages")

        self.line_timer = QLineEdit(self)
        self.line_timer.move(0, 150+1)
        self.line_timer.resize(350, 50)
        self.line_timer.setPlaceholderText("Delay before spam")

        self.button = QPushButton(self)
        self.button.move(0, 200+21)
        self.button.resize(350, 50)
        self.button.clicked.connect(self.start_send_message)
        self.button.setText("Start")

    def start_send_message(self):
        message = self.line_message.text()
        amount = int(self.line_count.text())
        time.sleep(int(self.line_timer.text()))

        while amount > 0:
            if keyboard.is_pressed("esc"):
                break
            else:
                amount -= 1
                pyautogui.typewrite(message.strip())
                pyautogui.press("enter")
        self.line_count.clear()
        self.line_message.clear()
        self.line_timer.clear()


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())
