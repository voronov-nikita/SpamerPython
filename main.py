import pyautogui
import time
import keyboard
import sys

from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QPushButton, QLabel, QAction, QShortcut
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QRect


version = "1.0.0"
class ActionDo():
    def reset(self):
        print("Reset")

    def settings(self):
        print("Settings")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"Spamer {version}")
        x, y = pyautogui.size()
        self.setGeometry(QRect(x//2, y//2, 350, 280))
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon("logo.png"))

        self.initUI()
        self.initAction()

    def initUI(self):
        self.label = QLabel(self)
        self.label.resize(350, 50)
        self.label.move(50, 0)
        self.label.setText("Введите необходимы значения")

        self.line_message = QLineEdit(self)
        self.line_message.move(0, 50)
        self.line_message.resize(350, 50)
        self.line_message.setPlaceholderText("Message for spam")

        self.line_count = QLineEdit(self)
        self.line_count.move(0, 100)
        self.line_count.resize(350, 50)
        self.line_count.setPlaceholderText("Number of spam messages")

        self.line_timer = QLineEdit(self)
        self.line_timer.move(0, 150)
        self.line_timer.resize(350, 50)
        self.line_timer.setPlaceholderText("Delay before spam")

        self.button = QPushButton(self)
        self.button.move(0, 175+20)
        self.button.resize(350, 100)
        self.button.clicked.connect(self.start_send_message)
        self.button.setText("START SPAM")

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

    def initAction(self):
        act = ActionDo()

        action1 = QAction("Выполнить", self)
        action1.setShortcut(QKeySequence("Ctrl+Shift+R"))
        action1.triggered.connect(act.reset)

        action2 = QAction("Выполнить", self)
        action2.setShortcut(QKeySequence("Alt+I"))
        action2.triggered.connect(act.settings)


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())
