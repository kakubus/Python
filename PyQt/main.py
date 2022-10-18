from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QSpinBox
from PyQt6.QtWidgets import QMainWindow, QFormLayout, QGridLayout
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import QIcon, QAction

import task3

# Tworzenie klasy głównego okna aplikacji dziedziczącej po QMainWindow

class Window(QMainWindow):
    #Dodanie konstruktora przyjmującego okno nadrzędne
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt6 Lab')
        self.setGeometry(400,400,800,400)

        
        self.createMenu()
        self.createTabs()
        
    
    # Funkcja dodająca pasek menu do okna
    def createMenu(self):
        # Stworzenie paska menu
        self.menu = self.menuBar()
        # Dodanie do paska listy rozwijalnej o nazwie File
        self.fileMenu = self.menu.addMenu("File")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.actionExit = QAction('Exit', self)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.close)
        self.fileMenu.addAction(self.actionExit)
        
        #Menu TASK1
        self.task1Menu = self.menu.addMenu("Task1")
        self.openTask1Menu = self.task1Menu.addAction("Open")
        #Menu TASK2
        self.task2Menu = self.menu.addMenu("Task2")
        self.clearTask2Menu = self.task2Menu.addAction("Clear")
        self.openTask2Menu = self.task2Menu.addAction("Open")
        self.saveTask2Menu = self.task2Menu.addAction("Save")
        self.saveAsTask2Menu = self.task2Menu.addAction("Save as")
        #Menu TASK3
        self.task3Menu = self.menu.addMenu("Task3")
        self.clearTask3Menu = self.task3Menu.addAction("Clear")

    
    # Funkcja dodająca wenętrzeny widżet do okna
    def createTabs(self):
        # Tworzenie widżetu posiadającego zakładki
        self.tabs = QTabWidget()
        
        # Stworzenie osobnych widżetów dla zakładek
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = task3.Task3Window()
        
        # Dodanie zakładek do widżetu obsługującego zakładki
        self.tabs.addTab(self.tab_1, "Pierwsza zakładka")        
        self.tabs.addTab(self.tab_2, "Druga zakładka")        
        self.tabs.addTab(self.tab_3, "Trzecia zakładka")
        
        #self.tab_1.show(createFormTask3())
        
        # Dodanie widżetu do głównego okna jako centralny widżet
        self.setCentralWidget(self.tabs)

    
        

# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec()

