# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Kingf\tktt\qtppy\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aa(object):
    def setupUi(self, aa):
        aa.setObjectName("aa")
        aa.resize(384, 251)
        self.centralwidget = QtWidgets.QWidget(aa)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 50, 91, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 190, 51, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 190, 31, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 150, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 180, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 230, 71, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 90, 41, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 90, 41, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 100, 16, 16))
        self.label_3.setObjectName("label_3")
        aa.setCentralWidget(self.centralwidget)

        self.retranslateUi(aa)
        QtCore.QMetaObject.connectSlotsByName(aa)

    def retranslateUi(self, aa):
        _translate = QtCore.QCoreApplication.translate
        aa.setWindowTitle(_translate("aa", "MainWindow"))
        self.textBrowser.setHtml(_translate("aa", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">0</span></p></body></html>"))
        self.lineEdit.setText(_translate("aa", "200"))
        self.label.setText(_translate("aa", "毫秒"))
        self.pushButton.setText(_translate("aa", "滚动抽取"))
        self.pushButton_2.setText(_translate("aa", "随机抽取"))
        self.label_2.setText(_translate("aa", "Made by cJkl"))
        self.lineEdit_2.setToolTip(_translate("aa", "<html><head/><body><p>5555</p></body></html>"))
        self.lineEdit_2.setText(_translate("aa", "1"))
        self.lineEdit_3.setText(_translate("aa", "25"))
        self.label_3.setText(_translate("aa", "~"))
