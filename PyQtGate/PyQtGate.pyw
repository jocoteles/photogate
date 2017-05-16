# PyQtGate - PyQt user interface for Photogate Shield
#**********************************************************
#Joao Teles - DCNME/UFSCar - Oct 2016 - jocoteles@gmail.com
#Last update: Mar 03 2017

import debug	#python debuger routines (see debug.py for instructions)

import os, sys
import serial

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg
from User_interface import *
import ardcomm

msg_co = "Photo_co"		#message sent to arduino to start communication
msg_ok = "Photo_ok"		#message sent back to pc from arduino
msg_st = "Photo_st"		#Signal from pc confirming sequence start
msg_ha = "Photo_ha"		#Signal from pc asking spectrometer halt

#Baudrate for arduino communication: (115200 is the maximum brate that still works fine with th Philco netbooks from Learning Physics Lab and gives resolution of 1 ms. For a dual core desktop, brates until 460800 works fine and gives resolution of 300 us)
brate = 115200

echo = ["" ,""]		#receives the return of ECaT1_ports.arduino_echo function [message from arduino, port]
sport = ""		#the actual serial port name for arduino communication
runningflag = False

data = [[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]	#all channels data initialization
dref = [512,512,512,512,512,512]			#all channels ref initialization
dtime = []									#time table data
fdisp = ""									#Nome do arquivo contendo as formas de onda gravadas

#Colors:
chc = []
chc.append((0,0,255))		#channel color 1
chc.append((0,255,0))		#channel color 2
chc.append((255,0,0))		#channel color 3
chc.append((0,128,128))		#channel color 4
chc.append((128,128,0))		#channel color 5
chc.append((128,0,128))		#channel color 6

#Generic alert message class
class Alertparam(QtGui.QDialog):
	def __init__(self, msg):
		super(Alertparam, self).__init__()

		msgBox = QtGui.QMessageBox()
		msgBox.setText(msg)
		msgBox.addButton(QtGui.QPushButton('Ok'), QtGui.QMessageBox.YesRole)
		#msgBox.addButton(QtGui.QPushButton('Reject'), QtGui.QMessageBox.NoRole)
		#msgBox.addButton(QtGui.QPushButton('Cancel'), QtGui.QMessageBox.RejectRole)
		ret = msgBox.exec_();


class MyForm(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_PyQtGate()
		self.ui.setupUi(self)

		#Lists all available ports:
		portlist = ardcomm.serial_ports()
		for port in portlist: self.ui.cB_port.addItem(port)

		#Clear plot screens
		self.clearplots()

		#Serial port actions:
		QtCore.QObject.connect(self.ui.pB_connect, QtCore.SIGNAL('clicked()'), self.findport)
		QtCore.QObject.connect(self.ui.pB_closeconnection, QtCore.SIGNAL('clicked()'), self.closeconnection)
		QtCore.QObject.connect(self.ui.cB_port, QtCore.SIGNAL('activated(QString)'), self.setport)

		#Time scan spin box actions:
		QtCore.QObject.connect(self.ui.sP_channel_1, QtCore.SIGNAL('valueChanged(int)'), lambda: self.timescan(1))
		QtCore.QObject.connect(self.ui.sP_channel_2, QtCore.SIGNAL('valueChanged(int)'), lambda: self.timescan(2))
		QtCore.QObject.connect(self.ui.sP_channel_3, QtCore.SIGNAL('valueChanged(int)'), lambda: self.timescan(3))
		QtCore.QObject.connect(self.ui.sP_channel_4, QtCore.SIGNAL('valueChanged(int)'), lambda: self.timescan(4))
		QtCore.QObject.connect(self.ui.sP_channel_5, QtCore.SIGNAL('valueChanged(int)'), lambda: self.timescan(5))
		QtCore.QObject.connect(self.ui.sP_channel_6, QtCore.SIGNAL('valueChanged(int)'), lambda: self.timescan(6))
		QtCore.QObject.connect(self.ui.pB_timetable, QtCore.SIGNAL('clicked()'), self.timetable)

		#Reference level slider actions:
		QtCore.QObject.connect(self.ui.vS_channel_1, QtCore.SIGNAL('valueChanged(int)'), self.sliderreference)
		QtCore.QObject.connect(self.ui.vS_channel_2, QtCore.SIGNAL('valueChanged(int)'), self.sliderreference)
		QtCore.QObject.connect(self.ui.vS_channel_3, QtCore.SIGNAL('valueChanged(int)'), self.sliderreference)
		QtCore.QObject.connect(self.ui.vS_channel_4, QtCore.SIGNAL('valueChanged(int)'), self.sliderreference)
		QtCore.QObject.connect(self.ui.vS_channel_5, QtCore.SIGNAL('valueChanged(int)'), self.sliderreference)
		QtCore.QObject.connect(self.ui.vS_channel_6, QtCore.SIGNAL('valueChanged(int)'), self.sliderreference)

		#Reference level text actions:
		QtCore.QObject.connect(self.ui.lE_channel_1, QtCore.SIGNAL('editingFinished()'), self.textreference)
		QtCore.QObject.connect(self.ui.lE_channel_2, QtCore.SIGNAL('editingFinished()'), self.textreference)
		QtCore.QObject.connect(self.ui.lE_channel_3, QtCore.SIGNAL('editingFinished()'), self.textreference)
		QtCore.QObject.connect(self.ui.lE_channel_4, QtCore.SIGNAL('editingFinished()'), self.textreference)
		QtCore.QObject.connect(self.ui.lE_channel_5, QtCore.SIGNAL('editingFinished()'), self.textreference)
		QtCore.QObject.connect(self.ui.lE_channel_6, QtCore.SIGNAL('editingFinished()'), self.textreference)

		#Constrain action:
		QtCore.QObject.connect(self.ui.cB_constrain, QtCore.SIGNAL('stateChanged(int)'), self.textreference)

		#Start sequence actions:
		QtCore.QObject.connect(self.ui.pB_startacq, QtCore.SIGNAL('clicked()'), self.startacq)
		self.ui.pB_startacq.setStyleSheet("color: white; background-color: green;")

		#File handling actions:
		QtCore.QObject.connect(self.ui.pB_save, QtCore.SIGNAL('clicked()'), self.SaveFile)
		QtCore.QObject.connect(self.ui.pB_load, QtCore.SIGNAL('clicked()'), self.LoadFile)
		QtCore.QObject.connect(self.ui.pB_savetime, QtCore.SIGNAL('clicked()'), self.SaveFileTime)

		#Plot channels enable actions:
		QtCore.QObject.connect(self.ui.cB_channel_1, QtCore.SIGNAL('clicked()'), self.plotdata)
		QtCore.QObject.connect(self.ui.cB_channel_2, QtCore.SIGNAL('clicked()'), self.plotdata)
		QtCore.QObject.connect(self.ui.cB_channel_3, QtCore.SIGNAL('clicked()'), self.plotdata)
		QtCore.QObject.connect(self.ui.cB_channel_4, QtCore.SIGNAL('clicked()'), self.plotdata)
		QtCore.QObject.connect(self.ui.cB_channel_5, QtCore.SIGNAL('clicked()'), self.plotdata)
		QtCore.QObject.connect(self.ui.cB_channel_6, QtCore.SIGNAL('clicked()'), self.plotdata)

		#Place pictures in the About page:
		#self.ui.l_ufscar.setGeometry(10, 10, 400, 100)
		pixmap = QPixmap(os.getcwd() + "/logoufscar.jpg")
		self.ui.l_ufscar.setPixmap(pixmap)
		self.ui.l_ufscar.show()
		pixmap = QPixmap(os.getcwd() + "/logocca.jpg")
		self.ui.l_cca.setPixmap(pixmap)
		self.ui.l_cca.show()



	#Serial port communication functions:
	#-------------------------------------

	def findport(self):	#finds automatically the serial port connected to arduino using the msg_co and msg_ok messages
		global msg_co, msg_ok, sport, brate, echo
		
		self.ui.l_commstatus.setText("Iniciando comunicacao com Photogate Shield...")
		qApp.processEvents()	#used to transmit instructions (l_status in this case) to the window application outside the function
		echo = ardcomm.arduino_echo(msg_co, len(msg_ok), brate)
		if echo[0] == msg_ok :
			port = echo[1]
			sport = serial.Serial(port, brate, timeout=1)
			self.ui.l_commstatus.setText("Conexao com Photogate Shield bem sucedida na porta " + port + ".")
			sport.flushInput()
			sport.flushOutput()
		else:
			self.ui.l_commstatus.setText("Photogate Shield nao encontrado.")

	def closeconnection(self):	#close connection to the serial port if it's already opened
		global sport, echo, msg_ok

		if echo[0] == msg_ok :
			sport.flushInput()
			sport.flushOutput()
			sport.close()
			echo = ["",""]
			self.ui.l_commstatus.setText("Conexao com Photogate Shield terminada.")

	def setport(self, port):	#set a serial port chosen by the user
		global msg_co, msg_ok, sport, brate, echo

		if echo[0] == msg_ok :
			sport.flushInput()
			sport.flushOutput()
			sport.close()
			echo = ["", ""]

		p = str(port)
		self.ui.l_commstatus.setText("Iniciando comunicacao com Photogate Shield...")
		qApp.processEvents()
		try:			
			sport = serial.Serial(p, brate, timeout=1)
			time.sleep(2.0)
			sport.write(msg_co)
			res = sport.read(len(msg_ok))
			if res == msg_ok :
				echo = [msg_ok, p]
				self.ui.l_commstatus.setText("Conexao com Photogate Shield bem sucedida na porta " + p + ".")
				sport.flushInput()
				sport.flushOutput()
			else:
				sport.close()
				self.ui.l_commstatus.setText("Photogate Shield nao encontrado na porta " + p + ".")

		except (OSError, serial.SerialException):
			self.ui.l_commstatus.setText(p + " nao pode ser aberta.")


	#Time scan functions:
	#-------------------
	def timescan(self, ch):

		global data, dref

		if ch == 1:
			sopt = self.ui.cB_subida_1.isChecked()
			dopt = self.ui.cB_descida_1.isChecked()
		elif ch == 2:
			sopt = self.ui.cB_subida_2.isChecked()
			dopt = self.ui.cB_descida_2.isChecked()
		elif ch == 3:
			sopt = self.ui.cB_subida_3.isChecked()
			dopt = self.ui.cB_descida_3.isChecked()
		elif ch == 4:
			sopt = self.ui.cB_subida_4.isChecked()
			dopt = self.ui.cB_descida_4.isChecked()
		elif ch == 5:
			sopt = self.ui.cB_subida_5.isChecked()
			dopt = self.ui.cB_descida_5.isChecked()
		elif ch == 6:
			sopt = self.ui.cB_subida_6.isChecked()
			dopt = self.ui.cB_descida_6.isChecked()

		dtime = []
		sflag = False
		if data[ch][0] > dref[ch-1]:
			sflag = True

		for i in range(1,len(data[0])-1):
			
			if data[ch][i] > dref[ch-1] and sflag == False:
				sflag = True
				if sopt:
					dtime.append(+data[0][i])

			if data[ch][i] < dref[ch-1] and sflag == True:
				sflag = False
				if dopt:
					dtime.append(-data[0][i])

		if dtime == []:
			dtime = [0]

		if ch == 1:
			self.ui.sP_channel_1.setMaximum(len(dtime))
			ptime = self.ui.sP_channel_1.value() - 1
			self.ui.lE_time_1.setText("%.4f"%(dtime[ptime]))
			self.plotdata()
			self.ui.pW_channel_1.plot([abs(dtime[ptime])],[dref[0]], pen=pg.mkPen(color=(chc[0])), symbol='o')
		elif ch == 2:
			self.ui.sP_channel_2.setMaximum(len(dtime))
			ptime = self.ui.sP_channel_2.value() - 1
			self.ui.lE_time_2.setText("%.4f"%(dtime[ptime]))
			self.plotdata()
			self.ui.pW_channel_2.plot([abs(dtime[ptime])],[dref[1]], pen=pg.mkPen(color=(chc[1])), symbol='o')
		elif ch == 3:
			self.ui.sP_channel_3.setMaximum(len(dtime))
			ptime = self.ui.sP_channel_3.value() - 1
			self.ui.lE_time_3.setText("%.4f"%(dtime[ptime]))
			self.plotdata()
			self.ui.pW_channel_3.plot([abs(dtime[ptime])],[dref[2]], pen=pg.mkPen(color=(chc[2])), symbol='o')
		elif ch == 4:
			self.ui.sP_channel_4.setMaximum(len(dtime))
			ptime = self.ui.sP_channel_4.value() - 1
			self.ui.lE_time_4.setText("%.4f"%(dtime[ptime]))
			self.plotdata()
			self.ui.pW_channel_4.plot([abs(dtime[ptime])],[dref[3]], pen=pg.mkPen(color=(chc[3])), symbol='o')
		elif ch == 5:
			self.ui.sP_channel_5.setMaximum(len(dtime))
			ptime = self.ui.sP_channel_5.value() - 1
			self.ui.lE_time_5.setText("%.4f"%(dtime[ptime]))
			self.plotdata()
			self.ui.pW_channel_5.plot([abs(dtime[ptime])],[dref[4]], pen=pg.mkPen(color=(chc[4])), symbol='o')
		elif ch == 6:
			self.ui.sP_channel_6.setMaximum(len(dtime))
			ptime = self.ui.sP_channel_6.value() - 1
			self.ui.lE_time_6.setText("%.4f"%(dtime[ptime]))
			self.plotdata()
			self.ui.pW_channel_6.plot([abs(dtime[ptime])],[dref[5]], pen=pg.mkPen(color=(chc[5])), symbol='o')


	def timetable(self):

		global data, dref, dtime

		sopt = [0,0,0,0,0,0]
		dopt = [0,0,0,0,0,0]
		if self.ui.cB_subida_1.isChecked(): sopt[0] = True
		if self.ui.cB_descida_1.isChecked(): dopt[0] = True
		if self.ui.cB_subida_2.isChecked(): sopt[1] = True
		if self.ui.cB_descida_2.isChecked(): dopt[1] = True
		if self.ui.cB_subida_3.isChecked(): sopt[2] = True
		if self.ui.cB_descida_3.isChecked(): dopt[2] = True
		if self.ui.cB_subida_4.isChecked(): sopt[3] = True
		if self.ui.cB_descida_4.isChecked(): dopt[3] = True
		if self.ui.cB_subida_5.isChecked(): sopt[4] = True
		if self.ui.cB_descida_5.isChecked(): dopt[4] = True
		if self.ui.cB_subida_6.isChecked(): sopt[5] = True
		if self.ui.cB_descida_6.isChecked(): dopt[5] = True

		cBlist = []
		dtime = []
		if self.ui.cB_channel_1.isChecked():
			cBlist.append(0)
			dtime.append(["Canal 1"])
		if self.ui.cB_channel_2.isChecked():
			cBlist.append(1)
			dtime.append(["Canal 2"])
		if self.ui.cB_channel_3.isChecked():
			cBlist.append(2)
			dtime.append(["Canal 3"])
		if self.ui.cB_channel_4.isChecked():
			cBlist.append(3)
			dtime.append(["Canal 4"])
		if self.ui.cB_channel_5.isChecked():
			cBlist.append(4)
			dtime.append(["Canal 5"])
		if self.ui.cB_channel_6.isChecked():
			cBlist.append(5)
			dtime.append(["Canal 6"])

		k = 0
		for j in cBlist:

			sflag = False
			if data[j+1][0] > dref[j]:
				sflag = True

			for i in range(1,len(data[0])-1):
				if data[j+1][i] > dref[j] and sflag == False:
					sflag = True
					if sopt[j]:
						dtime[k].append(+data[0][i])
				if data[j+1][i] < dref[j] and sflag == True:
					sflag = False
					if dopt[j]:
						dtime[k].append(-data[0][i])
			k += 1

		Ncol = len(dtime)
		mdata = []
		for i in range(Ncol): mdata.append(len(dtime[i]))
		Nrow = max(mdata)

		if Nrow > 1:
			self.ui.tW_timetable.setRowCount(Nrow-1)
			self.ui.tW_timetable.setColumnCount(Ncol)
			
			for i in range(Ncol):
				idata = QTableWidgetItem(dtime[i][0])
				self.ui.tW_timetable.setHorizontalHeaderItem(i,idata)
				for j in range(1,len(dtime[i])):
					idata = QTableWidgetItem("%.4f"%(dtime[i][j]))
					self.ui.tW_timetable.setItem(j-1,i,idata)


	#Reference level functions:
	#--------------------------
	def sliderreference(self):
	
		global dref

		if self.ui.cB_constrain.isChecked() == False:

			dref[0] = self.ui.vS_channel_1.sliderPosition()
			dref[1] = self.ui.vS_channel_2.sliderPosition()
			dref[2] = self.ui.vS_channel_3.sliderPosition()
			dref[3] = self.ui.vS_channel_4.sliderPosition()
			dref[4] = self.ui.vS_channel_5.sliderPosition()
			dref[5] = self.ui.vS_channel_6.sliderPosition()

			self.ui.lE_channel_1.setText(str(dref[0]))
			self.ui.lE_channel_2.setText(str(dref[1]))
			self.ui.lE_channel_3.setText(str(dref[2]))
			self.ui.lE_channel_4.setText(str(dref[3]))
			self.ui.lE_channel_5.setText(str(dref[4]))
			self.ui.lE_channel_6.setText(str(dref[5]))

		else:

			dref[0] = self.ui.vS_channel_1.sliderPosition()
			dref[1] = dref[0]
			dref[2] = dref[0]
			dref[3] = dref[0]
			dref[4] = dref[0]
			dref[5] = dref[0]

			self.ui.lE_channel_1.setText(str(dref[0]))
			self.ui.lE_channel_2.setText(str(dref[0]))
			self.ui.lE_channel_3.setText(str(dref[0]))
			self.ui.lE_channel_4.setText(str(dref[0]))
			self.ui.lE_channel_5.setText(str(dref[0]))
			self.ui.lE_channel_6.setText(str(dref[0]))

			self.ui.vS_channel_2.setValue(dref[0])
			self.ui.vS_channel_3.setValue(dref[0])
			self.ui.vS_channel_4.setValue(dref[0])
			self.ui.vS_channel_5.setValue(dref[0])
			self.ui.vS_channel_6.setValue(dref[0])


		self.plotdata()

	def textreference(self):

		global dref

		if self.ui.cB_constrain.isChecked() == False:

			# Calculate the trigger level at wave form half height if 'm' is typed:
			# ---------------------------------------------------------------------
			if self.ui.lE_channel_1.text() == 'm':
				self.ui.lE_channel_1.setText(str(self.halfheight(1)))
			if self.ui.lE_channel_2.text() == 'm':
				self.ui.lE_channel_2.setText(str(self.halfheight(2)))
			if self.ui.lE_channel_3.text() == 'm':
				self.ui.lE_channel_3.setText(str(self.halfheight(3)))
			if self.ui.lE_channel_4.text() == 'm':
				self.ui.lE_channel_4.setText(str(self.halfheight(4)))
			if self.ui.lE_channel_5.text() == 'm':
				self.ui.lE_channel_5.setText(str(self.halfheight(5)))
			if self.ui.lE_channel_6.text() == 'm':
				self.ui.lE_channel_6.setText(str(self.halfheight(6)))


			dref[0] = int(self.ui.lE_channel_1.text())
			dref[1] = int(self.ui.lE_channel_2.text())
			dref[2] = int(self.ui.lE_channel_3.text())
			dref[3] = int(self.ui.lE_channel_4.text())
			dref[4] = int(self.ui.lE_channel_5.text())
			dref[5] = int(self.ui.lE_channel_6.text())

			self.ui.vS_channel_1.setValue(dref[0])
			self.ui.vS_channel_2.setValue(dref[1])
			self.ui.vS_channel_3.setValue(dref[2])
			self.ui.vS_channel_4.setValue(dref[3])
			self.ui.vS_channel_5.setValue(dref[4])
			self.ui.vS_channel_6.setValue(dref[5])

		else:

			dref[0] = int(self.ui.lE_channel_1.text())
			dref[1] = dref[0]
			dref[2] = dref[0]
			dref[3] = dref[0]
			dref[4] = dref[0]
			dref[5] = dref[0]

			self.ui.vS_channel_1.setValue(dref[0])
			self.ui.vS_channel_2.setValue(dref[0])
			self.ui.vS_channel_3.setValue(dref[0])
			self.ui.vS_channel_4.setValue(dref[0])
			self.ui.vS_channel_5.setValue(dref[0])
			self.ui.vS_channel_6.setValue(dref[0])

			self.ui.lE_channel_2.setText(str(dref[0]))
			self.ui.lE_channel_3.setText(str(dref[0]))
			self.ui.lE_channel_4.setText(str(dref[0]))
			self.ui.lE_channel_5.setText(str(dref[0]))
			self.ui.lE_channel_6.setText(str(dref[0]))

		self.plotdata()


	def halfheight(self, c):
		# Return the trigger level at wave form half height:
		# ----------------------------------------------
		dbl = 0.1	# initial time interval (in seconds) to calculate the base line
		imax = int(len(data[0])*dbl/data[0][len(data[0])-1])	# index that corresponds to dbl
		dmin = 0
		for i in range(imax):	# Calcultate the base line
			dmin += data[c][i]
		return int((float(dmin)/imax + max(data[c]))*0.5)


	#Plot data function:
	#--------------------------
	def plotdata(self):
	
		global data, dref

		self.clearplots()

		ti = data[0][0]
		tf = data[0][len(data[0])-1]

		self.ui.pW_channel_1.plot(data[0], data[1], pen= chc[0])
		self.ui.pW_channel_1.plot([ti,tf], [dref[0],dref[0]], pen=pg.mkPen(color=(chc[0]), style=QtCore.Qt.DashLine))
		
		self.ui.pW_channel_2.plot(data[0], data[2], pen= chc[1])
		self.ui.pW_channel_2.plot([ti,tf], [dref[1],dref[1]], pen=pg.mkPen(color=(chc[1]), style=QtCore.Qt.DashLine))

		self.ui.pW_channel_3.plot(data[0], data[3], pen= chc[2])
		self.ui.pW_channel_3.plot([ti,tf], [dref[2],dref[2]], pen=pg.mkPen(color=(chc[2]), style=QtCore.Qt.DashLine))

		self.ui.pW_channel_4.plot(data[0], data[4], pen= chc[3])
		self.ui.pW_channel_4.plot([ti,tf], [dref[3],dref[3]], pen=pg.mkPen(color=(chc[3]), style=QtCore.Qt.DashLine))

		self.ui.pW_channel_5.plot(data[0], data[5], pen= chc[4])
		self.ui.pW_channel_5.plot([ti,tf], [dref[4],dref[4]], pen=pg.mkPen(color=(chc[4]), style=QtCore.Qt.DashLine))

		self.ui.pW_channel_6.plot(data[0], data[6], pen= chc[5])
		self.ui.pW_channel_6.plot([ti,tf], [dref[5],dref[5]], pen=pg.mkPen(color=(chc[5]), style=QtCore.Qt.DashLine))
		
		if self.ui.cB_channel_1.isChecked() == True:
			self.ui.pW_all.plot(data[0], data[1], pen= chc[0])
			self.ui.pW_all.plot([ti,tf], [dref[0],dref[0]], pen=pg.mkPen(color=(chc[0]), style=QtCore.Qt.DashLine))
		
		if self.ui.cB_channel_2.isChecked() == True:
			self.ui.pW_all.plot(data[0], data[2], pen= chc[1])
			self.ui.pW_all.plot([ti,tf], [dref[1],dref[1]], pen=pg.mkPen(color=(chc[1]), style=QtCore.Qt.DashLine))

		if self.ui.cB_channel_3.isChecked() == True:
			self.ui.pW_all.plot(data[0], data[3], pen= chc[2])
			self.ui.pW_all.plot([ti,tf], [dref[2],dref[2]], pen=pg.mkPen(color=(chc[2]), style=QtCore.Qt.DashLine))

		if self.ui.cB_channel_4.isChecked() == True:
			self.ui.pW_all.plot(data[0], data[4], pen= chc[3])
			self.ui.pW_all.plot([ti,tf], [dref[3],dref[3]], pen=pg.mkPen(color=(chc[3]), style=QtCore.Qt.DashLine))

		if self.ui.cB_channel_5.isChecked() == True:
			self.ui.pW_all.plot(data[0], data[5], pen= chc[4])
			self.ui.pW_all.plot([ti,tf], [dref[4],dref[4]], pen=pg.mkPen(color=(chc[4]), style=QtCore.Qt.DashLine))

		if self.ui.cB_channel_6.isChecked() == True:
			self.ui.pW_all.plot(data[0], data[6], pen= chc[5])
			self.ui.pW_all.plot([ti,tf], [dref[5],dref[5]], pen=pg.mkPen(color=(chc[5]), style=QtCore.Qt.DashLine))

	#Clear plots:
	#--------------------------
	def clearplots(self):

		self.ui.pW_channel_1.setBackground('w')
		self.ui.pW_channel_1.clear()
		self.ui.pW_channel_2.setBackground('w')
		self.ui.pW_channel_2.clear()
		self.ui.pW_channel_3.setBackground('w')
		self.ui.pW_channel_3.clear()
		self.ui.pW_channel_4.setBackground('w')
		self.ui.pW_channel_4.clear()
		self.ui.pW_channel_5.setBackground('w')
		self.ui.pW_channel_5.clear()
		self.ui.pW_channel_6.setBackground('w')
		self.ui.pW_channel_6.clear()
		self.ui.pW_all.setBackground('w')
		self.ui.pW_all.clear()


	#Start acquisition function:
	#----------------------------
	def startacq(self):

		global echo, sport, data, runningflag, fdisp, msg_ok, msg_st

		if runningflag == False:

			if echo[0] == msg_ok :	#Verify if the connection to arduino was already stablished
			
				runningflag = True

				sport.flushInput()
				sport.flushOutput()
				sport.write(msg_st)
				
				#Verifiy delay bounds:
				d = float(self.ui.lE_delay.text())
				if d < 0:
					self.ui.lE_delay.setText(str(0))
					d = 0
				elif d > 65535:
					self.ui.lE_delay.setText(str(65535))
					d = 65535
				else:
					self.ui.lE_delay.setText(str(int(d)))
					d = int(d)

				#Send delay value to Arduino:
				a = d//256
				b = d%256
				sport.write(chr(a))
				sport.write(chr(b))

				self.ui.l_mostrador.setText("rodando...")
				self.ui.pB_startacq.setText("Gravando")
				self.ui.pB_startacq.setStyleSheet("color: white; background-color: red;")
				qApp.processEvents()

				data = [[],[],[],[],[],[],[]]

				while (runningflag == True):

					#Wait for the 2x6 bytes level values plus the 4 bytes time value:
					while (sport.inWaiting() < 16): 0 == 0

					#Get the level values for the 6 channels:
					for i in range(6):
						a0 = ord(str(sport.read()))
						a1 = ord(str(sport.read()))
						r = a0 + a1*256			#converts a word = 2 bytes into a decimal
						data[i+1].append(r)
				
					#Get the time values:
					a0 = ord(str(sport.read()))
					a1 = ord(str(sport.read()))
					a2 = ord(str(sport.read()))
					a3 = ord(str(sport.read()))
					r = a0 + a1*256 + a2*65536 + a3*16777216	#converts a double word = 4 bytes into a decimal
					data[0].append(r*1e-6)

					qApp.processEvents()

				#sport.flushInput()
				#sport.flushOutput()
				sport.write(msg_ha)

				self.plotdata()

				self.ui.pB_startacq.setText("Iniciar")
				self.ui.pB_startacq.setStyleSheet("color: white; background-color: green;")
				self.ui.l_mostrador.setText("finalizada.")

				self.ui.l_filename.setText("*Arquivo: " + fdisp)


			else:
				win = Alertparam("Photogate Shield nao conectado!")
				win.show()

		else:
			runningflag = False


	#Manipulacao de arquivos
	def SaveFile(self):

		global data, fdisp

		if len(data[0]) > 2:

			filename = QtGui.QFileDialog.getSaveFileName(self, 'Salvar formas de onda', '.')
			fname = open(filename, 'w')				#Signal data

			fdisp = filename.split("/")
			fdisp = fdisp[len(fdisp)-1]
			self.ui.l_filename.setText("Arquivo: " + fdisp)

			fname.write("Tempo(s)\tCanal_1\tCanal_2\tCanal_3\tCanal_4\tCanal_5\tCanal_6\n")

			Ncol = len(data)
			Nrow = len(data[0])
			for i in range(Nrow):
				for j in range(Ncol-1):
					fname.write("%.4f"%(data[j][i])+"\t")
				fname.write("%.4f"%(data[j+1][i])+"\n")

			fname.close()

		else:

			win = Alertparam("Nao ha dados a serem gravados!")
			win.show()


	def LoadFile(self):

		global data, fdisp

		filename = QtGui.QFileDialog.getOpenFileName(self, 'Ler formas de onda', '~')
		fname = open(filename, 'r')			#Signal data

		fdisp = filename.split("/")
		fdisp = fdisp[len(fdisp)-1]
		self.ui.l_filename.setText("Arquivo: " + fdisp)

		try:

			line = fname.readline()		#skips the header

			data = [[],[],[],[],[],[],[]]
			while True :

				line = fname.readline()
				if (line == ""): break;

				words = line.split("\t")
				i = 0
				for w in words:
					data[i].append(float(w))
					i += 1

			fname.close()

			self.plotdata()
		
		except:

			win = Alertparam("Arquivo fora do padrao!")
			win.show()

	def SaveFileTime(self):

		global dtime

		if dtime != []:

			filename = QtGui.QFileDialog.getSaveFileName(self, 'Salvar tabela de tempos', '.')
			fname = open(filename, 'w')				#Signal data

			Nrow = len(dtime)
			for i in range(Nrow):
				for j in range(len(dtime[i])):
					fname.write("%.4f"%(dtime[i][j])+"\t")
				fname.write("\n")

			fname.close()

		else:

			win = Alertparam("Nao ha dados a serem gravados!")
			win.show()



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)

	myapp = MyForm()
	myapp.show()

	sys.exit(app.exec_())

