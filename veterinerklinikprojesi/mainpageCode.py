from PyQt5.QtWidgets import *
from main_page import Ui_MainWindow 

from kayiteklemeCode import KayitEklemePage

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.t_ekleme_butonu.clicked.connect(self.openkayiteklemepage)  
        self.kayitpage=KayitEklemePage()

    def openkayiteklemepage(self):
        self.kayitpage.show()
 