import sqlite3
import datetime
import time
import smtplib
import email
data_coffee=sqlite3.connect("coffedata.db")
cursor_coffee=data_coffee.cursor()

cursor_coffee.execute("CREATE TABLE IF NOT EXISTS coffedata(Type_of_coffee TEXT,Size TEXT,Money REAL,Time TEXT)")
cursor_coffee_person=data_coffee.cursor()
cursor_coffee_person.execute("CREATE TABLE IF NOT EXISTS persondatabase(Username TEXT,Password TEXT,Email TEXT,Phone INT)")
data_coffee.commit()
#cursor_coffee_people=data_coffee.cursor()
#cursor_coffee_people.execute("CREATE TABLE IF NOT EXISTS peopledb(Username)")


def add_coffee(coffee_name,money,size):
    timeit = time.time()
    date = str(datetime.datetime.fromtimestamp(timeit).strftime('%Y-%m-%d %H-%M-%S'))

    cursor_coffee.execute("INSERT INTO coffedata(Type_of_coffee,Size,Money,Time) VALUES(?,?,?,?)",(coffee_name,size,money,date))
    data_coffee.commit()

def calculate_money(type):
    cursor_coffee.execute("SELECT * FROM coffedata WHERE Type_of_coffee=? ;",[type])
    data=cursor_coffee.fetchall()
    money=0
    number=0
    for i in data:
        money += float(i[2])
        number+=1

    return money,number
def add_person(username,password,email,phone):
    cursor_coffee_person.execute("INSERT INTO persondatabase(Username,Password,Email,Phone) VALUES(?,?,?,?)",(username,password,email,phone))
    data_coffee.commit()

def read_person(username):
    cursor_coffee_person.execute("SELECT * FROM persondatabase WHERE Username=?;",[username])
    data=cursor_coffee_person.fetchall()
    return data
def email(username,message):
    sender='soylubatuhan13525@gmail.com'
    data=read_person(username)
    receiver=list(data)
    a=[]
    for i in receiver:
        for j in i:
            a.append(j)
    receiver_mail=a[2]
    receiver_mail_2=['{}'.format(receiver_mail)]
    print(1)
    message_2 = """From: From Person <{}>
    To: To Person <{}>
    Subject: Code

    {}.
    """.format(sender,receiver_mail_2,message)
    smtpObj = smtplib.SMTP()
    print(2)
    smtpObj.sendmail(sender, receiver_mail_2, message_2)
    print(3)
    # bır yerde hata verıyor duzgun calısmıyor bu yuzden bakmak lazım


