from PyQt5 import QtWidgets,uic
import sys
from project3_coffee_shop import milk_coffee,with_filter,only_milk_foam,milk_foam,coffee_base
from coffee_database import add_coffee
'''
class manager(QtWidgets.QWidget):
    def __init__(self):
        super(manager, self).__init__()
        uic.loadUi('manager.ui',self)

'''
class coffee(QtWidgets.QWidget):
    def __init__(self):
        super(coffee, self).__init__()
        uic.loadUi('coffee_gui.ui',self)
        self.pushButton.clicked.connect(self.latte)
        self.pushButton_2.clicked.connect(self.redeye)
        self.pushButton_3.clicked.connect(self.cappucino)
        self.pushButton_4.clicked.connect(self.flat_white)
        self.pushButton_5.clicked.connect(self.cortado)
        self.pushButton_6.clicked.connect(self.blackeye)
        self.pushButton_7.clicked.connect(self.tea)
        self.pushButton_8.clicked.connect(self.americano)
        #self.pushButton_9.clicked.connect(self.total)
        #self.w=None
    '''
        def total(self):
        if self.w is None:
            self.w = Manager_Page()
            self.w.loadData()

        self.w.show()

    '''

    def glass_select(self):
        self.glass_choice=self.comboBox.currentText()
        return self.glass_choice


    def latte(self):
        glass=self.glass_select()
        latte=milk_coffee(glass)
        self.label.setText("Your {} Latte is price : {}".format(glass,latte.moneyy))
        add_coffee('Latte',latte.moneyy,glass)
    def redeye(self):
        red=with_filter(self.glass_select())
        self.label.setText("Your {} Red Eye is price : {}".format(self.glass_select(),red.money))
        add_coffee('Red-Eye',red.money,self.glass_select())

    def cappucino(self):
        cappucino=milk_coffee(self.glass_select())
        self.label.setText("Your {} Cappucino is price : {}".format(self.glass_select(),cappucino.money))
        add_coffee('Cappucino',cappucino.money,self.glass_select())

    def flat_white(self):
        #self.label.setText("Latte {}".format(self.glass_select()))
        flat=milk_foam(self.glass_select())
        self.label.setText("Your {} Flat White price: {}. Thank you.:=)".format(self.glass_select(),flat.money))
        add_coffee('Flat-White',flat.money,self.glass_select())
    def cortado(self):
        cortado=only_milk_foam(self.glass_select())
        self.label.setText("Your {} Cortado is price : {}".format(self.glass_select(),cortado.money))
        add_coffee('Cortado',cortado.money,self.glass_select())

    def blackeye(self):
        glas=self.glass_select()
        black=with_filter(glas)
        black.add_money()
        self.label.setText("Your {} Black Eye is price : {}".format(glas,black.money))
        add_coffee('Black-Eye',black.money,self.glass_select())

    def tea(self):
        tea=10
        if self.glass_select()=="Large":
            tea_money=tea*2
        elif self.glass_select()=="Medium":
            tea_money=tea*1.5
        elif self.glass_select()=="Small":
            tea_money=tea*1
        self.label.setText("Your {} Tea is price : {}".format(self.glass_select(),tea_money))
        add_coffee('Tea',tea_money,self.glass_select())

    def americano(self):
        americano=coffee_base(self.glass_select())
        glas=self.glass_select()
        self.label.setText("Your {} americano is price :{}.".format(glas,americano.glass_money(glas)))
        add_coffee('Americano',americano.money,self.glass_select())

app = QtWidgets.QApplication(sys.argv)
window = coffee()
window.show()
app.exec_()
