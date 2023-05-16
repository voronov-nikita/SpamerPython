import pyautogui
import time
import keyboard
import sys

from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect, Qt


version = "1.0.1"



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"SPAM")
        x, y = pyautogui.size()
        self.setGeometry(QRect(x//2, y//2, 350, 280))
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.resize(350, 50)
        self.label.setText("Введите необходимы значения")
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
        self.line_message.move(0, 50)
        self.line_message.resize(350, 50)
        self.line_message.setPlaceholderText("Message for spam")
        self.line_message.setStyleSheet("""
        background: rgb(50, 50, 50);
        color: rgb(200, 200, 200);
        border: 0%;
        """)

        self.line_count = QLineEdit(self)
        self.line_count.move(0, 100)
        self.line_count.resize(350, 50)
        self.line_count.setPlaceholderText("Number of spam messages")
        self.line_count.setStyleSheet("""
        background: rgb(50, 50, 50);
        color: rgb(200, 200, 200);
        border: 0%;
        """)

        self.line_timer = QLineEdit(self)
        self.line_timer.move(0, 150)
        self.line_timer.resize(350, 50)
        self.line_timer.setPlaceholderText("Delay before spam")
        self.line_timer.setStyleSheet("""
        background: rgb(50, 50, 50);
        color: rgb(200, 200, 200);
        border: 0%;
        """)

        self.button = QPushButton(self)
        self.button.move(0, 175+20)
        self.button.resize(350, 100)
        self.button.clicked.connect(self.start_send_message)
        self.button.setText("START SPAM")
        self.button.setStyleSheet('background: rgb(145, 5, 4);\
                                  color: rgb(255,255, 255);\
                                  font-weight: bold;\
                                  border: 0%;')

    def start_send_message(self):
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

    


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())
