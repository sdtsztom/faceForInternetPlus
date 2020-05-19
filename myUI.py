# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './videoChoose.ui'
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
        self.labelVideo0 = QtWidgets.QLabel(self.centralwidget)
        self.labelVideo0.setGeometry(QtCore.QRect(90, 60, 700, 500))
        self.labelVideo0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelVideo0.setText("")
        self.labelVideo0.setObjectName("labelVideo0")
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(280, 610, 89, 25))
        self.buttonStart.setObjectName("buttonStart")
        self.pushChooseVideo = QtWidgets.QPushButton(self.centralwidget)
        self.pushChooseVideo.setGeometry(QtCore.QRect(460, 610, 89, 25))
        self.pushChooseVideo.setObjectName("pushChooseVideo")
        self.labelFilePath = QtWidgets.QLabel(self.centralwidget)
        self.labelFilePath.setGeometry(QtCore.QRect(90, 570, 700, 21))
        self.labelFilePath.setObjectName("labelFilePath")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.buttonStart.clicked.connect(MainWindow.showVideoButtonClicked)
        self.pushChooseVideo.clicked.connect(MainWindow.chooseFileButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonStart.setText(_translate("MainWindow", "开始"))
        self.pushChooseVideo.setText(_translate("MainWindow", "选择视频"))
        self.labelFilePath.setText(_translate("MainWindow", "尚未选择文件"))
