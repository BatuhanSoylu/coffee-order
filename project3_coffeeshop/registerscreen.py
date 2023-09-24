from PyQt5 import QtWidgets,uic
import sys
from coffee_database import *

class Register(QtWidgets.QWidget):
    def __init__(self):
        super(Register, self).__init__()
        uic.loadUi('register.ui',self)
        self.pushButton.clicked.connect(self.register)
    def register(self):
        username=self.lineEdit.text()
        password=self.lineEdit_3.text()
        email=self.lineEdit_2.text()
        phone=self.lineEdit_4.text()
        phone_number=int(phone)
        print(phone_number)
        password_check=self.lineEdit_5.text()
        print(password)
        print(password_check)

        if password_check==password:
            add_person(username,password,email,phone_number)
        else:
            self.label_6.setText("Please try again.")



app= QtWidgets.QApplication(sys.argv)
registerScreen=Register()
registerScreen.show()
app.exec_()

