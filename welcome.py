# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from payment import Ui_MainWindow3

class Ui_MainWindow(object):
    def __init__(self,username):
        self.username=username
        print(self.username)

    def loadData(self):
        usr=self.username
        print(usr)
        connection = sqlite3.connect("login.db")
        #query = ("SELECT * FROM USERS2 WHERE EMAIL=(?)",(username))
        connection.execute("SELECT * FROM USERS2 WHERE USERNAME=(?)",(usr))
        
        #self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            #self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.commit()
        connection.close()

    def paymentwindowshow(self):

        self.payment = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.payment)
        self.payment.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 71, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 101, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 470, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.paymentwindowshow)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230, 461, 51))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 320, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.loadData)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WELCOME"))
        self.label_2.setText(_translate("MainWindow", "Personal Details :"))
        self.pushButton.setText(_translate("MainWindow", "Click Here to Pay"))
        self.pushButton_2.setText(_translate("MainWindow", "Load"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
