import mysql.connector
from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import(connection)
import os
cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
cursor=cnx.cursor()

cursor.execute("CREATE TABLE issue(Bno int,Date_of_purchase date,date_of_return date)")
cursor.close()
cnx.close()
def clrscreen():
    print('\n'*5)

def ShowIssueBooks():
     try:
         os.system('cls')
         cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
         cursor=cnx.cursor()
         query=("SELECT * FROM issue")
         cursor.execute(query)
         myrecord=cursor.fetchall()
         for x in myrecord:
             print(x)
         for(Bno,date_of_issue,date_of_return) in cursor:
             print("Book Code:",Bno)
             print("Date Of Issue:",Date_of_purchase)
             print("Date Of Return:",Date_of_return)
             cursor.close()
             cnx.close()
             print("you have done it")
     except mysql.connector.Error as err:
         if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
             print("something is wrong with your user name or password")
         elif err.error==errorcode.ER_BAD_DB_ERROR:
             print("database does not exist")
         else:
            print(err)
     else:
        cnx.close()
      
    
    
def issueBook():
    try:
        cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
        cursor=cnx.cursor()
        bno=int(input("issue code:"))
        print("ENTER DATE OF PURCHASE(YEAR-MONTH-DATE:)")
        Date_of_purchase=str(input("enter date:"))
        print("ENTER DATE OF RETURN(YEAR-MONTH-DATE:)")
        Date_of_return=str(input("enter date:"))
        data=(bno,Date_of_purchase,Date_of_return)
        Qry=("INSERT INTO issue VALUES(%s,%s,%s)")
        cursor.execute(Qry,data)
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Record Inserted")
    except mysql.connector.Error as err:
         if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
             print("something is wrong with your user name or password")
         elif err.error==errorcode.ER_BAD_DB_ERROR:
             print("database does not exist")
         else:
            print(err)
    else:
        cnx.close()

def returnBook():
    try:
        cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
        cursor=cnx.cursor()
        bno=int(input("enter book code to issue:"))
        Qry=("""DELETE FROM Issue WHERE Bno=%s""")
        data=(bno,)
        cursor.execute(Qry,data)
        cnx.commit()
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
    else:
        cnx.close()
