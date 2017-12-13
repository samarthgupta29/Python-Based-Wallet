# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def paymentreg(self):
        semail = self.lineEdit.text()
        remail = self.lineEdit_2.text()
        amt = self.lineEdit_3.text()
        amt2 = int(amt)
        connection = sqlite3.connect("login.db")
        connection.execute("INSERT INTO TRANSACTIONTABLE3 VALUES(?,?,?)", (semail, remail, amt2))
        connection.execute("UPDATE USERS2 SET BALANCE=BALANCE-(?) WHERE EMAIL=(?)", (amt2, semail))
        connection.execute("UPDATE USERS2 SET BALANCE=BALANCE+(?) WHERE EMAIL=(?)", (amt2, remail))
        connection.commit()
        connection.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 150, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 210, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.paymentreg)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 340, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 21))
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
        self.label.setText(_translate("MainWindow", "Sender\'s E-Mail"))
        self.label_2.setText(_translate("MainWindow", "Reciever\'s E-Mail"))
        self.label_3.setText(_translate("MainWindow", "Amount"))
        self.pushButton.setText(_translate("MainWindow", "Pay"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
