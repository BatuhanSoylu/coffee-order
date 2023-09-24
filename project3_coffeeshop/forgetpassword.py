from PyQt5 import QtWidgets,uic
import sys
from coffee_database import *
import random
import smtplib

class Forget(QtWidgets.QWidget):
    def __init__(self):
        super(Forget, self).__init__()
        uic.loadUi('forget.ui',self)
        self.pushButton.clicked.connect(self.send_email)
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()

        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()

    def send_email(self):
        pass
        '''
        self.label_5.show()
        self.lineEdit_4.show()
        random_number = random.randint(0, 1000000)
        email('batuhan',random_number)
        
        :return: 
        '''
    # email functıon yaz dagabase dosyasına ve onu cagır
    # butona basılınca diger sayfa cekmeyı yap





app= QtWidgets.QApplication(sys.argv)
forget=Forget()
forget.show()
app.exec_()
