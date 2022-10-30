import mysql.connector
import datetime
now = datetime.datetime.now()


def hotel_all():
    while True:
        print("\t\t\t 1. Add New hotel")
        print("\t\t\t 2. List hotel")
        print("\t\t\t 3. Update hotel")
        print("\t\t\t 4. Delete hotel")
        print("\t\t\t 5. Back (Main Menu)")
        p = int(input("\t\t Enter Your Choice :"))
        if p == 1:
            add_hotel()
        if p == 2:
            search_hotel()
        if p == 3:
            update_hotel()
        if p == 4:
            delete_hootel()
        if p == 5:
            break


def review_col():
    while True:
        print("\t\t\t 1. Add review")
        print("\t\t\t 2. List review")
        print("\t\t\t 3. Back (Main Menu)")
        o = int(input("\t\t Enter Your Choice :"))
        if o == 1:
            add_review()
        if o == 2:
            list_review()
        if o == 3:
            break


def hotel_req():
    while True:
        print("\t\t\t 1. Required keyword")
        print("\t\t\t 2. List options")
        print("\t\t\t 3. Back (Main Menu)")
        s = int(input("\t\t Enter Your Choice :"))
        if s == 1:
            req_hotel()
        if s == 2:
            list_req()
        if s == 3:
            break


def user_mgmt():
    while True:
        print("\t\t\t 1. Add user")
        print("\t\t\t 2. List user")
        print("\t\t\t 3. Back (Main Menu)")
        u = int(input("\t\t Enter Your Choice :"))
        if u == 1:
            add_user()
        if u == 2:
            list_user()
        if u == 3:
            break


def create_database():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    print(" Creating HOTEL table")
    sql = "CREATE TABLE if not exists hotel(pcode int(4) PRIMARY KEY,pname char(30) NOT NULL,price float(8,2),pqty int(4),pcat char(30));"
    mycursor.execute(sql)
    print("Creating REVIEW table")
    sql = "CREATE TABLE if not exists review(orderid int(4)PRIMARY KEY,orderdate DATE,pcode char(30) NOT NULL ,pprice float(8,2),pqty int(4),supplier char(50),pcat char(30));"
    mycursor.execute(sql)
    print("REVIEW table created")
    print("Creating REQ table")
    sql = "CREATE TABLE if not exists req(salesid int(4) PRIMARY KEY,salesdate DATE,pcode char(30) references product(pcode),pprice float(8,2),pqty int(4),Total double(8,2));"
    mycursor.execute(sql)
    print("REQ table created")
    sql = "CREATE TABLE if not exists user (uid char(6) PRIMARY KEY,uname char(30) NOT NULL,upwd char(30));"
    mycursor.execute(sql)
    print("USER table created")


def list_database():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    sql = "show tables;"
    mycursor.execute(sql)
    for i in mycursor:
        print(i)


def add_review():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    now = datetime.datetime.now()
    sql = "INSERT INTO review (orderid, orderdate, pcode,pprice, pqty, supplier, pcat) values(%s,%s,%s,%s,%s,%s,%s)"
    code = int(input("Enter hotel code :"))
    oid = now.year+now.month+now.day+now.hour+now.minute+now.second
    qty = int(input("Enter hotel quantity : "))
    price = float(input("Enter hotel unit price: "))
    cat = input("Enter hotel category: ")
    supplier = input("Enter Supplier details: ")
    val = (oid, now, code, price, qty, supplier, cat)
    mycursor.execute(sql, val)
    mydb.commit()


def list_review():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * from review"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t\t REVIEW DETAILS")
    print("-"*85)
    print("orderid date hotel code price quantity supplier category")
    print("-" * 85)
    for i in mycursor:
        print(i[0], "\t", i[1], "\t", i[2], "\t",
              i[3], "\t", i[4], "\t", i[5], "\t", i[6])
    print("-" * 85)


def db_mgmt():
    while True:
        print("\t\t\t 1. Database creation")
        print("\t\t\t 2. List Database")
        print("\t\t\t 3. Back (Main Menu)")
        p = int(input("\t\t Enter Your Choice :"))
        if p == 1:
            create_database()
        if p == 2:
            list_database()
        if p == 3:
            break


def add_hotel():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    sql = "INSERT INTO hotel(pcode,pname,price,pqty,pcat) values (%s,%s,%s,%s,%s)"
    code = int(input("\t\t Enter hotel code :"))
    search = "SELECT count(*) FROM hotel WHERE pcode=%s;"
    val = (code,)
    mycursor.execute(search, val)
    for x in mycursor:
        cnt = x[0]
    if cnt == 0:
        name = input("\t\t Enter hotel name :")
        qty = int(input("\t\t Enter hotel quantity :"))
        price = float(input("\t\t Enter hotel unit price :"))
        cat = input("\t\t Enter hotel category :")
        val = (code, name, price, qty, cat)
        mycursor.execute(sql, val)
        mydb.commit()
    else:
        print("\t\t Hotel already exist")


