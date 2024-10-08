# Form implementation generated from reading ui file '.\uidesign_01.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import serial
import serial.tools.list_ports
import time
from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt6.QtSerialPort import *
from PyQt6.QtCore import *

# Define opcodes
_opcode_testserial          =   'op_sertest'
_opcode_testserial_verify   =   'op_sertest_verify'

_opcode_testi2c			    =   'op_i2ctest'
_opcode_testi2c_verify      =   'op_i2ctest_verify'
_opcode_testpwm_start		=   'op_pwmteststart'
_opcode_testpwm_stop		=   'op_pwmteststop'
_opcode_testpwm_verify		=   'op_pwmtest_verify'
_opcode_testio		        =   'op_iotest'
_opcode_testio_verify		=   'op_iotest_verify'

class Ui_MainWindow(object):

    bConnectionStatus = False
    serialSendSignal = QtCore.pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.comport = QSerialPort()
        self.bConnectionStatus = False
        self.bIsPWMEnabled = False
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        
        ## PAGES
        self.tbxPages = QtWidgets.QToolBox(parent=self.centralwidget)
        self.tbxPages.setGeometry(QtCore.QRect(0, 0, 800, 580))
        self.tbxPages.setObjectName("tbxPages")
        
        ## FIRST PAGE
        self.pgPhase1 = QtWidgets.QWidget()
        self.pgPhase1.setGeometry(QtCore.QRect(0, 0, 800, 465))
        self.pgPhase1.setObjectName("pgPhase1")
        
        self.label = QtWidgets.QLabel(parent=self.pgPhase1)
        self.label.setGeometry(QtCore.QRect(17, 5, 91, 30))
        self.label.setObjectName("label")
        
        self.cmbComportName = QtWidgets.QComboBox(parent=self.pgPhase1)
        self.cmbComportName.setGeometry(QtCore.QRect(130, 5, 101, 30))
        self.cmbComportName.setObjectName("cmbComport")
        
        self.btnRefComName = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnRefComName.setGeometry(QtCore.QRect(246, 5, 75, 30))
        self.btnRefComName.setObjectName("btnRefComName")
        
        self.btnConnect = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnConnect.setGeometry(QtCore.QRect(334, 5, 101, 30))
        self.btnConnect.setObjectName("btnConnect")
                
        self.lblConnectionStatus = QtWidgets.QLabel(parent=self.pgPhase1)
        self.lblConnectionStatus.setGeometry(QtCore.QRect(460, 5, 131, 30))
        self.lblConnectionStatus.setObjectName("lblConnectionStatus")
        
        self.label_comtest = QtWidgets.QLabel(parent=self.pgPhase1)
        self.label_comtest.setGeometry(QtCore.QRect(30, 50, 91, 30))
        self.label_comtest.setObjectName("label_comtest")

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
        self.rbConPass.setObjectName("rbConPass")
        
        self.rbConFailed = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbConFailed.setEnabled(False)
        self.rbConFailed.setGeometry(QtCore.QRect(560, 50, 82, 30))
        self.rbConFailed.setObjectName("rbConFailed")

        self.label_iictest = QtWidgets.QLabel(parent=self.pgPhase1)
        self.label_iictest.setGeometry(QtCore.QRect(30, 95, 150, 30))
        self.label_iictest.setObjectName("label_iictest")

        self.btnCheckIIC = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnCheckIIC.setGeometry(QtCore.QRect(180, 95, 141, 30))
        self.btnCheckIIC.setObjectName("btnCheckIIC")    
        
        self.rbIICNotest = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbIICNotest.setEnabled(False)
        self.rbIICNotest.setGeometry(QtCore.QRect(360, 95, 82, 30))
        self.rbIICNotest.setChecked(True)
        self.rbIICNotest.setObjectName("rbIICNotest")
        
        self.rbIICPass = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbIICPass.setEnabled(False)
        self.rbIICPass.setGeometry(QtCore.QRect(460, 95, 82, 30))
        self.rbIICPass.setObjectName("rbIICPass")
        
        self.rbIICFailed = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbIICFailed.setEnabled(False)
        self.rbIICFailed.setGeometry(QtCore.QRect(560, 95, 82, 30))
        self.rbIICFailed.setObjectName("rbIICFailed")

        self.lblpwm = QtWidgets.QLabel(parent=self.pgPhase1)
        self.lblpwm.setGeometry(QtCore.QRect(30, 140, 91, 30))
        self.lblpwm.setObjectName("lblpwm")

        self.btnCheckPWM = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnCheckPWM.setGeometry(QtCore.QRect(180, 140, 141, 30))
        self.btnCheckPWM.setObjectName("btnCheckPWM")
        
        self.rbPWMNotest = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbPWMNotest.setEnabled(False)
        self.rbPWMNotest.setGeometry(QtCore.QRect(360, 140, 82, 30))
        self.rbPWMNotest.setChecked(False)
        self.rbPWMNotest.setObjectName("rbPWMNotest")
        
        self.rbPWMFailed = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbPWMFailed.setEnabled(False)
        self.rbPWMFailed.setGeometry(QtCore.QRect(560, 140, 82, 30))
        self.rbPWMFailed.setObjectName("rbPWMFailed")
        
        self.rbPWMPass = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbPWMPass.setEnabled(False)
        self.rbPWMPass.setGeometry(QtCore.QRect(460, 140, 82, 30))
        self.rbPWMPass.setStyleSheet("")
        self.rbPWMPass.setObjectName("rbPWMPass")
        
        self.trPWMSpec = QtWidgets.QTreeWidget(parent=self.pgPhase1)
        self.trPWMSpec.setGeometry(QtCore.QRect(210, 185, 321, 80))
        self.trPWMSpec.setColumnCount(3)
        self.trPWMSpec.setObjectName("trPWMSpec")
        self.trPWMSpec.headerItem().setTextAlignment(0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trPWMSpec.headerItem().setTextAlignment(1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trPWMSpec.headerItem().setTextAlignment(2, QtCore.Qt.AlignmentFlag.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.trPWMSpec)
        item_0 = QtWidgets.QTreeWidgetItem(self.trPWMSpec)
        item_0 = QtWidgets.QTreeWidgetItem(self.trPWMSpec)

        self.label_IOtest = QtWidgets.QLabel(parent=self.pgPhase1)
        self.label_IOtest.setGeometry(QtCore.QRect(30, 280, 150, 30))
        self.label_IOtest.setObjectName("label_IOtest")

        self.btnCheckIO = QtWidgets.QPushButton(parent=self.pgPhase1)
        self.btnCheckIO.setGeometry(QtCore.QRect(180, 280, 141, 30))
        self.btnCheckIO.setObjectName("btnCheckIO")    
        
        self.rbIONotest = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbIONotest.setEnabled(False)
        self.rbIONotest.setGeometry(QtCore.QRect(360, 280, 82, 30))
        self.rbIONotest.setChecked(True)
        self.rbIONotest.setObjectName("rbIONotest")
        
        self.rbIOPass = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbIOPass.setEnabled(False)
        self.rbIOPass.setGeometry(QtCore.QRect(460, 280, 82, 30))
        self.rbIOPass.setObjectName("rbIOPass")
        
        self.rbIOFailed = QtWidgets.QRadioButton(parent=self.pgPhase1)
        self.rbIOFailed.setEnabled(False)
        self.rbIOFailed.setGeometry(QtCore.QRect(560, 280, 82, 30))
        self.rbIOFailed.setObjectName("rbIOFailed")
            
            #RAISE COMPONENTS#
        self.label.raise_()
        self.cmbComportName.raise_()
        self.btnConnect.raise_()
        self.label_comtest.raise_()
        self.lblConnectionStatus.raise_()
        self.btnCheckConnection.raise_()
        self.rbConPass.raise_()
        self.rbConFailed.raise_()
        self.rbConNotest.raise_()
        self.label_iictest.raise_()
        self.btnCheckIIC.raise_()
        self.rbIICPass.raise_()
        self.rbIICFailed.raise_()
        self.rbIICNotest.raise_()
        self.tbxPages.addItem(self.pgPhase1, "")
        self.lblpwm.raise_()
        self.btnCheckPWM.raise_()
        self.rbPWMFailed.raise_()
        self.rbPWMNotest.raise_()
        self.rbPWMPass.raise_()
        self.trPWMSpec.raise_()
        self.btnCheckIO.raise_()
        self.rbIOPass.raise_()
        self.rbIOFailed.raise_()
        self.rbIONotest.raise_()

        ## SECOND PAGE
        self.pgPhase2 = QtWidgets.QWidget()
        self.pgPhase2.setGeometry(QtCore.QRect(0, 0, 800, 465))
        self.pgPhase2.setObjectName("pgPhase2")
        self.tbxPages.addItem(self.pgPhase2, "")
        
        ## THIRD PAGE
        self.pgPhase3 = QtWidgets.QWidget()
        self.pgPhase3.setObjectName("pgPhase3")
        self.tbxPages.addItem(self.pgPhase3, "")
        
        ## FOURTH PAGE
        self.pgPhase4 = QtWidgets.QWidget()
        self.pgPhase4.setObjectName("pgPhase4")
        self.tbxPages.addItem(self.pgPhase4, "")
        
        ## FIFTH PAGE
        self.pgPhase5 = QtWidgets.QWidget()
        self.pgPhase5.setObjectName("pgPhase5")
        self.tbxPages.addItem(self.pgPhase5, "")
        
        ## MENU BAR
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        
        ## STATUS BAR
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #ACTIONS
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
        self.initiaLizeComponents(MainWindow)

        ## SIGNAL CONNECT
        self.btnConnect.clicked.connect(self.portOpen)
        self.btnCheckConnection.clicked.connect(self.TestConnectionPressed)
        self.btnCheckIIC.clicked.connect(self.TestIICPressed)
        self.btnRefComName.clicked.connect(self.RefreshComportName)
        self.comport.readyRead.connect(self.readFromPort)
        self.btnCheckPWM.clicked.connect(self.TestPWMPressed)
        self.btnCheckIO.clicked.connect(self.TestIOPressed)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "H4V4QCS ELECTRONIC DEPARTMENT © FATAH CO"))
        self.label.setText(_translate("MainWindow", "Select COM Port"))
        self.btnRefComName.setText(_translate("MainWindow", "Refresh"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.label_comtest.setText(_translate("MainWindow", "Test Connection"))
        self.lblConnectionStatus.setText(_translate("MainWindow", "Disconnected"))
        self.btnCheckConnection.setText(_translate("MainWindow", "Test Connection"))
        self.rbConNotest.setText(_translate("MainWindow", "Not Tested"))
        self.rbConPass.setText(_translate("MainWindow", "Passed"))
        self.rbConFailed.setText(_translate("MainWindow", "Failed"))
        self.label_iictest.setText(_translate("MainWindow", "Test I2C Connection"))
        self.btnCheckIIC.setText(_translate("MainWindow", "Test I2C"))
        self.rbIICNotest.setText(_translate("MainWindow", "Not Tested"))
        self.rbIICPass.setText(_translate("MainWindow", "Passed"))
        self.rbIICFailed.setText(_translate("MainWindow", "Failed"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase1), _translate("MainWindow", "Phase I"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase2), _translate("MainWindow", "Phase II"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase3), _translate("MainWindow", "Phase III"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase4), _translate("MainWindow", "Phase IV"))
        self.tbxPages.setItemText(self.tbxPages.indexOf(self.pgPhase5), _translate("MainWindow", "Phase V"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.lblpwm.setText(_translate("MainWindow", "Generate PWM"))
        self.btnCheckPWM.setText(_translate("MainWindow", "Start Generate PWM"))
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
        self.label_IOtest.setText(_translate("MainWindow", "Test IO Ports"))
        self.btnCheckIO.setText(_translate("MainWindow", "Test IO"))
        self.rbIONotest.setText(_translate("MainWindow", "Not Tested"))
        self.rbIOPass.setText(_translate("MainWindow", "Passed"))
        self.rbIOFailed.setText(_translate("MainWindow", "Failed"))

    def initiaLizeComponents(self,MainWindow):
        self.RefreshComportName(MainWindow)

    def portOpen(self, MainWindow):
        if self.bConnectionStatus == False:
            self.comport.setBaudRate( 9600 )
            self.comport.setPortName( self.cmbComportName.currentText() )
            self.comport.setDataBits( QSerialPort.DataBits.Data8 )
            self.comport.setParity( QSerialPort.Parity.NoParity )
            self.comport.setStopBits( QSerialPort.StopBits.OneStop )
            self.comport.setFlowControl( QSerialPort.FlowControl.NoFlowControl )
            r = self.comport.open(QIODeviceBase.OpenModeFlag.ReadWrite)
            if not r:
                self.lblConnectionStatus.setText('Port open error')
                self.lblConnectionStatus.setStyleSheet("color : red")
                self.bConnectionStatus = False
            else:
                self.lblConnectionStatus.setText('Port opened')
                self.lblConnectionStatus.setStyleSheet("color : green")
                self.bConnectionStatus = True
                self.btnConnect.setText('Disconnect')
        else:
            self.comport.close() 
            self.lblConnectionStatus.setText('Port closed')
            self.lblConnectionStatus.setStyleSheet("color : gray")
            self.bConnectionStatus = False
            self.btnConnect.setText('Connect')

    def TestConnectionPressed(self, MainWindow):
        request = _opcode_testserial
        self.sendFromPort(request)
        self.btnCheckConnection.setEnabled(False)

    def TestIICPressed(self, MainWindow):
        request = _opcode_testi2c
        self.sendFromPort(request)
        self.btnCheckIIC.setEnabled(False)

    def TestPWMPressed(self, MainWindow):
        if self.bIsPWMEnabled == False :
            request = _opcode_testpwm_start
            self.btnCheckPWM.setText('Stop Generate PWM')
            self.bIsPWMEnabled = True
        else :
            request = _opcode_testpwm_stop
            self.btnCheckPWM.setText('Start Generate PWM')
            self.bIsPWMEnabled = False
        self.sendFromPort(request)
        self.btnCheckPWM.setEnabled(False)
    
    def TestIOPressed(self, MainWindow):
        request = _opcode_testio
        self.sendFromPort(request)
        self.btnCheckIO.setEnabled(False)

    def sendFromPort(self, text):
        self.comport.write( text.encode() )
    
    def readFromPort(self):
        data = self.comport.readAll()
        if len(data) > 0:
            strRxData = (str(data, 'utf-8').rstrip('\x00') )
            if strRxData == _opcode_testserial_verify :
                self.rbConPass.setChecked(True)
                self.rbConPass.setStyleSheet("color : green")
                self.rbConFailed.setStyleSheet("color : gray")
                self.btnCheckConnection.setEnabled(True)
            
            if strRxData == _opcode_testi2c_verify :
                self.rbIICPass.setChecked(True)
                self.rbIICPass.setStyleSheet("color : green")
                self.rbIICFailed.setStyleSheet("color : gray")
                self.btnCheckIIC.setEnabled(True)
            
            if strRxData == _opcode_testpwm_verify :
                self.rbPWMPass.setChecked(True)
                self.rbPWMPass.setStyleSheet("color : green")
                self.rbPWMFailed.setStyleSheet("color : gray")
                self.btnCheckPWM.setEnabled(True)

            if strRxData == _opcode_testio_verify :
                self.rbIOPass.setChecked(True)
                self.rbIOPass.setStyleSheet("color : green")
                self.rbIOFailed.setStyleSheet("color : gray")
                self.btnCheckIO.setEnabled(True)

    def RefreshComportName(self, MainWindow):
        self.cmbComportName.clear()
        self.cmbComportName.addItems([ port.portName() for port in QSerialPortInfo().availablePorts() ])
        self.cmbComportName.setCurrentIndex(self.cmbComportName.count()-1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Create splashscreen
    splash_pix = QtGui.QPixmap('splash.jpg')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowType.WindowStaysOnTopHint)
    # add fade to splashscreen 
    opaqueness = 0.0
    step = 0.1
    splash.setWindowOpacity(opaqueness)
    splash.show()
    while opaqueness < 1:
        splash.setWindowOpacity(opaqueness)
        time.sleep(step) # Gradually appears
        opaqueness+=step
    time.sleep(1) # hold image on screen for a while
    splash.close() # close the splash screen
    #EO Splash Screen
    MainWindow.show()
    sys.exit(app.exec())
