#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
                                                                #python module:member1
                                                                 #USING MYSQL CONNECTOR WITH PYTHON

import mysql.connector
from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import(connection)
import os

cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
cursor=cnx.cursor()

cursor.execute("CREATE TABLE MemberRecord(Bno int,Mname char(232),MOB varchar(100),Date_of_membership date,ADR char(232))")
cursor.close()
cnx.close()
def clrscreen():
    print('\n'*5)

def display():
    try:
         os.system('cls')
         cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
         cursor=cnx.cursor()
         query=("SELECT *FROM MemberRecord")
         cursor.execute(query)
         myrecord=cursor.fetchall()
         for x in myrecord:
             print(x)
         for(Bno,Mname,MOB,Date_of_membership,ADR) in cursor:
             print("member code:",Bno)
             print("member name:",Mname)
             print("Mobile Number Of member:",MOB)
             print("Date Of membership:",Date_of_membership)
             print("Address:",ADR)
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

import mysql.connector
def insertData():
    try:
        cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
        cursor=cnx.cursor()
        bno=int(input("member code:"))
        mname=input("member name:")
        mob=int(input("Mobile Number Of member:"))
        print("ENTER DATE OF MEMBER-SHIP(YEAR-MONTH-DATE:)")
        Date_of_membership=str(input("Date Of membership:"))
        ADR=input("Address:")
        data=(bno,mname,mob,Date_of_membership,ADR)
        Qry=("INSERT INTO MemberRecord VALUES(%s,%s,%s,%s,%s)")
        cursor.execute(Qry,data)
        cnx.commit()
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

import mysql.connector                                                           
def delete_Member():
    try:
        cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
        cursor=cnx.cursor()
        bno=int(input("enter member code to be deleted from the member:"))
        Qry=("""DELETE FROM MemberRecord WHERE Bno=%s""")
        del_rec=(bno,)
        cursor.execute(Qry,del_rec)
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
        
#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
#SEARCH member1 RECORDS
import mysql.connector
def Search_Member():
    try:
        os.system("cls")
        cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
        cursor=cnx.cursor()
        bno=int(input("enter member Name to be searched from the member:"))
        query=("SELECT * FROM MemberRecord WHERE Bno=%s")
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
            print(err)
    else:
        cnx.close()  

#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"


                             #UPDATE member1 RECORDS

def UpdateMember():
    try:
        cnx=mysql.connector.connect(host='localhost',user="root",password="bittoo123!",database='library')
        cursor=cnx.cursor()
        bno=int(input("enter member code of member to be updated from the member:"))
        query=('SELECT* FROM MemberRecord WHERE Bno=%S')
        rec_srch=(bno,)
        print("ENTER NEW DATA")
        mname=input("ENTER MEMBER NAME:")
        mob=int(input("ENTER MOBILE NUMBER:"))
        print("ENTER DATE OF MEMBERSHIP(YEAR-MONTH-DATE::)")
        Date_of_membership=str(input("enter date:"))
        ADR=str(input("enter address"))
        Qry=("UPDATE MemberRecord SET mname=%s,mob=%s,Date_of_membership=%s,ADR=%s where Bno=%s")
        data=(mname,mob,Date_of_membership,ADR,bno)
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
        Updatemember()
        

               

