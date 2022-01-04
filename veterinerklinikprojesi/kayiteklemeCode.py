from PyQt5.QtWidgets import *
from kayitekleme import Ui_Form 


class KayitEklemePage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui =Ui_Form()
        self.ui.setupUi(self)
        
 