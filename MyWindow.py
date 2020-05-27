# -*-coding:utf-8-*-

import sys
from myUI import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import cv2
from demoModule import Tracker


class m_MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.timerVideo0 = QtCore.QTimer()
		self.cap0 = cv2.VideoCapture()
		self.video0Addr = 0
		self.ui.labelVideo0.setMouseTracking(True)
		self.flagFirstFrame = False
		self.labelVideoRec = self.ui.labelVideo0.geometry().getRect()
		self.tracker=Tracker()

	def slotInit(self):
		self.timerVideo0.timeout.connect(self.showVideo0)

	def showVideoButtonClicked(self):
		if self.timerVideo0.isActive() == False:
			flag = self.cap0.open(self.video0Addr)
			if flag == False:
				QtWidgets.QMessageBox.warning(self, "Warning", "请检测相机与电脑是否连接正确")
			else:
				self.timerVideo0.start(30)  # ms,about 30fps
				self.ui.buttonStart.setText('停止')
		else:
			self.timerVideo0.stop()
			self.cap0.release()
			self.ui.labelVideo0.clear()
			self.ui.labelFilePath.setText('尚未选择文件')
			self.ui.buttonStart.setText('开始')

	def chooseFileButtonClicked(self):
		self.video0Addr, _ = QFileDialog.getOpenFileName(self, '选择文件')
		self.flagFirstFrame = True  # 只有选择完文件后才有第一帧
		self.ui.labelFilePath.setText(self.video0Addr)
		ret,self.firstFrame=self.cap0.read()
		self.video0Resolution=[self.firstFrame.shape[1],self.firstFrame.shape[0]] # [w,h]
		self.showCV2CapRawImage(self.ui.labelVideo0,self.firstFrame)

	def showVideo0(self):
		flag, frame = self.cap0.read()
		frame=self.tracker.track(frame)
		self.showCV2CapRawImage(self.ui.labelVideo0, frame)

	def showCV2CapRawImage(self, label, rawImage):
		_, _, w, h = label.geometry().getRect()  # geometry() return QRect
		img = cv2.resize(rawImage, (w, h))
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		Qimg = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
		label.setPixmap(QtGui.QPixmap.fromImage(Qimg))

	def mousePressEvent(self, event):
		if self.flagFirstFrame:
			e = event.windowPos()
			self.recStart = [e.x(), e.y()]

	def mouseReleaseEvent(self, event):
		if self.flagFirstFrame:
			e = event.windowPos()
			self.recEnd = [e.x(), e.y()]
			box = self.calBox()
			self.flagFirstFrame = False
			self.tracker.track(self.firstFrame,box)
			self.slotInit()

	def calBox(self):
		WlabelVideo=self.labelVideoRec[2]
		HlabelVideo=self.labelVideoRec[3]
		startPos2LabelVideo = [self.recStart[0] - self.labelVideoRec[0], self.recStart[1] - self.labelVideoRec[1]]
		endPos2LabelVideo = [self.recEnd[0] - self.labelVideoRec[0], self.recEnd[1] - self.labelVideoRec[1]]
		ratioXStart = startPos2LabelVideo[0] / WlabelVideo
		ratioYStart = startPos2LabelVideo[1] / HlabelVideo
		ratioW = endPos2LabelVideo[0]-startPos2LabelVideo[0] / WlabelVideo
		ratioH = endPos2LabelVideo[1]-startPos2LabelVideo[1] / HlabelVideo
		frameW,frameH=self.video0Resolution
		return [frameW*ratioXStart, frameH*ratioYStart, frameW*ratioW, frameH*ratioH]


app = QApplication(sys.argv)
main_window = m_MainWindow()
main_window.show()
sys.exit(app.exec_())