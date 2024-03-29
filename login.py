# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from success import SuccessDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.USERNAME = "natia3"
        self.PASSWORD = "natia123"
        Dialog.setObjectName("login")
        Dialog.resize(445, 469)
        Dialog.setStyleSheet("background-color: rgb(0, 50, 50);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 50, 91, 41))
        self.label.setStyleSheet("color:rgb(199, 199, 199); font-size:30px;\n")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 101, 31))
        self.label_2.setStyleSheet("font-size:20px; color:rgb(199, 199, 199)")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 160, 351, 41))
        self.lineEdit.setStyleSheet("border-radius:15px; font-size:20px; padding:10px;\n""color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(60, 131, 131);\n""\n""")
        self.lineEdit.setPlaceholderText("Enter username")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 101, 31))
        self.label_3.setStyleSheet("font-size:20px; color:rgb(199, 199, 199)")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 280, 351, 41))
        self.lineEdit_2.setStyleSheet("border-radius:15px; padding:10px; font-size:20px;\n""color: rgb(255, 255, 255);"
                                      "\n""background-color: rgb(60, 131, 131);\n""\n""")
        self.lineEdit_2.setPlaceholderText("Enter password")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 380, 131, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 140, 103);\n""border-radius:15px; font-size:20px;"
                                      "\n""color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(53, 210, 351, 20))
        self.label_4.setStyleSheet("font-size:17px;\n""color: rgb(255, 0, 0);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(53, 330, 351, 20))
        self.label_5.setStyleSheet("font-size:17px;\n""color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(63, 350, 351, 20))
        self.label_6.setStyleSheet("font-size:17px;\n""color: rgb(255, 0, 0);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == "" and password == "":
            self.label_6.setText("Please enter your username and password!")
        elif username == "":
            self.label_6.setText("")
            self.label_4.setText("Please enter your username!")
            if password == self.PASSWORD:
                self.label_5.setText("")
            else:
                self.label_5.setText("Entered password is incorrect!")
        elif password == "":
            self.label_6.setText("")
            self.label_5.setText("Please enter your password!")
            if username == self.USERNAME:
                self.label_4.setText("")
            else:
                self.label_4.setText("Entered username is incorrect!")
        else:
            self.label_6.setText("")
            if self.USERNAME != username:
                self.label_4.setText("Entered username is incorrect!")
                if password == self.PASSWORD:
                    self.label_5.setText("")

            if self.PASSWORD != password:
                self.label_5.setText("Entered password is incorrect!")
                if username == self.USERNAME:
                    self.label_4.setText("")

            if username == self.USERNAME and password == self.PASSWORD:
                self.label_5.setText("")
                self.label_6.setText("")
                self.label_4.setText("")
                Dialog.close()
                success = SuccessDialog()
                success.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "LOGIN"))
        self.label_2.setText(_translate("Dialog", "UserName"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
