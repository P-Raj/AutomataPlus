# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutomataInterface.ui'
#
# Created: Sun Jan 30 19:21:00 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(721, 471)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Images/AutPlusLogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.OptionBox = QtGui.QGroupBox(self.centralwidget)
        self.OptionBox.setGeometry(QtCore.QRect(10, 10, 701, 371))
        self.OptionBox.setObjectName(_fromUtf8("OptionBox"))
        self.AutButton = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton.setGeometry(QtCore.QRect(10, 20, 201, 51))
        self.AutButton.setStyleSheet(_fromUtf8(""))
        self.AutButton.setObjectName(_fromUtf8("AutButton"))
        self.GrButton = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton.setGeometry(QtCore.QRect(250, 20, 191, 51))
        self.GrButton.setObjectName(_fromUtf8("GrButton"))
        self.line = QtGui.QFrame(self.OptionBox)
        self.line.setGeometry(QtCore.QRect(10, 70, 681, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.OptionBox)
        self.line_2.setGeometry(QtCore.QRect(200, 20, 61, 51))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_5 = QtGui.QFrame(self.OptionBox)
        self.line_5.setGeometry(QtCore.QRect(430, 20, 61, 51))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.GrButton_3 = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton_3.setGeometry(QtCore.QRect(480, 20, 191, 51))
        self.GrButton_3.setObjectName(_fromUtf8("GrButton_3"))
        self.line_4 = QtGui.QFrame(self.OptionBox)
        self.line_4.setGeometry(QtCore.QRect(10, 140, 681, 21))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.GrButton_4 = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton_4.setGeometry(QtCore.QRect(480, 90, 191, 51))
        self.GrButton_4.setObjectName(_fromUtf8("GrButton_4"))
        self.line_6 = QtGui.QFrame(self.OptionBox)
        self.line_6.setGeometry(QtCore.QRect(430, 90, 61, 51))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_3 = QtGui.QFrame(self.OptionBox)
        self.line_3.setGeometry(QtCore.QRect(200, 90, 61, 51))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.AutButton_2 = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton_2.setGeometry(QtCore.QRect(10, 90, 201, 51))
        self.AutButton_2.setStyleSheet(_fromUtf8(""))
        self.AutButton_2.setObjectName(_fromUtf8("AutButton_2"))
        self.GrButton_2 = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton_2.setGeometry(QtCore.QRect(250, 90, 191, 51))
        self.GrButton_2.setObjectName(_fromUtf8("GrButton_2"))
        self.line_9 = QtGui.QFrame(self.OptionBox)
        self.line_9.setGeometry(QtCore.QRect(10, 210, 681, 21))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.line_7 = QtGui.QFrame(self.OptionBox)
        self.line_7.setGeometry(QtCore.QRect(200, 160, 61, 51))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.AutButton_3 = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton_3.setGeometry(QtCore.QRect(10, 160, 201, 51))
        self.AutButton_3.setStyleSheet(_fromUtf8(""))
        self.AutButton_3.setObjectName(_fromUtf8("AutButton_3"))
        self.GrButton_5 = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton_5.setGeometry(QtCore.QRect(480, 160, 191, 51))
        self.GrButton_5.setObjectName(_fromUtf8("GrButton_5"))
        self.GrButton_6 = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton_6.setGeometry(QtCore.QRect(250, 160, 191, 51))
        self.GrButton_6.setObjectName(_fromUtf8("GrButton_6"))
        self.line_8 = QtGui.QFrame(self.OptionBox)
        self.line_8.setGeometry(QtCore.QRect(430, 160, 61, 51))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.GrButton_7 = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton_7.setGeometry(QtCore.QRect(480, 230, 191, 51))
        self.GrButton_7.setObjectName(_fromUtf8("GrButton_7"))
        self.line_10 = QtGui.QFrame(self.OptionBox)
        self.line_10.setGeometry(QtCore.QRect(200, 230, 61, 51))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.GrButton_8 = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton_8.setGeometry(QtCore.QRect(250, 230, 191, 51))
        self.GrButton_8.setObjectName(_fromUtf8("GrButton_8"))
        self.line_11 = QtGui.QFrame(self.OptionBox)
        self.line_11.setGeometry(QtCore.QRect(430, 230, 61, 51))
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.AutButton_4 = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton_4.setGeometry(QtCore.QRect(10, 230, 201, 51))
        self.AutButton_4.setStyleSheet(_fromUtf8(""))
        self.AutButton_4.setObjectName(_fromUtf8("AutButton_4"))
        self.line_12 = QtGui.QFrame(self.OptionBox)
        self.line_12.setGeometry(QtCore.QRect(10, 280, 681, 21))
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.line_15 = QtGui.QFrame(self.OptionBox)
        self.line_15.setGeometry(QtCore.QRect(10, 350, 681, 21))
        self.line_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.line_14 = QtGui.QFrame(self.OptionBox)
        self.line_14.setGeometry(QtCore.QRect(430, 300, 61, 51))
        self.line_14.setFrameShape(QtGui.QFrame.VLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.AutButton_5 = QtGui.QCommandLinkButton(self.OptionBox)
        self.AutButton_5.setGeometry(QtCore.QRect(10, 300, 201, 51))
        self.AutButton_5.setStyleSheet(_fromUtf8(""))
        self.AutButton_5.setObjectName(_fromUtf8("AutButton_5"))
        self.line_13 = QtGui.QFrame(self.OptionBox)
        self.line_13.setGeometry(QtCore.QRect(200, 300, 61, 51))
        self.line_13.setFrameShape(QtGui.QFrame.VLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.GrButton_9 = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton_9.setGeometry(QtCore.QRect(480, 300, 191, 51))
        self.GrButton_9.setObjectName(_fromUtf8("GrButton_9"))
        self.GrButton_10 = QtGui.QCommandLinkButton(self.OptionBox)
        self.GrButton_10.setGeometry(QtCore.QRect(250, 300, 191, 51))
        self.GrButton_10.setObjectName(_fromUtf8("GrButton_10"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 400, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line_17 = QtGui.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(0, 390, 720, 3))
        self.line_17.setFrameShape(QtGui.QFrame.HLine)
        self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_17.setObjectName(_fromUtf8("line_17"))
        self.line_16 = QtGui.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(80, 400, 3, 30))
        self.line_16.setFrameShape(QtGui.QFrame.VLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.MoreButton = QtGui.QPushButton(self.centralwidget)
        self.MoreButton.setGeometry(QtCore.QRect(90, 400, 50, 30))
        self.MoreButton.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);"))
        self.MoreButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/MoreInfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MoreButton.setIcon(icon1)
        self.MoreButton.setIconSize(QtCore.QSize(25, 25))
        self.MoreButton.setObjectName(_fromUtf8("MoreButton"))
        self.HelpButton = QtGui.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(20, 400, 50, 30))
        self.HelpButton.setStyleSheet(_fromUtf8("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 127);"))
        self.HelpButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HelpButton.setIcon(icon2)
        self.HelpButton.setIconSize(QtCore.QSize(44, 26))
        self.HelpButton.setObjectName(_fromUtf8("HelpButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Automata+ : Automata Operations", None, QtGui.QApplication.UnicodeUTF8))
        self.OptionBox.setTitle(QtGui.QApplication.translate("MainWindow", "SELECT AN OPTION", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton.setText(QtGui.QApplication.translate("MainWindow", "DETECT\n"
"NON-DETERMINISM", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton.setText(QtGui.QApplication.translate("MainWindow", "DETECT\n"
"EPSILON-TRANSITION", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton_3.setText(QtGui.QApplication.translate("MainWindow", "COMPLEMENT \n"
"OF AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton_4.setText(QtGui.QApplication.translate("MainWindow", "MINIMISE DFA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_2.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_2.setText(QtGui.QApplication.translate("MainWindow", "REVERSAL OF\n"
"AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton_2.setText(QtGui.QApplication.translate("MainWindow", "DFA TO GRAMMAR", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_3.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_3.setText(QtGui.QApplication.translate("MainWindow", "EQUIVALENCE OF \n"
"TWO  DFA\'S", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton_5.setText(QtGui.QApplication.translate("MainWindow", "NFA TO DFA", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton_6.setText(QtGui.QApplication.translate("MainWindow", "PRODUCT AUTOMATA\n"
"OF TWO DFA\'S", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton_7.setText(QtGui.QApplication.translate("MainWindow", "DFA TO REGULAR\n"
"EXPRESSION", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton_8.setText(QtGui.QApplication.translate("MainWindow", "WORD-ACCEPTANCE\n"
"ONE BY ONE (DFA)", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_4.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_4.setText(QtGui.QApplication.translate("MainWindow", "WORD-ACCEPTANCE \n"
"IN ONE GO(DFA)", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_5.setToolTip(QtGui.QApplication.translate("MainWindow", "AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.AutButton_5.setText(QtGui.QApplication.translate("MainWindow", "CHECK ACCEPTANCE\n"
"OF EMPTY LANGUAGE", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton_9.setText(QtGui.QApplication.translate("MainWindow", "VIEW\n"
"THE AUTOMATA", None, QtGui.QApplication.UnicodeUTF8))
        self.GrButton_10.setText(QtGui.QApplication.translate("MainWindow", "REMOVE USELESS\n"
"STATES", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "< Back", None, QtGui.QApplication.UnicodeUTF8))

import MoreInfoIcon_rc
import HelpIcon_rc
