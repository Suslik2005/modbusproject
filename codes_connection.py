import sys

import threading
import PySide6
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from pymodbus.constants import Endian

from main_window import Ui_MainWindow
from new_value import Ui_Dialog
from slave_connection import Ui_Dialog1
from main import User


class Slave(QMainWindow):
    def __init__(self):
        super(Slave, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bruh = None
        self.wo = None
        self.bo = None
        self.IP = None
        self.port = None
        self.counter = 0
        self.dict = {}
        self.revizor_dict = {}
        self.ui.tableWidget_zapis.setColumnCount(3)

        self.ui.pushButton_add.clicked.connect(self.open_new_value)
        self.ui.pushButton_connect.clicked.connect(self.connec)
        if self.bruh != None:
            self.ui.pushButton_disconnect.clicked.connect(self.disc)

    def revizor_vivod(self):
        while True:
            print(self.revizor_dict)
            for i,v in self.revizor_dict.items():
                adress = int(v[1])
                tip = v[3]
                if tip == "int16":
                    r = self.bruh.read_16int(adress)
                elif tip == "dint32":
                    r = self.bruh.read_dint(adress)
                elif tip == "int64":
                    r = self.bruh.read_64int(adress)
                elif tip == "udint32":
                    r = self.bruh.read_udint(adress)
                elif tip == "float32":
                    r = self.bruh.read_float(adress)
                elif tip == "double64":
                    r = self.bruh.read_double(adress)
                elif tip == "uint16":
                    r = self.bruh.read_uint(adress)
                elif tip == "uint64":
                    r = self.bruh.read_64uint(adress)
                print(self.revizor_dict[str(adress)+tip])
                self.revizor_dict[str(adress)+tip] = [self.revizor_dict[str(adress)+tip][0], adress, r, tip]
                self.ui.tableWidget_2.item(int(v[0]), 1).setText(str(v[2]))

    def potok(self, a):
        for i in range(3):
            b = PySide6.QtWidgets.QTableWidgetItem(str(a[i+1]))
            self.ui.tableWidget_2.setItem(self.counter - 1, i, b)
        t1 = threading.Thread(target=self.revizor_vivod, args=(), daemon=True)
        t1.start()
        # t1.join()
    def vivod(self):
        adress = int(self.new_value.lineEdit_index_1488.text())
        tip = self.new_value.comboBox.currentText()
        if adress in self.dict:
            if tip == "int16":
                r = self.bruh.read_16int(adress)
            elif tip == "dint32":
                r = self.bruh.read_dint(adress)
            elif tip == "int64":
                r = self.bruh.read_64int(adress)
            elif tip == "udint32":
                r = self.bruh.read_udint(adress)
            elif tip == "float32":
                r = self.bruh.read_float(adress)
            elif tip == "double64":
                r = self.bruh.read_double(adress)
            elif tip == "uint16":
                r = self.bruh.read_uint(adress)
            elif tip == "uint64":
                r = self.bruh.read_64uint(adress)
            super_id = str(adress)+str(tip)
            if super_id not in self.revizor_dict:
                self.revizor_dict[super_id] = [self.counter, adress, r, tip]
                self.counter+=1
                self.ui.tableWidget_2.setRowCount(self.counter)
                self.potok(self.revizor_dict[super_id])
                self.new_window1.close()


    def connec(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog1()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.pushButton_connection.clicked.connect(self.super_connect)

    def disc(self):
        self.bruh.disconnect()

    def wobo(self, value):
        match value:
            case "1234":
                wo = Endian.Big
                bo = Endian.Big
            case "3412":
                wo = Endian.Big
                bo = Endian.Little
            case "4321":
                wo = Endian.Little
                bo = Endian.Little
            case "2143":
                wo = Endian.Little
                bo = Endian.Big
        return [wo, bo]

    def super_connect(self):
        self.IP = self.ui_window.lineEdit_IP.text()
        wordbyte = self.ui_window.comboBox_2.currentText()
        self.port = self.ui_window.lineEdit_port.text()
        wo = self.wobo(wordbyte)
        self.bo = wo[1]
        self.wo = wo[0]
        print(self.bo, self.wo, wo)
        self.bruh = User(self.wo, self.bo, self.IP, int(self.port))
        self.bruh.connecting()
        self.new_window.close()

    def open_new_value(self):
        self.new_window1 = QtWidgets.QDialog()
        self.new_value = Ui_Dialog()
        self.new_value.setupUi(self.new_window1)
        self.new_window1.show()
        self.new_value.pushButton_valueadd.clicked.connect(self.add_new_value)
        self.new_value.pushButton_chten.clicked.connect(self.vivod)


    def add_new_value(self):
        vaalue = self.new_value.lineEdit_value.text()
        data = self.new_value.comboBox.currentText()
        index = int(self.new_value.lineEdit_index_1488.text())
        if data == "int16":
            self.bruh.write_16int(int(vaalue) , index)
        elif data == "int64":
            self.bruh.write_64int(int(vaalue), index)
        elif data == "dint32":
            self.bruh.write_dint(int(vaalue), index)
        elif data == "udint32":
            self.bruh.write_udint(int(vaalue), index)
        elif data == "float32":
            self.bruh.write_float(float(vaalue), index)
        elif data == "double64":
            self.bruh.write_double(float(vaalue), index)
        elif data == "uint16":
            self.bruh.write_uint(int(vaalue), index)
        elif data == "uint64":
            self.bruh.write_64uint(int(vaalue), index)
        a = [index, vaalue, data]
        self.dict[index] = [vaalue, data]
        self.ui.tableWidget_zapis.setRowCount(len(self.dict))
        print(self.dict)
        for i in range(3):
            b = PySide6.QtWidgets.QTableWidgetItem(str(a[i]))
            self.ui.tableWidget_zapis.setItem(len(self.dict)-1, i, b)
        self.new_window1.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Slave()
    window.show()
    sys.exit(app.exec())


