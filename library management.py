
import mysql.connector

cnx=mysql.connector.connect(host='localhost',user="root",password="mysql_password!")
cursor=cnx.cursor()
query=("CREATE DATABASE library")
cursor.execute(query)


print("\t\t\tproject on LIBRARY MANAGEMET\n")
print("\t\t\t----------------------------------------------\n")
#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
#MODULES USED IN PROJECT
import Menulib
import Book
import issue


#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
while True:
    Book.clrscreen()
    print("\t\t\tLIBRARY MANAGEMENT\n")

    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print("\b1.BOOK MANAGEMENT\b")
    print("\b2.MEMBERS MANAGEMENT\b")
    print("\b3.ISSUE/RETURN BOOK \b")
    print("\b4.EXIT\b")
    choice=int(input("enter choice between 1-4:"))
    if choice==1:
        Menulib.MenuBook()
    elif choice==2:
        Menulib.MenuMember()
    elif choice==3:
        Menulib.MenuIssueReturn()
    elif choice==4:
        break
    else: 
        print("wrong choice....enter ur choice again")
        x=input("enter any key to continueY/N:")
        
#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"

