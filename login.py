# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from welcome import Ui_MainWindow
#from signup import Ui_Dialog2
from signup2 import Ui_SignupWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def showmessagebox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        #msgBox.setIcon(QtWidgets.QMessageBox.warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        #msgBox.setStandardButtons(QtWidgets.QMessageBox)
        msgBox.exec_()
    def signupwindowshow(self):
        self.signup=QtWidgets.QMainWindow()
        self.ui=Ui_SignupWindow()
        self.ui.setupUi(self.signup)
        self.signup.show()
    def welcomewindowshow(self,username):

        self.welcome = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(username)
        self.ui.setupUi(self.welcome)
        self.welcome.show()
    #def signUpshow(self):
     #   self.signUpWindow=QtWidgets.QDialog
      #  self.ui=Ui_Dialog2()
       # self.ui.setupUi(self.signUpWindow)
        #self.signUpWindow.show()
    def loginCheck(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()

        connection=sqlite3.connect("login.db")
        result=connection.execute("SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD=?", (username, password))
        if((len(result.fetchall()))>0):
            print("User found ")
            self.welcomewindowshow(username)
        else:
            print("User not found")
            self.showmessagebox("Warning","Invalid user and password")
    def registerCheck(self):
        print("sign up button clicked")
        self.signupwindowshow()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(777, 509)
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(270, 180, 71, 16))
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(270, 260, 71, 16))
        self.pass_label.setObjectName("pass_label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(350, 180, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 260, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")
        ###################################################
        self.pushButton.clicked.connect(self.loginCheck)
        ###################################################
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 420, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        ###################################################
        self.pushButton_2.clicked.connect(self.registerCheck)
        ###################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME"))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.pushButton_2.setText(_translate("Dialog", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

