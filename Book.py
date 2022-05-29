from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import(connection)
import os
import platform
import mysql.connector
cnx=mysql.connector.connect(host='localhost',user="root",password="mysql_password!",database='library')
cursor=cnx.cursor()

cursor.execute("CREATE TABLE BookRecord(Bno int,Bname char(232),Author char(232),price int,publisher char(232),quantity int,date_of_purchase date)")
cursor.close()
cnx.close()
def clrscreen():
    if platform.system()=="windows":
        print(os.system("cls"))

def display():
    try:
        os.system("cls")
        cnx=mysql.connector.connect(host='localhost',user="root",password="mysql_password!",database='library')
        cursor=cnx.cursor()
        query=("SELECT * FROM BookRecord")
        cursor.execute(query)
        myrecords=cursor.fetchall()
        for x in myrecords:
            print(x)
        for(Bno,Bname,Author,price,publisher,quantity,Date_of_purchase) in cursor:
            print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            print("Book Code:",Bno)
            print("Book Name:",Bname)
            print("Author of Book :",Author)
            print("price of Book:",price)
            print("Publisher:",publisher)
            print("total quantity:",quantity)
            print("purchased on:",Date_of_purchase)
            print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            cursor.close()
            cnx.close()
            print("sucessfully done")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your user name or password")
        elif err.error==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
    else:
        cnx.close()
#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
        
                                                            #INSERT VALUES INTO DATABASES
import mysql.connector
def insertData():
    try:
        cnx=mysql.connector.connect(host='localhost',user="root",password="mysql_password!",database='library')
        cursor=cnx.cursor()
        bno=int(input("ENTER BOOK CODE:"))
        bname=input("ENTER BOOK NAME:")
        Auth=input("ENTER BOOK AUTHOR'S  NAME:")
        price=int(input("ENTER BOOK PRICE:"))
        publisher=input("ENTER PUBLISHER OF BOOK:")
        quantity=int(input("ENTER QUANTITY PURCHASED:"))
        print("ENTER DATE OF PURCHASE(YEAR-MONTH-DATE:)")
        date_of_purchase=str(input("enter date:"))
        data=(bno,bname,Auth,price,publisher,quantity,date_of_purchase)
        Qry=("INSERT INTO BookRecord VALUES(%s,%s,%s, %s,%s,%s, %s)")
        cursor.execute(Qry,data)
        cnx.commit()
    #make sure data is committed to the database cnx.commit()
        cursor.close()
        cnx.close()
        print("record successfully inserted")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your user name or password")
        elif err.error==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
    else:
        cnx.close()

#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
                                                            #DELETE VALUES
def deleteBook():
     try:
        cnx=mysql.connector.connect(host='localhost',user="root",password="mysql_password!",database='library')
        cursor=cnx.cursor()
        bno=int(input("enter book code of book to be deleted from the library:"))
        Qry=("""DELETE FROM BookRecord WHERE Bno=%s""")
        del_rec=(bno,)
        cursor.execute(Qry,del_rec)
        cnx.commit()
    #make sure data is committed to the database cnx.commit()
        cursor.close()
        cnx.close()
        print(cursor.rowcount,"record(s) DELETED SUCCESSFULLY")
     except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your user name or password")
        elif err.error==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
     cnx.close()
        
#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
#SEARCH BOOK RECORDS
     
def SearchBookRec():
    try:
        os.system("cls")
        cnx=mysql.connector.connect(host='localhost',user="root",password="mysql_password!",database='library')
        cursor=cnx.cursor()
        bno=int(input("enter book code of book to be search from the library:"))
        query=("SELECT * FROM BookRecord WHERE Bno=%s")
        srch_rec=(bno,)
        cursor.execute(query,srch_rec)
        print(cursor.fetchall())
        
        cnx.close()
        print("sucessfully done")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your user name or password")
        elif err.error==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            return 1
    else:
        cnx.close()

#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
                                                            #UPDATE BOOK RECORDS

def UpdateBook():
    try:
        cnx=mysql.connector.connect(host='localhost',user="root",password="mysql_password!",database='library')
        cursor=cnx.cursor()
        bno=int(input("enter book code of book to be updated from the library:"))
        query=('SELECT* FROM BookRecord WHERE Bno=%S')
        rec_srch=(bno,)
        print("ENTER NEW DATA")
        bname=input("ENTER BOOK  NAME:")
        Auth=input("ENTER BOOK AUTHOR'S  NAME:")
        price=int(input("ENTER BOOK PRICE:"))
        publisher=input("ENTER PUBLISHER OF BOOK:")
        quantity=int(input("ENTER QUANTITY PURCHASED:"))
        print("ENTER DATE OF PURCHASE(YEAR-MONTH-DATE::)")
        Date_of_purchase=str(input("enter date:"))
        Qry=("UPDATE BookRecord SET bname=%s,Author=%s,price=%s,publisher=%s,quantity=%s,Date_of_purchase=%s where Bno=%s")
        data=(bname,Auth,price,publisher,quantity,Date_of_purchase,bno)
        cursor.execute(Qry,data)
        cnx.commit()
    #make sure data is committed to the database cnx.commit()
        cursor.close()
        cnx.close()
        print(cursor.rowcount,"record(s) UPDATED SUCCESSFULLY")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("something is wrong with your user name or password")
        elif err.error==errorcode.ER_BAD_DB_ERROR:
            print("database does not exist")
        else:
            print(err)
        cnx.close()
        UpdateBook()
        

               
