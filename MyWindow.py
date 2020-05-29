# -*-coding:utf-8-*-

import sys
from myUI import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
import cv2
import time,threading
from run_demo import *


class m_MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.timerVideo0 = QtCore.QTimer()
		self.cap0 = cv2.VideoCapture()
		self.video0Addr=0

		self.slotInit()
		
	def slotInit(self):
		self.timerVideo0.timeout.connect(self.showVideo0)

	def showVideoButtonClicked(self):
		if self.timerVideo0.isActive() == False:
			flag = self.cap0.open(self.video0Addr)
			if flag == False:
				QtWidgets.QMessageBox.warning(self, "Warning", "请检测相机与电脑是否连接正确")
			else:
				self.timerVideo0.start(30) # ms,about 30fps
				self.ui.buttonStart.setText('停止')
				self.ui.labelOutput.setText('正在等待运行结果...')
				self.runModelThread=threading.Thread(target=self.runModel,name='runModelThread')
				self.runModelThread.start()
				self.threadRunning=True
		else:	# 停止按钮按下
			self.timerVideo0.stop()
			self.cap0.release()
			self.ui.labelVideo0.clear()
			self.ui.labelFilePath.setText('尚未选择文件')
			self.ui.buttonStart.setText('开始')
			self.ui.labelOutput.setText('')
			#if self.threadRunning:
				#self.runModelThread.terminate()
			delete_frames()

	def chooseFileButtonClicked(self):
		self.video0Addr,_=QFileDialog.getOpenFileName(self,'选择文件')
		self.ui.labelFilePath.setText(self.video0Addr)
		
	def showVideo0(self):
		flag, frame = self.cap0.read()
		if flag:
			self.showCV2CapRawImage(self.ui.labelVideo0, frame)
		else:	# read over
			self.cap0.open(self.video0Addr)


	def showCV2CapRawImage(self,label,rawImage):
		_,_,w,h=label.geometry().getRect() # geometry() return QRect
		img = cv2.resize(rawImage, (w, h))
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		Qimg = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
		label.setPixmap(QtGui.QPixmap.fromImage(Qimg))

	def runModel(self):
		delete_frames()
		modelOutput=run(self.video0Addr)
		print('model run over!')
		self.ui.labelOutput.setText(modelOutput)
		self.threadRunning=False
		delete_frames()

app=QApplication(sys.argv)
main_window = m_MainWindow()
main_window.show()
sys.exit(app.exec_())