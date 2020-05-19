# -*-coding:utf-8-*-

import sys
from myUI import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import cv2


class m_MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.timerCamera0 = QtCore.QTimer()
		self.cap0 = cv2.VideoCapture()
		self.cam0Addr=0
		self.camera0State=0

		self.slotInit()
		
	def slotInit(self):
		self.timerCamera0.timeout.connect(self.showCamera0)

	def showCameraButtonClicked(self):
		if self.timerCamera0.isActive() == False:
			flag = self.cap0.open(self.cam0Addr)
			if flag == False:
				QtWidgets.QMessageBox.warning(self, "Warning", "请检测相机与电脑是否连接正确")
			else:
				self.timerCamera0.start(30) # ms,about 30fps
				self.ui.buttonSwitchCamera.setText('停止')
		else:
			self.timerCamera0.stop()
			self.cap0.release()
			self.ui.labelCamera0.clear()
			self.ui.buttonSwitchCamera.setText('开始')
		
	def showCamera0(self):
		flag, image = self.cap0.read()
		self.showCV2CapRawImage(self.ui.labelCamera0,image)


	def showCV2CapRawImage(self,label,rawImage):
		_,_,w,h=label.geometry().getRect() # geometry() return QRect
		img = cv2.resize(rawImage, (w, h))
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		Qimg = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
		label.setPixmap(QtGui.QPixmap.fromImage(Qimg))

app=QApplication(sys.argv)
main_window = m_MainWindow()
main_window.show()
sys.exit(app.exec_())