def update_hotel():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    code = int(input("Enter the hotel code :"))
    qty = int(input("Enter the quantity :"))
    sql = "UPDATE hotel SET pqty=pqty+%s WHERE pcode=%s;"
    val = (qty, code)
    mycursor.execute(sql, val)
    mydb.commit()
    print("\t\t Hotel details updated")


def delete_hotel():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    code = int(input("Enter the hotel code :"))
    sql = "DELETE FROM hotel WHERE pcode = %s;"
    val = (code,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")


def search_hotel():
    while True:
        print("\t\t\t 1. List all hotels")
        print("\t\t\t 2. List hotels code wise")
        print("\t\t\t 3. List hotel category wise")
        print("\t\t\t 4. Back (Main Menu)")
        s = int(input("\t\t Enter Your Choice :"))
        if s == 1:
            list_hotel()
        if s == 2:
            code = int(input(" Enter hotel code :"))
            list_prcode(code)
        if s == 3:
            cat = input("Enter category :")
            list_prcat(cat)
        if s == 4:
            break


def list_hotel():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * from hotel"
    mycursor.execute(sql)
    print("\t\t\t\t HOTEL DETAILS")
    print("\t\t", "-" * 47)
    print("\t\t code name price quantity category")
    print("\t\t", "-" * 47)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])
    print("\t\t", "-" * 47)


def list_prcode(code):
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * from hotel WHERE pcode=%s"
    val = (code,)
    mycursor.execute(sql, val)
    print("\t\t\t\t HOTEL DETAILS")
    print("\t\t", "-" * 47)
    print("\t\t code name price quantity category")
    print("\t\t", "-" * 47)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])
    print("\t\t", "-" * 47)


def sale_hotel():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    pcode = input("Enter hotel code: ")
    sid = int(input("Enter sales id: "))
    sql = "SELECT count(*) from hotel WHERE pcode=%s;"
    val = (pcode,)
    mycursor.execute(sql, val)
    for x in mycursor:
        cnt = x[0]
    if cnt != 0:
        sql = "SELECT * from hotel WHERE pcode=%s;"
        val = (pcode,)
        mycursor.execute(sql, val)
        for x in mycursor:
            print(x)
            price = int(x[2])
            pqty = int(x[3])
        qty = int(input("Enter no of quantity :"))
        if qty <= pqty:
            total = qty * price
            print("Collect Rs. ", total)
            sql = "INSERT into req values(%s,%s,%s,%s,%s,%s)"
            val = (sid, datetime.datetime.now(),
                   pcode, price, qty, total)
            mycursor.execute(sql, val)
            sql = "UPDATE hotel SET pqty=pqty-%s WHERE pcode=%s"
            val = (qty, pcode)
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            print("Quantity not available")
    else:
        print("Hotel is not available")


def list_req():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM req"
    mycursor.execute(sql)
    print("\t\t\t\t REQ DETAILS")
    print("-" * 80)
    print("Sales ID Date hotel Code Price Quantity Total")
    print("-" * 80)
    for x in mycursor:
        print(x[0], "\t", x[1], "\t", x[2], "\t",
              x[3], "\t\t", x[4], "\t\t", x[5])
    print("-" * 80)


def list_prcat(cat):
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="nobita3", database="stock")
    mycursor = mydb.cursor()
    print(cat)
    sql = "SELECT * from hotel WHERE pcat =%s"
    val = (cat,)
    mycursor.execute(sql, val)
    clrscr()
    print("\t\t\t\t HOTEL DETAILS")
    print("\t\t", "-" * 47)
    print("\t\t code name price quantity category")
    print("\t\t", "-" * 47)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])
    print("\t\t", "-" * 47)


def add_user():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    uid = input("Enter emaid id :")
    name = input("Enter Name :")
    password = input("Enter Password :")
    sql = "INSERT INTO user values (%s,%s,%s);"
    val = (uid, name, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "user created")


def list_user():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="nobita3", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT uid, uname from user"
    mycursor.execute(sql)
    clrscr()
    print("\t\t\t\t USER DETAILS")
    print("\t\t", "-" * 27)
    print("\t\t UID name ")
    print("\t\t", "-" * 27)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1])
    print("\t\t", "-" * 27)


def clrscr():
    print("\n"*5)


while True:
    clrscr()
    print("\t\t\t HOTEL REC-SYS")
    print("\t\t\t ****************\n")
    print("\t\t 1. HOTEL MANAGEMENT")
    print("\t\t 2. REVIEW MANAGEMENT")
    print("\t\t 3. REQUIREMENT MANAGEMENT")
    print("\t\t 4. USER MANAGEMENT")
    print("\t\t 5. DATABASE SETUP")
    print("\t\t 6. EXIT\n")
    n = int(input("Enter your choice :"))
    if n == 1:
        hotel_mgmt()
    if n == 2:
        # os.system('cls')
        review_mgmt()
    if n == 3:
        req_mgmt()
    if n == 4:
        user_mgmt()
    if n == 5:
        db_mgmt()
    if n == 6:
        break
