import sys 
from PyQt5 import QtWidgets
from entry1 import Ui_MainWindow
from PyQt5.QtWidgets import *
from animal import Animals 

class Window (QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
    
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSave.clicked.connect(self.addAnimals)

        
    def addAnimals(self):
        name1 =self.ui.lineName.text() 
        problem1= self.ui.lineProblem.text()
        age1 =self.ui.lineAge.text()
        gender1= self.ui.lineGender.text()
        #cmbclass1 = self.ui.cmbClass.currentText()
        
        newAnimal=Animals(name1,age1,gender1,problem1)
        newAnimal.addAnimals(newAnimal)

  
def app():
    app=QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()
# Uygulama =QApplication(sys.argv)
# win = QMainWindow()
# ui =Ui_MainWindow()
# ui.setupUi(win)
# win.show()
# sys.exit(Uygulama.exec_())
