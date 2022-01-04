import sys 
from PyQt5 import QtWidgets
from update import Ui_MainWindow
from PyQt5.QtWidgets import *
from animal import Animals
class updt (QtWidgets.QMainWindow):
    def __init__(self):
        super(updt, self).__init__()

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.pushButton_2.clicked.connect(self.update_search)  
        self.ui.pushButton_5.clicked.connect(self.update) 
    def update_search(self):
        a=Animals("","","","")
        s = self.ui.lineEdit_3.text()
        z = a.find(s)
        if z is None:
            print('bro boş obje')
        else:
            self.ui.lineEdit_4.setText(z[1])
            self.ui.lineEdit_5.setText(z[2])
            self.ui.lineEdit_6.setText(z[3])
            
    def update(self):
        n =self.ui.lineEdit_3.text()
        u=Animals("","","","")
        u.deleteAnimal(n)
        u.find(n)
        
        y = self.ui.lineEdit_4.text()
        c = self.ui.lineEdit_5.text()
        p =self.ui.lineEdit_6.text()
        newAnimals=Animals(n,y,c,p)  
        newAnimals.addAnimals(newAnimals)
        
        

def app():
    app=QApplication(sys.argv)
    win = updt()
    win.show()
    sys.exit(app.exec_())
app()   