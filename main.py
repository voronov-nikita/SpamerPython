import pyautogui
import time
import keyboard
import sys

from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QPushButton
from PyQt5.QtGui import QIcon



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spamer")
        x, y = pyautogui.size()
        self.setGeometry(x//2, y//2, 350, 400)
        self.initUI()

    def initUI(self):
        self.line_message = QLineEdit(self)
        self.line_message.move(350//2, 100)

        self.line_count = QLineEdit(self)
        self.line_count.move(350//2, 200)

        self.button = QPushButton("Начать", self)
        self.move(350//2, 400)
        self.button.clicked.connect(self.start_send_message)

    def start_send_message(self):
        message = self.line_message.text()
        amount = int(self.line_count.text())
        time.sleep(6)

        while amount > 0:
            if keyboard.is_pressed("esc"):
                break
            else:
                amount -= 1

                pyautogui.typewrite(message.strip())
                pyautogui.press("enter")


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())
