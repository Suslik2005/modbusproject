# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slave_connection.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        if not Dialog1.objectName():
            Dialog1.setObjectName(u"Dialog1")
        Dialog1.resize(369, 234)
        Dialog1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"backgorund-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit_port = QLineEdit(self.frame)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setStyleSheet(u"font-size: 12pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout_3.addWidget(self.lineEdit_port)

        self.lineEdit_IP = QLineEdit(self.frame)
        self.lineEdit_IP.setObjectName(u"lineEdit_IP")
        self.lineEdit_IP.setStyleSheet(u"font-size: 12pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout_3.addWidget(self.lineEdit_IP)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"color: white;\n"
"padding-left: 10px;\n"
"font-size: 12pt;\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.comboBox_2)

        self.pushButton_connection = QPushButton(self.frame)
        self.pushButton_connection.setObjectName(u"pushButton_connection")
        self.pushButton_connection.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"font-size: 12pt;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50 px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_connection)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog1)

        QMetaObject.connectSlotsByName(Dialog1)
    # setupUi

    def retranslateUi(self, Dialog1):
        Dialog1.setWindowTitle(QCoreApplication.translate("Dialog1", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog1", u"Port, IP adress, word and byte order", None))
        self.lineEdit_port.setText(QCoreApplication.translate("Dialog1", u"502", None))
        self.lineEdit_port.setPlaceholderText(QCoreApplication.translate("Dialog1", u"port", None))
        self.lineEdit_IP.setText(QCoreApplication.translate("Dialog1", u"127.0.0.1", None))
        self.lineEdit_IP.setPlaceholderText(QCoreApplication.translate("Dialog1", u"IP adress", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog1", u"1234", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog1", u"3412", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog1", u"4321", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Dialog1", u"2143", None))

        self.pushButton_connection.setText(QCoreApplication.translate("Dialog1", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
    # retranslateUi

