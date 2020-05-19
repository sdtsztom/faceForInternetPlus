# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './SimpleCamera.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCamera0 = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera0.setGeometry(QtCore.QRect(90, 60, 700, 500))
        self.labelCamera0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelCamera0.setText("")
        self.labelCamera0.setObjectName("labelCamera0")
        self.buttonSwitchCamera = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSwitchCamera.setGeometry(QtCore.QRect(390, 610, 89, 25))
        self.buttonSwitchCamera.setObjectName("buttonSwitchCamera")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.buttonSwitchCamera.clicked.connect(MainWindow.showCameraButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonSwitchCamera.setText(_translate("MainWindow", "开始"))
