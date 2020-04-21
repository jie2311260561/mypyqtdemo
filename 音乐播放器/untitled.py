# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 267)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.neme_label = QtWidgets.QLabel(self.centralwidget)
        self.neme_label.setGeometry(QtCore.QRect(90, 50, 61, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.neme_label.setFont(font)
        self.neme_label.setObjectName("neme_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(90, 120, 61, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.name_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_Edit.setGeometry(QtCore.QRect(150, 50, 161, 31))
        self.name_Edit.setObjectName("name_Edit")
        self.pass_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_Edit.setGeometry(QtCore.QRect(150, 120, 161, 31))
        self.pass_Edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_Edit.setObjectName("pass_Edit")
        self.end_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.end_Btn.setGeometry(QtCore.QRect(110, 180, 75, 23))
        self.end_Btn.setObjectName("end_Btn")
        self.exit_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_Btn.setGeometry(QtCore.QRect(250, 180, 75, 23))
        self.exit_Btn.setObjectName("exit_Btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exit_Btn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.neme_label.setText(_translate("MainWindow", "姓名"))
        self.pass_label.setText(_translate("MainWindow", "密码"))
        self.end_Btn.setText(_translate("MainWindow", "登录"))
        self.exit_Btn.setText(_translate("MainWindow", "退出"))
