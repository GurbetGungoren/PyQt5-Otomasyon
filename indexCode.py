import sys 
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from index import Ui_index_goruntu
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from addanimalCode import addWindow
from updateCode import updt
from searchCode import searchWindow
from deleteCode import deleteWindow

#from animal import Animals 
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_index_goruntu()
        self.ui.setupUi(self)
        self.ui.btnentry.clicked.connect(self.openkayiteklemepage)  
        self.ui.btnupdate.clicked.connect(self.guncelelmesayfasiniac) 
        self.kayitpage=addWindow()
        self.guncellemesayfasi = updt()

        self.ui.btnSearch.clicked.connect(self.aramasayfasiac) 
        self.aramasayfasi=searchWindow()

        self.ui.btndelete.clicked.connect(self.silmesayfasiac)
        self.silmesayfasi=deleteWindow()

    def openkayiteklemepage(self):
        self.kayitpage.show()
    
    def guncelelmesayfasiniac(self):
        self.guncellemesayfasi.show()

    def aramasayfasiac(self):
        self.aramasayfasi.show()

    def silmesayfasiac(self):
        self.silmesayfasi.show()

    
    

        

app=QApplication([])
win = Window()
win.show()
app.exec_()
