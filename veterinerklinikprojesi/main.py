from PyQt5.QtWidgets import QApplication
from mainpageCode import MainPage


app=QApplication([])
win = MainPage()
win.show()
app.exec_()
