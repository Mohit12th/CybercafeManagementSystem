import mysql.connector as a 
con=a.connect(host="localhost",user="root",passwd="1234")
if con.is_connected():
    print("Successfully connected")#to display you are successfully connected.
c=con.cursor()
sql1= "create database if not exists ccms"#Creating Database in case it does not exist
c.execute(sql1)
sql2="use ccms"#Using databse
c.execute(sql2)
sql3="create table if not exists customer(Name varchar(20),Age int,Address varchar(100),Phone_no int(10))"#create table custumer
c.execute(sql3)
sql5="create table if not exists bill(name varchar(20),Time_accessed_in_min int,Total_charges int)"#create table bill
con.commit()
#menu
def main():
    print("1.Add new Customer details")
    print("2.Bill")
    print("3.Customer's detail view")
    print("4.Quit")
    choice=input("Enter your choice:")
    while True:
        if(choice=='1'):
            Custdetail()
        elif(choice=='2'):
            bill_amount()
        elif(choice=='3'):
            search()
        else:
            print(quit)
            break

#to enter custumer detail
def Custdetail():
    name=input("Enter your name")#Custumer name
    age=int(input("Enter your age"))#Custumer age
    address=input("Enter you residential address")#custumer address
    phone_no=int(input("Enter you Phone Number"))#Custumer phone_no
    h="insert into customer values('{}',{},'{}',{})".format(name,age,address,phone_no)
    c.execute(h)
    con.commit()
    print("Thanks for your information")
    main()
    return

def bill_amount():
    name=input("Enter your name :")#Custumer name
    time=int(input("Enter the time you accessed cyber cafe in minutes :"))#Time custumer accessed in cyber cafe in  minutes
    total=time*25#total amount in respect to time custumer accessed in cyber cafe in  minutes
    kg="insert into bill values('{}',{},'{}')".format(name,time,total)
    c.execute(kg)
    con.commit()
    print("Please pay Rs.",total,"in total")
    main()
    return

def search():
    phone_no=input("Enter the phone number of the customer you want to search :")#Custumer phone_no
    mg="select * from customer where Phone_no=" + str(phone_no)
    c.execute(mg)
    data=c.fetchall()
    for row in data:
        print("Name:",row[0])
        print("Age:",row[1])
        print("Address:",row[2])
        print("Phone number:",row[3])
        main()
        return
main()
