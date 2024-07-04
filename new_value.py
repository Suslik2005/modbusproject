# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_value.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 344)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;\n"
"")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(11, 11, 461, 321))
        self.frame.setStyleSheet(u"backgorund-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: white;\n"
"padding-left: 10px;\n"
"font-size: 12pt;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.comboBox)

        self.lineEdit_value = QLineEdit(self.frame)
        self.lineEdit_value.setObjectName(u"lineEdit_value")
        self.lineEdit_value.setStyleSheet(u"font-size: 12pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout.addWidget(self.lineEdit_value)

        self.lineEdit_index_1488 = QLineEdit(self.frame)
        self.lineEdit_index_1488.setObjectName(u"lineEdit_index_1488")
        self.lineEdit_index_1488.setStyleSheet(u"font-size: 12pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout.addWidget(self.lineEdit_index_1488)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_valueadd = QPushButton(self.frame)
        self.pushButton_valueadd.setObjectName(u"pushButton_valueadd")
        self.pushButton_valueadd.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.pushButton_valueadd)

        self.pushButton_chten = QPushButton(self.frame)
        self.pushButton_chten.setObjectName(u"pushButton_chten")
        self.pushButton_chten.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.pushButton_chten)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"new_value", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"int16", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"dint32", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"int64", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"uint16", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"udint32", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"uint64", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"float32", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"double64", None))

        self.lineEdit_value.setPlaceholderText(QCoreApplication.translate("Dialog", u"value", None))
        self.lineEdit_index_1488.setText("")
        self.lineEdit_index_1488.setPlaceholderText(QCoreApplication.translate("Dialog", u"index", None))
        self.pushButton_valueadd.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_chten.setText(QCoreApplication.translate("Dialog", u"\u0427\u0442\u0435\u043d\u0438\u0435", None))
    # retranslateUi

