from PyQt5 import QtWidgets,uic
import sys
from coffee_database import *
from registerscreen import Register
from coffee_gui import coffee
class Login(QtWidgets.QWidget):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('login.ui',self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.register)
        self.pushButton_3.hide()
        self.pushButton_3.clicked.connect(self.otherpage)

    def login(self):

        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        name_pass=read_person(username)

        for i in name_pass:
            j=list(i)
            if j[1]==password:
                print("hello")
                # ui to py file convert for open in the first working

                if self.w.isVisible():
                    self.w.hide()
                self.w.show()
            else:
                self.pushButton_3.show()
                print("try again")
                self.label_5.setText("Try Again.")
    def otherpage(self):
        pass
    def register(self):
        self.w = Register()
        self.w.show()



app= QtWidgets.QApplication(sys.argv)
login=Login()
login.show()
app.exec_()