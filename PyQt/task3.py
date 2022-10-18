
from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QSpinBox
from PyQt6.QtWidgets import QMainWindow, QFormLayout, QGridLayout
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar, QLabel
from PyQt6.QtGui import QIcon, QAction

class Task3Window(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.createFormTask3()
        
    def createFormTask3(self):
            layout = QGridLayout(self)
            
            Label_text_1 = QLabel(self)
            Label_text_1.setText("Pole A")
            text_1 = QLineEdit(self)
            text_1.resize(250, 40)
            
            Label_number_1 = QLabel(self)
            Label_number_1.setText("Pole B")
            number_1 = QSpinBox()
            layout.addWidget(Label_text_1, 0,1)
            layout.addWidget(Label_number_1, 1,1)
            layout.addWidget(text_1, 0,2)
            layout.addWidget(number_1, 1,2)