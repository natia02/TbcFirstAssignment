from PyQt5 import QtCore, QtGui, QtWidgets

class UI_Success(object):
    def setupUi(self, SuccessDialog):
        SuccessDialog.setObjectName("SuccessDialog")
        SuccessDialog.resize(400, 400)
        SuccessDialog.setStyleSheet("background-color: rgb(0, 50, 50);")
        self.label = QtWidgets.QLabel(SuccessDialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color:rgb(199, 199, 199); font-size:20px;")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(SuccessDialog)
        QtCore.QMetaObject.connectSlotsByName(SuccessDialog)

    def retranslateUi(self, SuccessDialog):
        _translate = QtCore.QCoreApplication.translate
        SuccessDialog.setWindowTitle(_translate("SuccessDialog", "Success"))
        self.label.setText(_translate("SuccessDialog", "Congratulations! \n You logged in successfully!"))


class SuccessDialog(QtWidgets.QDialog, UI_Success):
    def __init__(self, parent=None):
        super(SuccessDialog, self).__init__(parent)
        self.setupUi(self)