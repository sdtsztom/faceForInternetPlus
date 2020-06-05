# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoChoose.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1175, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelVideo0 = QtWidgets.QLabel(self.centralwidget)
        self.labelVideo0.setGeometry(QtCore.QRect(20, 60, 700, 500))
        self.labelVideo0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelVideo0.setText("")
        self.labelVideo0.setObjectName("labelVideo0")
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(210, 610, 89, 25))
        self.buttonStart.setObjectName("buttonStart")
        self.pushChooseVideo = QtWidgets.QPushButton(self.centralwidget)
        self.pushChooseVideo.setGeometry(QtCore.QRect(390, 610, 89, 25))
        self.pushChooseVideo.setObjectName("pushChooseVideo")
        self.labelFilePath = QtWidgets.QLabel(self.centralwidget)
        self.labelFilePath.setGeometry(QtCore.QRect(20, 570, 700, 21))
        self.labelFilePath.setObjectName("labelFilePath")
        self.labelOverlapPlot = QtWidgets.QLabel(self.centralwidget)
        self.labelOverlapPlot.setGeometry(QtCore.QRect(740, 250, 411, 311))
        self.labelOverlapPlot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelOverlapPlot.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOverlapPlot.setObjectName("labelOverlapPlot")
        self.radioAlg1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioAlg1.setGeometry(QtCore.QRect(740, 60, 112, 23))
        self.radioAlg1.setObjectName("radioAlg1")
        self.radioAlg2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioAlg2.setGeometry(QtCore.QRect(880, 60, 112, 23))
        self.radioAlg2.setObjectName("radioAlg2")
        self.radioAlg3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioAlg3.setGeometry(QtCore.QRect(1020, 60, 112, 23))
        self.radioAlg3.setObjectName("radioAlg3")
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
        self.labelOverlapPlot.setText(_translate("MainWindow", "重叠率效果图"))
        self.radioAlg1.setText(_translate("MainWindow", "算法1"))
        self.radioAlg2.setText(_translate("MainWindow", "算法2"))
        self.radioAlg3.setText(_translate("MainWindow", "算法3"))
