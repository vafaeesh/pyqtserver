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
        MainWindow.resize(800, 570)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tbxPages = QtWidgets.QToolBox(parent=self.centralwidget)
        self.tbxPages.setGeometry(QtCore.QRect(0, 0, 800, 550))
        self.tbxPages.setObjectName("tbxPages")
        self.pgPhase1 = QtWidgets.QWidget()
        self.pgPhase1.setGeometry(QtCore.QRect(0, 0, 800, 415))
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
        self.rbConNotest.setChecked(False)
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
        self.lblpwm = QtWidgets.QLabel(parent=self.pgPhase1)
        self.lblpwm.setGeometry(QtCore.QRect(80, 145, 91, 30))
        self.lblpwm.setObjectName("lblpwm")
        self.btnCheckPWM = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnCheckPWM.setGeometry(QtCore.QRect(180, 145, 141, 30))
        self.btnCheckPWM.setObjectName("btnCheckPWM")
        self.rbPWMFailed = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbPWMFailed.setEnabled(False)
        self.rbPWMFailed.setGeometry(QtCore.QRect(560, 145, 82, 30))
        self.rbPWMFailed.setObjectName("rbPWMFailed")
        self.rbPWMNotest = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbPWMNotest.setEnabled(False)
        self.rbPWMNotest.setGeometry(QtCore.QRect(360, 145, 82, 30))
        self.rbPWMNotest.setChecked(False)
        self.rbPWMNotest.setObjectName("rbPWMNotest")
        self.rbPWMPass = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbPWMPass.setEnabled(False)
        self.rbPWMPass.setGeometry(QtCore.QRect(460, 145, 82, 30))
        self.rbPWMPass.setStyleSheet("")
        self.rbPWMPass.setObjectName("rbPWMPass")
        self.trPWMSpec = QtWidgets.QTreeWidget(parent=self.pgPhase1)
        self.trPWMSpec.setGeometry(QtCore.QRect(210, 190, 321, 81))
        self.trPWMSpec.setColumnCount(3)
        self.trPWMSpec.setObjectName("trPWMSpec")
        self.trPWMSpec.headerItem().setTextAlignment(0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trPWMSpec.headerItem().setTextAlignment(1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trPWMSpec.headerItem().setTextAlignment(2, QtCore.Qt.AlignmentFlag.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.trPWMSpec)
        item_0 = QtWidgets.QTreeWidgetItem(self.trPWMSpec)
        item_0 = QtWidgets.QTreeWidgetItem(self.trPWMSpec)
        self.rbTimerNotest = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbTimerNotest.setEnabled(False)
        self.rbTimerNotest.setGeometry(QtCore.QRect(360, 300, 82, 30))
        self.rbTimerNotest.setChecked(True)
        self.rbTimerNotest.setObjectName("rbTimerNotest")
        self.rbTimerPass = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbTimerPass.setEnabled(False)
        self.rbTimerPass.setGeometry(QtCore.QRect(460, 300, 82, 30))
        self.rbTimerPass.setStyleSheet("")
        self.rbTimerPass.setObjectName("rbTimerPass")
        self.lbltimer = QtWidgets.QLabel(parent=self.pgPhase1)
        self.lbltimer.setGeometry(QtCore.QRect(80, 300, 91, 30))
        self.lbltimer.setObjectName("lbltimer")
        self.btnCheckTimer = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnCheckTimer.setGeometry(QtCore.QRect(180, 300, 141, 30))
        self.btnCheckTimer.setObjectName("btnCheckTimer")
        self.rbTimerFailed = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbTimerFailed.setEnabled(False)
        self.rbTimerFailed.setGeometry(QtCore.QRect(560, 300, 82, 30))
        self.rbTimerFailed.setObjectName("rbTimerFailed")
        self.trTimerSpec = QtWidgets.QTreeWidget(parent=self.pgPhase1)
        self.trTimerSpec.setGeometry(QtCore.QRect(210, 340, 321, 61))
        self.trTimerSpec.setColumnCount(3)
        self.trTimerSpec.setObjectName("trTimerSpec")
        self.trTimerSpec.headerItem().setTextAlignment(0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trTimerSpec.headerItem().setTextAlignment(1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trTimerSpec.headerItem().setTextAlignment(2, QtCore.Qt.AlignmentFlag.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.trTimerSpec)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(2, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(2, brush)
        item_0 = QtWidgets.QTreeWidgetItem(self.trTimerSpec)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(2, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(2, brush)
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
        self.lblpwm.raise_()
        self.btnCheckPWM.raise_()
        self.rbPWMFailed.raise_()
        self.rbPWMNotest.raise_()
        self.rbPWMPass.raise_()
        self.trPWMSpec.raise_()
        self.rbTimerNotest.raise_()
        self.rbTimerPass.raise_()
        self.lbltimer.raise_()
        self.btnCheckTimer.raise_()
        self.rbTimerFailed.raise_()
        self.trTimerSpec.raise_()
        self.tbxPages.addItem(self.pgPhase1, "")
        self.pgPhase2 = QtWidgets.QWidget()
        self.pgPhase2.setGeometry(QtCore.QRect(0, 0, 800, 415))
        self.pgPhase2.setObjectName("pgPhase2")
        self.btnCheckTimer_2 = QtWidgets.QPushButton(parent=self.pgPhase2)
        self.btnCheckTimer_2.setGeometry(QtCore.QRect(180, 10, 141, 30))
        self.btnCheckTimer_2.setObjectName("btnCheckTimer_2")
        self.rbTimerPass_2 = QtWidgets.QRadioButton(parent=self.pgPhase2)
        self.rbTimerPass_2.setEnabled(False)
        self.rbTimerPass_2.setGeometry(QtCore.QRect(460, 10, 82, 30))
        self.rbTimerPass_2.setStyleSheet("")
        self.rbTimerPass_2.setObjectName("rbTimerPass_2")
        self.rbTimerFailed_2 = QtWidgets.QRadioButton(parent=self.pgPhase2)
        self.rbTimerFailed_2.setEnabled(False)
        self.rbTimerFailed_2.setGeometry(QtCore.QRect(560, 10, 82, 30))
        self.rbTimerFailed_2.setObjectName("rbTimerFailed_2")
        self.lbltimer_2 = QtWidgets.QLabel(parent=self.pgPhase2)
        self.lbltimer_2.setGeometry(QtCore.QRect(80, 10, 91, 30))
        self.lbltimer_2.setObjectName("lbltimer_2")
        self.rbTimerNotest_2 = QtWidgets.QRadioButton(parent=self.pgPhase2)
        self.rbTimerNotest_2.setEnabled(False)
        self.rbTimerNotest_2.setGeometry(QtCore.QRect(360, 10, 82, 30))
        self.rbTimerNotest_2.setChecked(False)
        self.rbTimerNotest_2.setObjectName("rbTimerNotest_2")
        self.rbTimerPass_3 = QtWidgets.QRadioButton(parent=self.pgPhase2)
        self.rbTimerPass_3.setEnabled(False)
        self.rbTimerPass_3.setGeometry(QtCore.QRect(460, 55, 82, 29))
        self.rbTimerPass_3.setStyleSheet("")
        self.rbTimerPass_3.setObjectName("rbTimerPass_3")
        self.lbltimer_3 = QtWidgets.QLabel(parent=self.pgPhase2)
        self.lbltimer_3.setGeometry(QtCore.QRect(80, 55, 91, 29))
        self.lbltimer_3.setObjectName("lbltimer_3")
        self.btnCheckTimer_3 = QtWidgets.QPushButton(parent=self.pgPhase2)
        self.btnCheckTimer_3.setGeometry(QtCore.QRect(180, 55, 141, 29))
        self.btnCheckTimer_3.setObjectName("btnCheckTimer_3")
        self.rbTimerFailed_3 = QtWidgets.QRadioButton(parent=self.pgPhase2)
        self.rbTimerFailed_3.setEnabled(False)
        self.rbTimerFailed_3.setGeometry(QtCore.QRect(560, 55, 82, 29))
        self.rbTimerFailed_3.setObjectName("rbTimerFailed_3")
        self.trTimerSpec_3 = QtWidgets.QTreeWidget(parent=self.pgPhase2)
        self.trTimerSpec_3.setGeometry(QtCore.QRect(210, 95, 321, 60))
        self.trTimerSpec_3.setColumnCount(3)
        self.trTimerSpec_3.setObjectName("trTimerSpec_3")
        self.trTimerSpec_3.headerItem().setTextAlignment(0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trTimerSpec_3.headerItem().setTextAlignment(1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trTimerSpec_3.headerItem().setTextAlignment(2, QtCore.Qt.AlignmentFlag.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.trTimerSpec_3)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(2, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(2, brush)
        item_0 = QtWidgets.QTreeWidgetItem(self.trTimerSpec_3)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setBackground(2, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_0.setForeground(2, brush)
        self.rbTimerNotest_3 = QtWidgets.QRadioButton(parent=self.pgPhase2)
        self.rbTimerNotest_3.setEnabled(False)
        self.rbTimerNotest_3.setGeometry(QtCore.QRect(360, 55, 82, 29))
        self.rbTimerNotest_3.setChecked(True)
        self.rbTimerNotest_3.setObjectName("rbTimerNotest_3")
        self.tbxPages.addItem(self.pgPhase2, "")
        self.pgPhase3 = QtWidgets.QWidget()
        self.pgPhase3.setGeometry(QtCore.QRect(0, 0, 800, 415))
        self.pgPhase3.setObjectName("pgPhase3")
        self.tbxPages.addItem(self.pgPhase3, "")
        self.pgPhase4 = QtWidgets.QWidget()
        self.pgPhase4.setGeometry(QtCore.QRect(0, 0, 800, 415))
        self.pgPhase4.setObjectName("pgPhase4")
        self.tbxPages.addItem(self.pgPhase4, "")
        self.pgPhase5 = QtWidgets.QWidget()
        self.pgPhase5.setGeometry(QtCore.QRect(0, 0, 800, 415))
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
        self.tbxPages.setCurrentIndex(1)
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
        self.lblpwm.setText(_translate("MainWindow", "Generate PWM"))
        self.btnCheckPWM.setText(_translate("MainWindow", "Generate PWM"))
        self.rbPWMFailed.setText(_translate("MainWindow", "Failed"))
        self.rbPWMNotest.setText(_translate("MainWindow", "Not Tested"))
        self.rbPWMPass.setText(_translate("MainWindow", "Passed"))
        self.trPWMSpec.headerItem().setText(0, _translate("MainWindow", "CHANNEL"))
        self.trPWMSpec.headerItem().setText(1, _translate("MainWindow", "FREQUENCY"))
        self.trPWMSpec.headerItem().setText(2, _translate("MainWindow", "DUTY CYCLE"))
        __sortingEnabled = self.trPWMSpec.isSortingEnabled()
        self.trPWMSpec.setSortingEnabled(False)
        self.trPWMSpec.topLevelItem(0).setText(0, _translate("MainWindow", "1"))
        self.trPWMSpec.topLevelItem(0).setText(1, _translate("MainWindow", "50 HZ"))
        self.trPWMSpec.topLevelItem(0).setText(2, _translate("MainWindow", "50%"))
        self.trPWMSpec.topLevelItem(1).setText(0, _translate("MainWindow", "2"))
        self.trPWMSpec.topLevelItem(1).setText(1, _translate("MainWindow", "50 HZ"))
        self.trPWMSpec.topLevelItem(1).setText(2, _translate("MainWindow", "25%"))
        self.trPWMSpec.topLevelItem(2).setText(0, _translate("MainWindow", "3"))
        self.trPWMSpec.topLevelItem(2).setText(1, _translate("MainWindow", "50 HZ"))
        self.trPWMSpec.topLevelItem(2).setText(2, _translate("MainWindow", "75%"))
        self.trPWMSpec.setSortingEnabled(__sortingEnabled)
        self.rbTimerNotest.setText(_translate("MainWindow", "Not Tested"))
        self.rbTimerPass.setText(_translate("MainWindow", "Passed"))
        self.lbltimer.setText(_translate("MainWindow", "Timers Check"))
        self.btnCheckTimer.setText(_translate("MainWindow", "Start Check Timers"))
        self.rbTimerFailed.setText(_translate("MainWindow", "Failed"))
        self.trTimerSpec.headerItem().setText(0, _translate("MainWindow", "CHANNEL"))
        self.trTimerSpec.headerItem().setText(1, _translate("MainWindow", "FREQUENCY"))
        self.trTimerSpec.headerItem().setText(2, _translate("MainWindow", "DUTY CYCLE"))
        __sortingEnabled = self.trTimerSpec.isSortingEnabled()
        self.trTimerSpec.setSortingEnabled(False)
        self.trTimerSpec.topLevelItem(0).setText(0, _translate("MainWindow", "1"))
        self.trTimerSpec.topLevelItem(1).setText(0, _translate("MainWindow", "2"))
        self.trTimerSpec.setSortingEnabled(__sortingEnabled)
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase1), _translate("MainWindow", "Phase I"))
        self.btnCheckTimer_2.setText(_translate("MainWindow", "Start CAN Check"))
        self.rbTimerPass_2.setText(_translate("MainWindow", "Passed"))
        self.rbTimerFailed_2.setText(_translate("MainWindow", "Failed"))
        self.lbltimer_2.setText(_translate("MainWindow", "CAN Test"))
        self.rbTimerNotest_2.setText(_translate("MainWindow", "Not Tested"))
        self.rbTimerPass_3.setText(_translate("MainWindow", "Passed"))
        self.lbltimer_3.setText(_translate("MainWindow", "Voltage Read"))
        self.btnCheckTimer_3.setText(_translate("MainWindow", "Start Reading Voltages"))
        self.rbTimerFailed_3.setText(_translate("MainWindow", "Failed"))
        self.trTimerSpec_3.headerItem().setText(0, _translate("MainWindow", "Nominal Voltage"))
        self.trTimerSpec_3.headerItem().setText(1, _translate("MainWindow", "Read Voltage"))
        self.trTimerSpec_3.headerItem().setText(2, _translate("MainWindow", "Status"))
        __sortingEnabled = self.trTimerSpec_3.isSortingEnabled()
        self.trTimerSpec_3.setSortingEnabled(False)
        self.trTimerSpec_3.topLevelItem(0).setText(0, _translate("MainWindow", "1"))
        self.trTimerSpec_3.topLevelItem(1).setText(0, _translate("MainWindow", "2"))
        self.trTimerSpec_3.setSortingEnabled(__sortingEnabled)
        self.rbTimerNotest_3.setText(_translate("MainWindow", "Not Tested"))
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
