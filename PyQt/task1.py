from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QSpinBox
from PyQt6.QtWidgets import QMainWindow, QFormLayout, QGridLayout
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar, QLabel
from PyQt6.QtGui import QIcon, QAction

class Task1Window(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.createFormTask1()
