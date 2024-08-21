# Form implementation generated from reading ui file '.\uidesign_01.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tbxPages = QtWidgets.QToolBox(parent=self.centralwidget)
        self.tbxPages.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.tbxPages.setObjectName("tbxPages")
        self.pgPhase1 = QtWidgets.QWidget()
        self.pgPhase1.setGeometry(QtCore.QRect(0, 0, 800, 465))
        self.pgPhase1.setObjectName("pgPhase1")
        self.label = QtWidgets.QLabel(parent=self.pgPhase1)
        self.label.setGeometry(QtCore.QRect(17, 10, 91, 20))
        self.label.setObjectName("label")
        self.cmbComport = QtWidgets.QComboBox(parent=self.pgPhase1)
        self.cmbComport.setGeometry(QtCore.QRect(130, 10, 101, 20))
        self.cmbComport.setObjectName("cmbComport")
        self.btnConnect = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnConnect.setGeometry(QtCore.QRect(334, 5, 101, 30))
        self.btnConnect.setObjectName("btnConnect")
        self.label_2 = QtWidgets.QLabel(parent=self.pgPhase1)
        self.label_2.setGeometry(QtCore.QRect(80, 55, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lblConnectionStatus = QtWidgets.QLabel(parent=self.pgPhase1)
        self.lblConnectionStatus.setGeometry(QtCore.QRect(460, 10, 131, 20))
        self.lblConnectionStatus.setObjectName("lblConnectionStatus")
        self.btnCheckConnection = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnCheckConnection.setGeometry(QtCore.QRect(180, 50, 141, 30))
        self.btnCheckConnection.setObjectName("btnCheckConnection")
        self.rbConNotest = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbConNotest.setEnabled(False)
        self.rbConNotest.setGeometry(QtCore.QRect(360, 50, 82, 30))
        self.rbConNotest.setChecked(True)
        self.rbConNotest.setObjectName("rbConNotest")
        self.rbConPass = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbConPass.setEnabled(False)
        self.rbConPass.setGeometry(QtCore.QRect(460, 50, 82, 30))
        self.rbConPass.setStyleSheet("")
        self.rbConPass.setObjectName("rbConPass")
        self.rbConFailed = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbConFailed.setEnabled(False)
        self.rbConFailed.setGeometry(QtCore.QRect(560, 50, 82, 30))
        self.rbConFailed.setObjectName("rbConFailed")
        self.btnRefComName = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnRefComName.setGeometry(QtCore.QRect(246, 5, 75, 30))
        self.btnRefComName.setObjectName("btnRefComName")
        self.label.raise_()
        self.cmbComport.raise_()
        self.btnConnect.raise_()
        self.label_2.raise_()
        self.lblConnectionStatus.raise_()
        self.btnCheckConnection.raise_()
        self.rbConPass.raise_()
        self.rbConFailed.raise_()
        self.rbConNotest.raise_()
        self.btnRefComName.raise_()
        self.tbxPages.addItem(self.pgPhase1, "")
        self.pgPhase2 = QtWidgets.QWidget()
        self.pgPhase2.setGeometry(QtCore.QRect(0, 0, 800, 465))
        self.pgPhase2.setObjectName("pgPhase2")
        self.tbxPages.addItem(self.pgPhase2, "")
        self.pgPhase3 = QtWidgets.QWidget()
        self.pgPhase3.setGeometry(QtCore.QRect(0, 0, 800, 465))
        self.pgPhase3.setObjectName("pgPhase3")
        self.tbxPages.addItem(self.pgPhase3, "")
        self.pgPhase4 = QtWidgets.QWidget()
        self.pgPhase4.setGeometry(QtCore.QRect(0, 0, 800, 465))
        self.pgPhase4.setObjectName("pgPhase4")
        self.tbxPages.addItem(self.pgPhase4, "")
        self.pgPhase5 = QtWidgets.QWidget()
        self.pgPhase5.setGeometry(QtCore.QRect(0, 0, 800, 465))
        self.pgPhase5.setObjectName("pgPhase5")
        self.tbxPages.addItem(self.pgPhase5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tbxPages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "H4V4QCS ELECTRONIC DEPARTMENT © FATAH CO"))
        self.label.setText(_translate("MainWindow", "Select COM Port"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.label_2.setText(_translate("MainWindow", "Test Connection"))
        self.lblConnectionStatus.setText(_translate("MainWindow", "Disconnected"))
        self.btnCheckConnection.setText(_translate("MainWindow", "Test Connection"))
        self.rbConNotest.setText(_translate("MainWindow", "Not Tested"))
        self.rbConPass.setText(_translate("MainWindow", "Passed"))
        self.rbConFailed.setText(_translate("MainWindow", "Failed"))
        self.btnRefComName.setText(_translate("MainWindow", "Refresh"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase1), _translate("MainWindow", "Phase I"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase2), _translate("MainWindow", "Phase II"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase3), _translate("MainWindow", "Phase III"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase4), _translate("MainWindow", "Phase IV"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase5), _translate("MainWindow", "Phase V"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
