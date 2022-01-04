import sys 
from PyQt5 import QtWidgets
from delete import Ui_MainWindow
from PyQt5.QtWidgets import *
from animal import Animals 

class  deleteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.delete)

    def delete(self):
        delete_name=self.ui.lineEdit.text() 
        a=Animals("","","","")
        a.deleteAnimal(delete_name)
        #index bul pop la sis popla 4 kere çalıştır
        #geri kalanları yazdır tekrardan

