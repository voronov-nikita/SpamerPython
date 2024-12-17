# 
# 
# 
# 

from PyQt5.QtWidgets import QDialog, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon

class SuccessfulCompletion(QDialog):
    def __init__(self):
        super().__init__()
        self.window_name = "Сообщение"
        self.window_size = (350, 150)
        self.window_icon = "logo.ico"

        self.InitInterface()
        self.InitText()

    def InitInterface(self):
        self._center()
        
        self.setWindowIcon(QIcon(self.window_icon))
        self.setWindowTitle("Внимание")

    
    def InitText(self):
        self.label = QLabel(self)
        self.label.resize(self.width(), self.height())
        self.label.setText("  \tУспешно Завершено!")
        self.label.setStyleSheet("""
            background: rgb(25, 25, 25);
            color: rgb(203, 203, 65);
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