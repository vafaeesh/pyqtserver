# Form implementation generated from reading ui file '.\testview.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btnOk = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.btnOk.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.btnOk.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btnOk.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btnOk.setObjectName("btnOk")
        self.cmComPorts = QtWidgets.QComboBox(parent=Dialog)
        self.cmComPorts.setGeometry(QtCore.QRect(130, 20, 231, 22))
        self.cmComPorts.setObjectName("cmComPorts")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 47, 13))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.btnOk.accepted.connect(Dialog.accept) # type: ignore
        self.btnOk.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Com Ports Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
