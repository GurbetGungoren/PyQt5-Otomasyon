# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ara.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblara = QtWidgets.QLabel(self.centralwidget)
        self.lblara.setGeometry(QtCore.QRect(180, 70, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblara.setFont(font)
        self.lblara.setObjectName("lblara")
        self.btn_ara = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ara.setGeometry(QtCore.QRect(180, 180, 101, 31))
        self.btn_ara.setObjectName("btn_ara")
        self.text_line = QtWidgets.QLineEdit(self.centralwidget)
        self.text_line.setGeometry(QtCore.QRect(150, 129, 151, 31))
        self.text_line.setObjectName("text_line")
        self.lbl_goster = QtWidgets.QLabel(self.centralwidget)
        self.lbl_goster.setGeometry(QtCore.QRect(90, 260, 221, 51))
        self.lbl_goster.setText("")
        self.lbl_goster.setObjectName("lbl_goster")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblara.setText(_translate("MainWindow", "Kayıt Arama"))
        self.btn_ara.setText(_translate("MainWindow", "Ara"))