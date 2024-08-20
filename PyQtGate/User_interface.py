# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_interface.ui'
#
# Created: Tue May 16 10:33:40 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_PyQtGate(object):
    def setupUi(self, PyQtGate):
        PyQtGate.setObjectName(_fromUtf8("PyQtGate"))
        PyQtGate.setWindowModality(QtCore.Qt.ApplicationModal)
        PyQtGate.resize(862, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PyQtGate.sizePolicy().hasHeightForWidth())
        PyQtGate.setSizePolicy(sizePolicy)
        PyQtGate.setAcceptDrops(False)
        PyQtGate.setAutoFillBackground(False)
        PyQtGate.setModal(True)
        self.tabPrincipal = QtWidgets.QTabWidget(PyQtGate)
        self.tabPrincipal.setGeometry(QtCore.QRect(6, 7, 851, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabPrincipal.sizePolicy().hasHeightForWidth())
        self.tabPrincipal.setSizePolicy(sizePolicy)
        self.tabPrincipal.setObjectName(_fromUtf8("tabPrincipal"))
        self.tab_mostrador = QtWidgets.QWidget()
        self.tab_mostrador.setObjectName(_fromUtf8("tab_mostrador"))
        self.pB_startacq = QtWidgets.QPushButton(self.tab_mostrador)
        self.pB_startacq.setGeometry(QtCore.QRect(520, 498, 141, 27))
        self.pB_startacq.setObjectName(_fromUtf8("pB_startacq"))
        self.l_mostrador = QtWidgets.QLabel(self.tab_mostrador)
        self.l_mostrador.setGeometry(QtCore.QRect(110, 503, 111, 17))
        self.l_mostrador.setObjectName(_fromUtf8("l_mostrador"))
        self.label_7 = QtWidgets.QLabel(self.tab_mostrador)
        self.label_7.setGeometry(QtCore.QRect(30, 503, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.vS_channel_1 = QtWidgets.QSlider(self.tab_mostrador)
        self.vS_channel_1.setGeometry(QtCore.QRect(758, 27, 29, 61))
        self.vS_channel_1.setMaximum(1023)
        self.vS_channel_1.setProperty("value", 512)
        self.vS_channel_1.setTracking(True)
        self.vS_channel_1.setOrientation(QtCore.Qt.Vertical)
        self.vS_channel_1.setObjectName(_fromUtf8("vS_channel_1"))
        self.lE_channel_1 = QtWidgets.QLineEdit(self.tab_mostrador)
        self.lE_channel_1.setGeometry(QtCore.QRect(788, 47, 41, 27))
        self.lE_channel_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_channel_1.setObjectName(_fromUtf8("lE_channel_1"))
        self.vS_channel_2 = QtWidgets.QSlider(self.tab_mostrador)
        self.vS_channel_2.setGeometry(QtCore.QRect(758, 107, 29, 61))
        self.vS_channel_2.setMaximum(1023)
        self.vS_channel_2.setProperty("value", 512)
        self.vS_channel_2.setSliderPosition(512)
        self.vS_channel_2.setOrientation(QtCore.Qt.Vertical)
        self.vS_channel_2.setObjectName(_fromUtf8("vS_channel_2"))
        self.lE_channel_2 = QtWidgets.QLineEdit(self.tab_mostrador)
        self.lE_channel_2.setGeometry(QtCore.QRect(788, 127, 41, 27))
        self.lE_channel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_channel_2.setObjectName(_fromUtf8("lE_channel_2"))
        self.lE_channel_5 = QtWidgets.QLineEdit(self.tab_mostrador)
        self.lE_channel_5.setGeometry(QtCore.QRect(788, 367, 41, 27))
        self.lE_channel_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_channel_5.setObjectName(_fromUtf8("lE_channel_5"))
        self.lE_channel_4 = QtWidgets.QLineEdit(self.tab_mostrador)
        self.lE_channel_4.setGeometry(QtCore.QRect(788, 287, 41, 27))
        self.lE_channel_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_channel_4.setObjectName(_fromUtf8("lE_channel_4"))
        self.lE_channel_3 = QtWidgets.QLineEdit(self.tab_mostrador)
        self.lE_channel_3.setGeometry(QtCore.QRect(788, 207, 41, 27))
        self.lE_channel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_channel_3.setObjectName(_fromUtf8("lE_channel_3"))
        self.lE_channel_6 = QtWidgets.QLineEdit(self.tab_mostrador)
        self.lE_channel_6.setGeometry(QtCore.QRect(788, 447, 41, 27))
        self.lE_channel_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_channel_6.setObjectName(_fromUtf8("lE_channel_6"))
        self.vS_channel_4 = QtWidgets.QSlider(self.tab_mostrador)
        self.vS_channel_4.setGeometry(QtCore.QRect(758, 267, 29, 61))
        self.vS_channel_4.setMaximum(1023)
        self.vS_channel_4.setProperty("value", 512)
        self.vS_channel_4.setOrientation(QtCore.Qt.Vertical)
        self.vS_channel_4.setObjectName(_fromUtf8("vS_channel_4"))
        self.vS_channel_3 = QtWidgets.QSlider(self.tab_mostrador)
        self.vS_channel_3.setGeometry(QtCore.QRect(758, 187, 29, 61))
        self.vS_channel_3.setMaximum(1023)
        self.vS_channel_3.setProperty("value", 512)
        self.vS_channel_3.setOrientation(QtCore.Qt.Vertical)
        self.vS_channel_3.setObjectName(_fromUtf8("vS_channel_3"))
        self.vS_channel_5 = QtWidgets.QSlider(self.tab_mostrador)
        self.vS_channel_5.setGeometry(QtCore.QRect(758, 347, 29, 61))
        self.vS_channel_5.setMaximum(1023)
        self.vS_channel_5.setProperty("value", 512)
        self.vS_channel_5.setOrientation(QtCore.Qt.Vertical)
        self.vS_channel_5.setObjectName(_fromUtf8("vS_channel_5"))
        self.vS_channel_6 = QtWidgets.QSlider(self.tab_mostrador)
        self.vS_channel_6.setGeometry(QtCore.QRect(758, 427, 29, 61))
        self.vS_channel_6.setMaximum(1023)
        self.vS_channel_6.setProperty("value", 512)
        self.vS_channel_6.setOrientation(QtCore.Qt.Vertical)
        self.vS_channel_6.setObjectName(_fromUtf8("vS_channel_6"))
        self.tab_views = QtWidgets.QTabWidget(self.tab_mostrador)
        self.tab_views.setGeometry(QtCore.QRect(2, 3, 751, 491))
        self.tab_views.setTabPosition(QtWidgets.QTabWidget.West)
        self.tab_views.setObjectName(_fromUtf8("tab_views"))
        self.tab_separados = QtWidgets.QWidget()
        self.tab_separados.setObjectName(_fromUtf8("tab_separados"))
        self.pW_channel_5 = PlotWidget(self.tab_separados)
        self.pW_channel_5.setGeometry(QtCore.QRect(8, 349, 701, 51))
        self.pW_channel_5.setObjectName(_fromUtf8("pW_channel_5"))
        self.pW_channel_3 = PlotWidget(self.tab_separados)
        self.pW_channel_3.setGeometry(QtCore.QRect(8, 189, 701, 51))
        self.pW_channel_3.setObjectName(_fromUtf8("pW_channel_3"))
        self.sP_channel_4 = QtWidgets.QSpinBox(self.tab_separados)
        self.sP_channel_4.setGeometry(QtCore.QRect(78, 246, 61, 21))
        self.sP_channel_4.setMinimum(1)
        self.sP_channel_4.setObjectName(_fromUtf8("sP_channel_4"))
        self.lE_time_1 = QtWidgets.QLineEdit(self.tab_separados)
        self.lE_time_1.setGeometry(QtCore.QRect(148, 5, 81, 21))
        self.lE_time_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_time_1.setObjectName(_fromUtf8("lE_time_1"))
        self.sP_channel_2 = QtWidgets.QSpinBox(self.tab_separados)
        self.sP_channel_2.setGeometry(QtCore.QRect(79, 86, 61, 21))
        self.sP_channel_2.setMinimum(1)
        self.sP_channel_2.setObjectName(_fromUtf8("sP_channel_2"))
        self.lE_time_5 = QtWidgets.QLineEdit(self.tab_separados)
        self.lE_time_5.setGeometry(QtCore.QRect(148, 325, 81, 21))
        self.lE_time_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_time_5.setObjectName(_fromUtf8("lE_time_5"))
        self.cB_subida_4 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_subida_4.setGeometry(QtCore.QRect(313, 246, 100, 22))
        self.cB_subida_4.setChecked(True)
        self.cB_subida_4.setObjectName(_fromUtf8("cB_subida_4"))
        self.pW_channel_4 = PlotWidget(self.tab_separados)
        self.pW_channel_4.setGeometry(QtCore.QRect(8, 269, 701, 51))
        self.pW_channel_4.setObjectName(_fromUtf8("pW_channel_4"))
        self.cB_descida_2 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_descida_2.setGeometry(QtCore.QRect(408, 86, 100, 22))
        self.cB_descida_2.setObjectName(_fromUtf8("cB_descida_2"))
        self.l_channel_8 = QtWidgets.QLabel(self.tab_separados)
        self.l_channel_8.setGeometry(QtCore.QRect(232, 90, 70, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.l_channel_8.setFont(font)
        self.l_channel_8.setObjectName(_fromUtf8("l_channel_8"))
        self.sP_channel_3 = QtWidgets.QSpinBox(self.tab_separados)
        self.sP_channel_3.setGeometry(QtCore.QRect(79, 166, 61, 21))
        self.sP_channel_3.setMinimum(1)
        self.sP_channel_3.setObjectName(_fromUtf8("sP_channel_3"))
        self.l_channel_12 = QtWidgets.QLabel(self.tab_separados)
        self.l_channel_12.setGeometry(QtCore.QRect(232, 410, 70, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.l_channel_12.setFont(font)
        self.l_channel_12.setObjectName(_fromUtf8("l_channel_12"))
        self.l_channel_9 = QtWidgets.QLabel(self.tab_separados)
        self.l_channel_9.setGeometry(QtCore.QRect(232, 170, 70, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.l_channel_9.setFont(font)
        self.l_channel_9.setObjectName(_fromUtf8("l_channel_9"))
        self.cB_subida_1 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_subida_1.setGeometry(QtCore.QRect(312, 6, 97, 22))
        self.cB_subida_1.setChecked(True)
        self.cB_subida_1.setObjectName(_fromUtf8("cB_subida_1"))
        self.l_channel_10 = QtWidgets.QLabel(self.tab_separados)
        self.l_channel_10.setGeometry(QtCore.QRect(232, 250, 70, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.l_channel_10.setFont(font)
        self.l_channel_10.setObjectName(_fromUtf8("l_channel_10"))
        self.lE_time_3 = QtWidgets.QLineEdit(self.tab_separados)
        self.lE_time_3.setGeometry(QtCore.QRect(149, 165, 81, 21))
        self.lE_time_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_time_3.setObjectName(_fromUtf8("lE_time_3"))
        self.pW_channel_2 = PlotWidget(self.tab_separados)
        self.pW_channel_2.setGeometry(QtCore.QRect(8, 109, 701, 51))
        self.pW_channel_2.setObjectName(_fromUtf8("pW_channel_2"))
        self.cB_descida_5 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_descida_5.setGeometry(QtCore.QRect(408, 325, 100, 22))
        self.cB_descida_5.setObjectName(_fromUtf8("cB_descida_5"))
        self.l_channel_11 = QtWidgets.QLabel(self.tab_separados)
        self.l_channel_11.setGeometry(QtCore.QRect(232, 330, 70, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.l_channel_11.setFont(font)
        self.l_channel_11.setObjectName(_fromUtf8("l_channel_11"))
        self.cB_descida_6 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_descida_6.setGeometry(QtCore.QRect(408, 405, 100, 22))
        self.cB_descida_6.setObjectName(_fromUtf8("cB_descida_6"))
        self.cB_subida_3 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_subida_3.setGeometry(QtCore.QRect(313, 165, 100, 22))
        self.cB_subida_3.setChecked(True)
        self.cB_subida_3.setObjectName(_fromUtf8("cB_subida_3"))
        self.sP_channel_5 = QtWidgets.QSpinBox(self.tab_separados)
        self.sP_channel_5.setGeometry(QtCore.QRect(78, 326, 61, 21))
        self.sP_channel_5.setMinimum(1)
        self.sP_channel_5.setObjectName(_fromUtf8("sP_channel_5"))
        self.sP_channel_6 = QtWidgets.QSpinBox(self.tab_separados)
        self.sP_channel_6.setGeometry(QtCore.QRect(78, 406, 61, 21))
        self.sP_channel_6.setMinimum(1)
        self.sP_channel_6.setObjectName(_fromUtf8("sP_channel_6"))
        self.cB_subida_2 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_subida_2.setGeometry(QtCore.QRect(313, 86, 100, 22))
        self.cB_subida_2.setChecked(True)
        self.cB_subida_2.setObjectName(_fromUtf8("cB_subida_2"))
        self.sP_channel_1 = QtWidgets.QSpinBox(self.tab_separados)
        self.sP_channel_1.setGeometry(QtCore.QRect(78, 6, 61, 21))
        self.sP_channel_1.setMinimum(1)
        self.sP_channel_1.setObjectName(_fromUtf8("sP_channel_1"))
        self.cB_descida_4 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_descida_4.setGeometry(QtCore.QRect(408, 246, 100, 22))
        self.cB_descida_4.setObjectName(_fromUtf8("cB_descida_4"))
        self.cB_subida_5 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_subida_5.setGeometry(QtCore.QRect(313, 325, 100, 22))
        self.cB_subida_5.setChecked(True)
        self.cB_subida_5.setObjectName(_fromUtf8("cB_subida_5"))
        self.pW_channel_6 = PlotWidget(self.tab_separados)
        self.pW_channel_6.setGeometry(QtCore.QRect(8, 429, 701, 51))
        self.pW_channel_6.setObjectName(_fromUtf8("pW_channel_6"))
        self.cB_descida_3 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_descida_3.setGeometry(QtCore.QRect(408, 165, 100, 22))
        self.cB_descida_3.setObjectName(_fromUtf8("cB_descida_3"))
        self.cB_subida_6 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_subida_6.setGeometry(QtCore.QRect(313, 405, 100, 22))
        self.cB_subida_6.setChecked(True)
        self.cB_subida_6.setObjectName(_fromUtf8("cB_subida_6"))
        self.l_channel_7 = QtWidgets.QLabel(self.tab_separados)
        self.l_channel_7.setGeometry(QtCore.QRect(231, 10, 70, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.l_channel_7.setFont(font)
        self.l_channel_7.setObjectName(_fromUtf8("l_channel_7"))
        self.lE_time_6 = QtWidgets.QLineEdit(self.tab_separados)
        self.lE_time_6.setGeometry(QtCore.QRect(148, 405, 81, 21))
        self.lE_time_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_time_6.setObjectName(_fromUtf8("lE_time_6"))
        self.lE_time_2 = QtWidgets.QLineEdit(self.tab_separados)
        self.lE_time_2.setGeometry(QtCore.QRect(149, 85, 81, 21))
        self.lE_time_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_time_2.setObjectName(_fromUtf8("lE_time_2"))
        self.cB_descida_1 = QtWidgets.QCheckBox(self.tab_separados)
        self.cB_descida_1.setGeometry(QtCore.QRect(407, 6, 97, 22))
        self.cB_descida_1.setObjectName(_fromUtf8("cB_descida_1"))
        self.lE_time_4 = QtWidgets.QLineEdit(self.tab_separados)
        self.lE_time_4.setGeometry(QtCore.QRect(148, 245, 81, 21))
        self.lE_time_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_time_4.setObjectName(_fromUtf8("lE_time_4"))
        self.pW_channel_1 = PlotWidget(self.tab_separados)
        self.pW_channel_1.setGeometry(QtCore.QRect(8, 29, 701, 51))
        self.pW_channel_1.setObjectName(_fromUtf8("pW_channel_1"))
        self.tab_views.addTab(self.tab_separados, _fromUtf8(""))
        self.tab_juntos = QtWidgets.QWidget()
        self.tab_juntos.setObjectName(_fromUtf8("tab_juntos"))
        self.pW_all = PlotWidget(self.tab_juntos)
        self.pW_all.setGeometry(QtCore.QRect(9, 7, 701, 341))
        self.pW_all.setObjectName(_fromUtf8("pW_all"))
        self.tW_timetable = QtWidgets.QTableWidget(self.tab_juntos)
        self.tW_timetable.setGeometry(QtCore.QRect(182, 357, 528, 111))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tW_timetable.setFont(font)
        self.tW_timetable.setObjectName(_fromUtf8("tW_timetable"))
        self.tW_timetable.setColumnCount(0)
        self.tW_timetable.setRowCount(0)
        self.tW_timetable.horizontalHeader().setDefaultSectionSize(85)
        self.tW_timetable.verticalHeader().setDefaultSectionSize(20)
        self.pB_timetable = QtWidgets.QPushButton(self.tab_juntos)
        self.pB_timetable.setGeometry(QtCore.QRect(40, 410, 111, 27))
        self.pB_timetable.setObjectName(_fromUtf8("pB_timetable"))
        self.tab_views.addTab(self.tab_juntos, _fromUtf8(""))
        self.cB_constrain = QtWidgets.QCheckBox(self.tab_mostrador)
        self.cB_constrain.setGeometry(QtCore.QRect(690, 501, 151, 22))
        self.cB_constrain.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.cB_constrain.setObjectName(_fromUtf8("cB_constrain"))
        self.cB_channel_1 = QtWidgets.QCheckBox(self.tab_mostrador)
        self.cB_channel_1.setGeometry(QtCore.QRect(762, 9, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cB_channel_1.setFont(font)
        self.cB_channel_1.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);"))
        self.cB_channel_1.setChecked(True)
        self.cB_channel_1.setObjectName(_fromUtf8("cB_channel_1"))
        self.cB_channel_2 = QtWidgets.QCheckBox(self.tab_mostrador)
        self.cB_channel_2.setGeometry(QtCore.QRect(762, 90, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cB_channel_2.setFont(font)
        self.cB_channel_2.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.cB_channel_2.setChecked(True)
        self.cB_channel_2.setObjectName(_fromUtf8("cB_channel_2"))
        self.cB_channel_3 = QtWidgets.QCheckBox(self.tab_mostrador)
        self.cB_channel_3.setGeometry(QtCore.QRect(762, 170, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cB_channel_3.setFont(font)
        self.cB_channel_3.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.cB_channel_3.setChecked(True)
        self.cB_channel_3.setObjectName(_fromUtf8("cB_channel_3"))
        self.cB_channel_4 = QtWidgets.QCheckBox(self.tab_mostrador)
        self.cB_channel_4.setGeometry(QtCore.QRect(762, 250, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cB_channel_4.setFont(font)
        self.cB_channel_4.setStyleSheet(_fromUtf8("color: rgb(0, 128, 128);\n"
"background-color: rgb(255, 255, 255);"))
        self.cB_channel_4.setChecked(True)
        self.cB_channel_4.setObjectName(_fromUtf8("cB_channel_4"))
        self.cB_channel_5 = QtWidgets.QCheckBox(self.tab_mostrador)
        self.cB_channel_5.setGeometry(QtCore.QRect(762, 330, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cB_channel_5.setFont(font)
        self.cB_channel_5.setStyleSheet(_fromUtf8("color: rgb(128, 128, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.cB_channel_5.setChecked(True)
        self.cB_channel_5.setObjectName(_fromUtf8("cB_channel_5"))
        self.cB_channel_6 = QtWidgets.QCheckBox(self.tab_mostrador)
        self.cB_channel_6.setGeometry(QtCore.QRect(762, 410, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cB_channel_6.setFont(font)
        self.cB_channel_6.setStyleSheet(_fromUtf8("color: rgb(128, 0, 128);\n"
"background-color: rgb(255, 255, 255);"))
        self.cB_channel_6.setChecked(True)
        self.cB_channel_6.setObjectName(_fromUtf8("cB_channel_6"))
        self.label_8 = QtWidgets.QLabel(self.tab_mostrador)
        self.label_8.setGeometry(QtCore.QRect(334, 504, 51, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lE_delay = QtWidgets.QLineEdit(self.tab_mostrador)
        self.lE_delay.setGeometry(QtCore.QRect(394, 502, 61, 21))
        self.lE_delay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_delay.setObjectName(_fromUtf8("lE_delay"))
        self.label_9 = QtWidgets.QLabel(self.tab_mostrador)
        self.label_9.setGeometry(QtCore.QRect(460, 504, 21, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tabPrincipal.addTab(self.tab_mostrador, _fromUtf8(""))
        self.tab_arquivo = QtWidgets.QWidget()
        self.tab_arquivo.setObjectName(_fromUtf8("tab_arquivo"))
        self.pB_save = QtWidgets.QPushButton(self.tab_arquivo)
        self.pB_save.setGeometry(QtCore.QRect(80, 70, 181, 27))
        self.pB_save.setObjectName(_fromUtf8("pB_save"))
        self.pB_load = QtWidgets.QPushButton(self.tab_arquivo)
        self.pB_load.setGeometry(QtCore.QRect(80, 110, 181, 27))
        self.pB_load.setObjectName(_fromUtf8("pB_load"))
        self.pB_savetime = QtWidgets.QPushButton(self.tab_arquivo)
        self.pB_savetime.setGeometry(QtCore.QRect(310, 70, 181, 27))
        self.pB_savetime.setObjectName(_fromUtf8("pB_savetime"))
        self.tabPrincipal.addTab(self.tab_arquivo, _fromUtf8(""))
        self.tab_serial = QtWidgets.QWidget()
        self.tab_serial.setObjectName(_fromUtf8("tab_serial"))
        self.pB_connect = QtWidgets.QPushButton(self.tab_serial)
        self.pB_connect.setGeometry(QtCore.QRect(70, 90, 261, 27))
        self.pB_connect.setObjectName(_fromUtf8("pB_connect"))
        self.label_2 = QtWidgets.QLabel(self.tab_serial)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 311, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pB_closeconnection = QtWidgets.QPushButton(self.tab_serial)
        self.pB_closeconnection.setGeometry(QtCore.QRect(70, 210, 98, 27))
        self.pB_closeconnection.setObjectName(_fromUtf8("pB_closeconnection"))
        self.layoutWidget = QtWidgets.QWidget(self.tab_serial)
        self.layoutWidget.setGeometry(QtCore.QRect(71, 141, 231, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.cB_port = QtWidgets.QComboBox(self.layoutWidget)
        self.cB_port.setObjectName(_fromUtf8("cB_port"))
        self.horizontalLayout_2.addWidget(self.cB_port)
        self.label_25 = QtWidgets.QLabel(self.tab_serial)
        self.label_25.setGeometry(QtCore.QRect(70, 270, 101, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.l_commstatus = QtWidgets.QLabel(self.tab_serial)
        self.l_commstatus.setGeometry(QtCore.QRect(180, 270, 491, 17))
        self.l_commstatus.setObjectName(_fromUtf8("l_commstatus"))
        self.tabPrincipal.addTab(self.tab_serial, _fromUtf8(""))
        self.tab_sobre = QtWidgets.QWidget()
        self.tab_sobre.setObjectName(_fromUtf8("tab_sobre"))
        self.l_ufscar = QtWidgets.QLabel(self.tab_sobre)
        self.l_ufscar.setGeometry(QtCore.QRect(160, 370, 180, 125))
        self.l_ufscar.setObjectName(_fromUtf8("l_ufscar"))
        self.l_cca = QtWidgets.QLabel(self.tab_sobre)
        self.l_cca.setGeometry(QtCore.QRect(567, 368, 130, 122))
        self.l_cca.setObjectName(_fromUtf8("l_cca"))
        self.label_3 = QtWidgets.QLabel(self.tab_sobre)
        self.label_3.setGeometry(QtCore.QRect(530, 497, 211, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_sobre)
        self.textBrowser.setGeometry(QtCore.QRect(80, 40, 681, 321))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabPrincipal.addTab(self.tab_sobre, _fromUtf8(""))
        self.l_filename = QtWidgets.QLabel(PyQtGate)
        self.l_filename.setGeometry(QtCore.QRect(290, 12, 561, 17))
        self.l_filename.setObjectName(_fromUtf8("l_filename"))

        self.retranslateUi(PyQtGate)
        self.tabPrincipal.setCurrentIndex(0)
        self.tab_views.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PyQtGate)

    def retranslateUi(self, PyQtGate):
        PyQtGate.setWindowTitle(_translate("PyQtGate", "PyQtGate", None))
        self.tab_mostrador.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Mostrar dados de aquisição</p></body></html>", None))
        self.pB_startacq.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Inicia e interrompe a aquisição de sinal do Photogate</p></body></html>", None))
        self.pB_startacq.setText(_translate("PyQtGate", "Iniciar", None))
        self.l_mostrador.setText(_translate("PyQtGate", "parada", None))
        self.label_7.setText(_translate("PyQtGate", "Aquisição:", None))
        self.vS_channel_1.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Nível de referência para disparo de tempo do Canal 1</p></body></html>", None))
        self.lE_channel_1.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Nível de referência para disparo de tempo do Canal 1</p></body></html>", None))
        self.lE_channel_1.setText(_translate("PyQtGate", "512", None))
        self.vS_channel_2.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Nível de referência para disparo de tempo do Canal 2</p></body></html>", None))
        self.lE_channel_2.setText(_translate("PyQtGate", "512", None))
        self.lE_channel_5.setText(_translate("PyQtGate", "512", None))
        self.lE_channel_4.setText(_translate("PyQtGate", "512", None))
        self.lE_channel_3.setText(_translate("PyQtGate", "512", None))
        self.lE_channel_6.setText(_translate("PyQtGate", "512", None))
        self.vS_channel_4.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Nível de referência para disparo de tempo do Canal 4</p></body></html>", None))
        self.vS_channel_3.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Nível de referência para disparo de tempo do Canal 3</p></body></html>", None))
        self.vS_channel_5.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Nível de referência para disparo de tempo do Canal 5</p></body></html>", None))
        self.vS_channel_6.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Nível de referência para disparo de tempo do Canal 6</p></body></html>", None))
        self.sP_channel_4.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Varre os tempos disparados.</p></body></html>", None))
        self.lE_time_1.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Tempo de disparo</p></body></html>", None))
        self.lE_time_1.setText(_translate("PyQtGate", "0", None))
        self.sP_channel_2.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Varre os tempos disparados.</p></body></html>", None))
        self.lE_time_5.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Tempo de disparo</p></body></html>", None))
        self.lE_time_5.setText(_translate("PyQtGate", "0", None))
        self.cB_subida_4.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na subida em relação à referência</p></body></html>", None))
        self.cB_subida_4.setText(_translate("PyQtGate", "Subida", None))
        self.cB_descida_2.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na descida em relação à referência</p></body></html>", None))
        self.cB_descida_2.setText(_translate("PyQtGate", "Descida", None))
        self.l_channel_8.setText(_translate("PyQtGate", "segundos", None))
        self.sP_channel_3.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Varre os tempos disparados.</p></body></html>", None))
        self.l_channel_12.setText(_translate("PyQtGate", "segundos", None))
        self.l_channel_9.setText(_translate("PyQtGate", "segundos", None))
        self.cB_subida_1.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na subida em relação à referência</p></body></html>", None))
        self.cB_subida_1.setText(_translate("PyQtGate", "Subida", None))
        self.l_channel_10.setText(_translate("PyQtGate", "segundos", None))
        self.lE_time_3.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Tempo de disparo</p></body></html>", None))
        self.lE_time_3.setText(_translate("PyQtGate", "0", None))
        self.cB_descida_5.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na descida em relação à referência</p></body></html>", None))
        self.cB_descida_5.setText(_translate("PyQtGate", "Descida", None))
        self.l_channel_11.setText(_translate("PyQtGate", "segundos", None))
        self.cB_descida_6.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na descida em relação à referência</p></body></html>", None))
        self.cB_descida_6.setText(_translate("PyQtGate", "Descida", None))
        self.cB_subida_3.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na subida em relação à referência</p></body></html>", None))
        self.cB_subida_3.setText(_translate("PyQtGate", "Subida", None))
        self.sP_channel_5.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Varre os tempos disparados.</p></body></html>", None))
        self.sP_channel_6.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Varre os tempos disparados.</p></body></html>", None))
        self.cB_subida_2.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na subida em relação à referência</p></body></html>", None))
        self.cB_subida_2.setText(_translate("PyQtGate", "Subida", None))
        self.sP_channel_1.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Varre os tempos disparados.</p></body></html>", None))
        self.cB_descida_4.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na descida em relação à referência</p></body></html>", None))
        self.cB_descida_4.setText(_translate("PyQtGate", "Descida", None))
        self.cB_subida_5.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na subida em relação à referência</p></body></html>", None))
        self.cB_subida_5.setText(_translate("PyQtGate", "Subida", None))
        self.cB_descida_3.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na descida em relação à referência</p></body></html>", None))
        self.cB_descida_3.setText(_translate("PyQtGate", "Descida", None))
        self.cB_subida_6.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na subida em relação à referência</p></body></html>", None))
        self.cB_subida_6.setText(_translate("PyQtGate", "Subida", None))
        self.l_channel_7.setText(_translate("PyQtGate", "segundos", None))
        self.lE_time_6.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Tempo de disparo</p></body></html>", None))
        self.lE_time_6.setText(_translate("PyQtGate", "0", None))
        self.lE_time_2.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Tempo de disparo</p></body></html>", None))
        self.lE_time_2.setText(_translate("PyQtGate", "0", None))
        self.cB_descida_1.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Marca os tempos de disparo na descida em relação à referência</p></body></html>", None))
        self.cB_descida_1.setText(_translate("PyQtGate", "Descida", None))
        self.lE_time_4.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Tempo de disparo</p></body></html>", None))
        self.lE_time_4.setText(_translate("PyQtGate", "0", None))
        self.tab_views.setTabText(self.tab_views.indexOf(self.tab_separados), _translate("PyQtGate", "Separados", None))
        self.pW_all.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Gráfico de amostragem dos seis canais em que a ordenada (restrita ao intervalo de 0 a 1023) é porporcional à voltagem medida nas respectivas portas óticas e a abscissa corresponde ao tempo em segundos.</p></body></html>", None))
        self.tW_timetable.setToolTip(_translate("PyQtGate", "<html><head/><body><p><span style=\" font-weight:400;\">Tabela de tempos (em segundos) de disparo dos canais selecionados. Tempos positivos referem-se à subida e negativos à descida.</span></p></body></html>", None))
        self.pB_timetable.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Gera tabela de tempos de disparo na subida e/ou descida conforme os níveis de referência de cada canal</p></body></html>", None))
        self.pB_timetable.setText(_translate("PyQtGate", "Gerar tempos", None))
        self.tab_views.setTabText(self.tab_views.indexOf(self.tab_juntos), _translate("PyQtGate", "Juntos", None))
        self.cB_constrain.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Vincula os controles de referência ao canal 1</p></body></html>", None))
        self.cB_constrain.setText(_translate("PyQtGate", "Vincular ao canal 1", None))
        self.cB_channel_1.setText(_translate("PyQtGate", "Canal 1", None))
        self.cB_channel_2.setText(_translate("PyQtGate", "Canal 2", None))
        self.cB_channel_3.setText(_translate("PyQtGate", "Canal 3", None))
        self.cB_channel_4.setText(_translate("PyQtGate", "Canal 4", None))
        self.cB_channel_5.setText(_translate("PyQtGate", "Canal 5", None))
        self.cB_channel_6.setText(_translate("PyQtGate", "Canal 6", None))
        self.label_8.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Atraso adicional entre cada aquisição (0 a 65535 ms)</p></body></html>", None))
        self.label_8.setText(_translate("PyQtGate", "Atraso:", None))
        self.lE_delay.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Atraso adicional entre cada aquisição (0 a 65535 ms)</p></body></html>", None))
        self.lE_delay.setText(_translate("PyQtGate", "0", None))
        self.label_9.setText(_translate("PyQtGate", "ms", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab_mostrador), _translate("PyQtGate", "Mostrador", None))
        self.pB_save.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Salva arquivo com as formas de onda completas de todos os canais</p></body></html>", None))
        self.pB_save.setText(_translate("PyQtGate", "Salvar formas de onda", None))
        self.pB_load.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Lê arquivo com as formas de onda completas</p></body></html>", None))
        self.pB_load.setText(_translate("PyQtGate", "Ler formas de onda", None))
        self.pB_savetime.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Salva arquivo com os tempos de disparo dos canais selecionados de acordo com a tabela de tempos</p></body></html>", None))
        self.pB_savetime.setText(_translate("PyQtGate", "Salvar tabela de tempos", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab_arquivo), _translate("PyQtGate", "Arquivo", None))
        self.pB_connect.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Seleciona automaticamente a porta USB em que a placa Arduino está conectada. É necessário que a Arduino esteja pré-carregada com o código Photogate específico.</p></body></html>", None))
        self.pB_connect.setText(_translate("PyQtGate", "Selecionar porta automaticamente", None))
        self.label_2.setText(_translate("PyQtGate", "Comunicação serial com Arduino", None))
        self.pB_closeconnection.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Interrompa a conexão com a placa Arduino.</p></body></html>", None))
        self.pB_closeconnection.setText(_translate("PyQtGate", "Interromper", None))
        self.label.setText(_translate("PyQtGate", "Selecionar da lista:", None))
        self.cB_port.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Selecione de uma lista a porta USB em que a placa Arduino está conectada. É necessário que a Arduino esteja pré-carregada com o código Photogate específico.</p></body></html>", None))
        self.label_25.setText(_translate("PyQtGate", "Comunicação:", None))
        self.l_commstatus.setText(_translate("PyQtGate", "não iniciada", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab_serial), _translate("PyQtGate", "Serial", None))
        self.l_ufscar.setText(_translate("PyQtGate", "TextLabel", None))
        self.l_cca.setText(_translate("PyQtGate", "TextLabel", None))
        self.label_3.setText(_translate("PyQtGate", "Centro de Ciências Agrárias", None))
        self.textBrowser.setHtml(_translate("PyQtGate", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">PyQtGate</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Last update: Mar 03 2017</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">PyQtGate tem como objetivo oferecer uma interface gráfica para o hardware de portas óticas utilizado nos Laboratórios de Ensino de Física do Centro de Ciências Agrárias da Universidade Federal de São Carlos (CCA-UFSCar).</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">PyQtGate foi desenvolvido em PyQt e deve ser utilizado em conjunto com os hardwares de aquisição do sistema de portas óticas composto por: (i) placa de prototipagem Arduino Uno, (ii) Photogate Shield para Arduino Uno e (iii) conjunto de sensores óticos. A placa Arduino deve ser carregada com o código específico APGate, cuja cópia encontra-se abaixo. Com excessão da placa Arduino, todas as peças de hardware e todos os softwares foram desenvolvidos no CCA-UFSCar.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">O Shield Photogate para Arduino foi desenvolvido usando a ferramenta online para criação de circuitos eletrônicos EasyEDA e encontra-se disponível em: https://easyeda.com</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">João Teles</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">jteles@cca.ufscar.br</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Outubro/2016</span></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/*APGate: Arduino PhotoGate para uso nos dispositivos de portas óticas dos Laboratórios</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">de Ensino de Física do CCA-UFSCar.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Esse codigo deve ser carregado na placa  Arduino UNO que deve operar em conjunto</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">com os hardwares Shield Photogate e sensores óticos. A comunicao deve ser feita com</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">o software PyQtGate.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Joao Teles, jteles@cca.ufscar.br</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Last update: Mar 03 2017</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">--------------------------------</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analog pin 0: canal 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analog pin 1: canal 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analog pin 2: canal 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analog pin 3: canal 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analog pin 4: canal 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Analog pin 5: canal 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*/</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">//Defines for setting and clearing register bits for faster analog readings</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#ifndef cbi</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#define cbi(sfr, bit) (_SFR_BYTE(sfr) &amp;= ~_BV(bit))</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#endif</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#ifndef sbi</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#endif</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">char msg_co[9] = &quot;Photo_co&quot;;    //Signal from pc asking to connect</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">char msg_ok[9] = &quot;Photo_ok&quot;;    //Connection confirmation signal from arduino to pc</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">char msg_st[9] = &quot;Photo_st&quot;;    //Signal from pc confirming sequence start</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">char msg_t[9]  = &quot;01234567&quot;;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">int i, v;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">int y[7];</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">unsigned char a, b;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">unsigned char a3, a2, a1, a0;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">unsigned long t0, t;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">void erase_msg_t(void);</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">void setup() {</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    // set prescale to 16 (128 is the default) for improving analog reading time:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    sbi(ADCSRA,ADPS2) ;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    cbi(ADCSRA,ADPS1) ;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    cbi(ADCSRA,ADPS0) ;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Serial.begin(115200);</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">}</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">void loop() {</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    //Read command message from pc:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    if (Serial.available() &gt; 7)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        for (i = 0; i &lt; 8; i++) msg_t[i] = Serial.read();</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    //Confirmation of pc-arduino communication:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    if (strcmp(msg_t, msg_co) == 0) {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        for (i = 0; i &lt; 8; i++) </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            Serial.write(msg_ok[i]);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    }</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    //Acquisition start:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    if (strcmp(msg_t, msg_st) == 0) {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                while (Serial.available() &lt; 2) {}</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                a = Serial.read();</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                b = Serial.read();</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                v = ((int)a)*256 + ((int)b);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        t0 = micros();</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        while (Serial.available() == 0) {</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            y[0] = analogRead(0);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            y[1] = analogRead(1);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            y[2] = analogRead(2);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            y[3] = analogRead(3);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            y[4] = analogRead(4);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            y[5] = analogRead(5);</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            t = micros()-t0;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            for (i = 0; i &lt; 6; i++) {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                a1 = y[i]/256;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                a0 = y[i]%256;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                Serial.write(a0);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                Serial.write(a1);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            }</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            a3 = t/16777216;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            a2 = (t-a3*16777216)/65536;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            a1 = (t-a3*16777216-a2*65536)/256;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            a0 = t-a3*16777216-a2*65536-a1*256;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            Serial.write(a0);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            Serial.write(a1);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            Serial.write(a2);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            Serial.write(a3);</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                        delay(v);</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        }</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        erase_msg_t();</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    }</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">}</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">void erase_msg_t(void) {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    for (i = 0; i &lt; 8; i++) msg_t[i] = \'9\';</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">}</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab_sobre), _translate("PyQtGate", "Sobre", None))
        self.l_filename.setToolTip(_translate("PyQtGate", "<html><head/><body><p>Último arquivo salvo ou lido. Um asterisco na frente indica que a última aquisição ainda não foi salva.</p></body></html>", None))
        self.l_filename.setText(_translate("PyQtGate", "*Arquivo:", None))

from pyqtgraph import PlotWidget
