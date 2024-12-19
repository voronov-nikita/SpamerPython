# 
# Файл основного тела приложения
# Сюда импортируются модули логики и компоненты для запуска самого приложения
# 
# 

from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon

from components.emptyPlace import MessageEmptyPlace
from components.successfulCompletion import SuccessfulCompletion

import config
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width_window = 400
        self.height_window = 450

        # this is step for inputs-lines
        self.step = self.height_window//5

        self.setWindowTitle(config.titleApp)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon(config.logo))
        self._center()
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
            
            self.line_count.clear()
            self.line_message.clear()
            self.line_timer.clear()

            ex = SuccessfulCompletion()
            ex.exec_()
            
        except ValueError:
            self.line_count.clear()
            self.line_message.clear()
            self.line_timer.clear()
            ex = MessageEmptyPlace()
            ex.exec_()
            
    def _center(self):
        '''
        Центрование окна по размеру экрана
        '''
        # Получаем размеры экрана
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())