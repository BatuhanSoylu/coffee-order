from PyQt5 import QtWidgets,uic
import sys
from coffee_database import *


class Manager_Page(QtWidgets.QWidget):
    def __init__(self):
        super(Manager_Page, self).__init__()
        uic.loadUi('manager.ui',self)
        self.loadData()

    def loadData(self):
        coffee=['Latte','Flat-White','Cappucino','Americano','Cortado','Red-Eye','Black-Eye','Tea','Total']
        row=0
        total_money=0
        total_number=0
        self.tableWidget.setRowCount(len(coffee))
        #self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem('{}'.format(Latte[0])))
        #self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem('{}'.format(Latte[1])))
        for i in coffee:
            cof = list(calculate_money('{}'.format(i)))
            total_money+=cof[0]
            total_number+=cof[1]

            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem('{}'.format(cof[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem('{}'.format(cof[1])))
            self.tableWidget.setItem(8, 0, QtWidgets.QTableWidgetItem('{}'.format(total_money)))
            self.tableWidget.setItem(8, 1, QtWidgets.QTableWidgetItem('{}'.format(total_number)))

            row =row+1



app=QtWidgets.QApplication(sys.argv)
manager_window=Manager_Page()
manager_window.show()
app.exec_()