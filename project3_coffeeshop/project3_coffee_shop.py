class coffee_base():
    double_raise=1.2
    def __init__(self,glass_selection):
        self.money=10
        self.glass_selection=glass_selection

    def add_money(self):
        self.money=self.money*self.double_raise

    def glass_money(self, glass_selection):
        if glass_selection == "Large":
            self.money = self.money * 2
        elif glass_selection == "Medium":
            self.money = self.money * 1.5
        elif glass_selection == "Small":
            self.money = self.money * 1
        return self.money

class milk_coffee(coffee_base):   #latte ,cappucıno
    def __init__(self,glass_selection):
        super(milk_coffee, self).__init__(glass_selection)
        #self.milk_rate=milk_rate
        self.money_milk=10
        self.moneyy=self.money_milk+coffee_base.glass_money(self,glass_selection)


    def add_milk(self,milk_rate,glass_selection):
        self.milk_rate=milk_rate
        #self.money_MİLKK=self.money_milk*(milk_rate*2)
        self.money=self.money_milk+coffee_base.glass_money(self,glass_selection)+int(self.milk_rate*2)
        return self.money


class milk_foam(milk_coffee): #flat white
    def __init__(self,glass_selection):
        super(milk_foam, self).__init__(glass_selection)
        self.money=self.money*1.3
        coffee_base.glass_money(self,glass_selection)


class only_milk_foam(coffee_base): #cortado
    def __init__(self,glass_selection):
        super(only_milk_foam, self).__init__(glass_selection)
        self.money = self.money * 1.2
        coffee_base.glass_money(self,glass_selection)


class with_filter(coffee_base): #redeye blackeye
    def __init__(self,glass_selection):
        super(with_filter, self).__init__(glass_selection)
        self.filter_=10
        if glass_selection == "Large":
            self.add = self.filter_ * 1.4
        elif glass_selection == "Medium":
            self.add = self.filter_ * 1.2
        elif glass_selection == "Small":
            self.add = self.filter_ * 1
        self.money=self.add+coffee_base.glass_money(self,glass_selection)



'''

def glass_choice():
    choice=input("Please select glass dimension\nLarge\nMedium\nSmall\n")
    return choice


print(
    "Welcome:)) Which coffee do you prefer?\n1)Latte\n2)Flat White\n3)Cappucino\n4)Americano\n5)Cortado\n6)RedEye\n7)BlackEye")
select_coffee = input()
if int(select_coffee) == 1:
    choice=input("Do you want to determine the milk rate? Please write 'yes'.")
    if choice=="yes":
        enter = input("Please enter milk raite")
        glas=glass_choice()
        latte = milk_coffee(glas)
        latte.add_milk(enter,glas)
        print(latte.money)
    else:
        latte = milk_coffee(glass_choice())
        print(latte.money)
elif int(select_coffee) == 2:
    flat_white= milk_foam(glass_choice())
    print(flat_white.money)
elif int(select_coffee) == 3:
    cappucino=milk_coffee(glass_choice())
    print(cappucino.money)
elif int(select_coffee) == 4:
    americano=coffee_base(1)
    print(americano.money)
    americano.glass_money(glass_choice())
    print(americano.money)
elif int(select_coffee) == 5:
    cortado=only_milk_foam(glass_choice())
    print(cortado.money)
elif int(select_coffee) == 6:
    red_eye=with_filter(glass_choice())
    print(red_eye.money)
elif int(select_coffee) == 7:
    black_eye=with_filter(glass_choice())
    black_eye.add_money()
    print(black_eye.money)

    

'''