import sys 
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from index import Ui_index_goruntu
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal



from search import Ui_MainWindow

#from animal import Animals 
class Window (QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui =Ui_index_goruntu()
        self.ui.setupUi(self)
        self.ui.btnentry.clicked.connect(self.openaddpage)


        
       
    def openaddpage(self):
        from main.py import Window
        self.kayıteklemesayfası = Window()
        self.kayıteklemesayfası.show()

        
        


    

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
