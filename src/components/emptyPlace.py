# 
# 
# 
# 
# 

from PyQt5.QtWidgets import QDialog, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon


class MessageEmptyPlace(QDialog):
    def __init__(self):
        super().__init__()

        self.width_window = 350
        self.height_window = 150

        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("Внимание")
        self._center()
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
        
    def _center(self):
        '''
        Центрование окна по размеру экрана
        '''
        # Получаем размеры экрана
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())