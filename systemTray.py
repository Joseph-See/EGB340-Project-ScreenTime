"""
Creating a system tray icon for the program

"""

# Import modules
import sys
import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, Qt
from balloontip import *
from multiprocessing import Process

class DisplayNotifcations(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def notification(title, message):
        balloon_tip(title, message)     

    def run(self):
        self.notification(title, message)
        

class TrayIcon(QWidget):

    def __init__(self):
        
        self.initGUI()


    def initGUI(self):
        icon = QtGui.QIcon("chair.png")

        
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)

        menu = QMenu()
        option1 = QAction("Created by Joseph See")
        option2 = QAction("Check Connection with chair")
        option3 = QAction("Quit")
        menu.addAction(option1)
        menu.addAction(option2)
        menu.addAction(option3)

        # quit = QAction("Quit")
        # quit.triggered.connect(self.quit)
        # menu.addAction(quit)

        # tray.setContextMenu(menu) 

   
        

def main():
    app = QApplication(sys.argv)    
    tray = TrayIcon()
    tray.show()
    app.exec()

    
    
    

if __name__ == '__main__':
    main() 
