import sys 
from PyQt5 import QtWidgets
from search import Ui_MainWindow
from PyQt5.QtWidgets import *
from animal import Animals

class searchWindow (QtWidgets.QMainWindow):
    def __init__(self):
        super(searchWindow, self).__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_ara.clicked.connect(self.search)

    def search(self):
        textAra = self.ui.text_line.text()
        a=Animals("","","","")
        findin=a.find(textAra)
        #print(findin)
        if findin is None:   # eğer dönen obje boş ise hayvan bulunamadı
            x='Aranılan hayvan bulunamadı'
        else:
            x = findin[0]+","+findin[1]+","+findin[2]+","+findin[3]
    
        self.ui.lbl_goster.setText(x)
                       
def app():
    app=QApplication(sys.argv)
    win = searchWindow()
    win.show()
    sys.exit(app.exec_())
app()