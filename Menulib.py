
                                                #python module:MENULIB
import Member
import Book
import issue

#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
def MenuBook():
    Book.clrscreen()
    print("\t\t\tBOOK RECORD MANAGEMENT\n")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print("1.ADD BOOK RECORD")
    print("2.DISPLAY BOOK RECORDS")
    print("3.SEARCH BOOK RECORD")
    print("4.DELETE BOOK RECORD")
    print("5.UPDATE BOOK RECORD")
    print("6.RETURN TO MAIN MENU")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    choice=int(input("enter choice between 1-6:"))
    if choice==1:
        Book.insertData()
    elif choice==2:
        Book.display()
    elif choice==3:
        Book.SearchBookRec()
    elif choice==4:
        Book.deleteBook()
    elif choice==5:
        Book.UpdateBook()
    elif choice==6:
        return
    else:
        print("wrong choice....enter ur choice again")
        x=input("enter any key to continueY/N:")
    
#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"

def MenuMember():
    Book.clrscreen()
    print("\t\t\tMEMBER RECORD MANAGEMENT\n")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print("1.ADD MEMBER RECORD")
    print("2.DISPLAY MEMBER RECORDS")
    print("3.SEARCH MEMBER RECORD")
    print("4.DELETE MEMBERRECORD")
    print("5.UPDATE MEMBER RECORD")
    print("6.RETURN TO MAIN MENU")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    choice=int(input("enter choice between 1-6:"))
    if choice==1:
        Member.insertData()
    elif choice==2:
        Member.display()
    elif choice==3:
        Member.Search_Member()
    elif choice==4:
        Member.delete_Member()
    elif choice==5:
        Member.UpdateMember()
    elif choice==6:
        return
    else:
        print("wrong choice....enter ur choice again")
        x=input("enter any key to continueY/N:")
    

#"=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"
def MenuIssueReturn():
    Book.clrscreen()
    print("\t\t\t ISSUE RECORD MANAGEMENT\n")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print("1.ISSUE BOOK")
    print("2.DISPLAY ISSUSED BOOK RECORDS")
    print("3.RETURN ISSUED BOOK ")
    print("4.RETURN TO MAIN MENU")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    choice=int(input("enter choice between 1-4:"))
    if choice==1:
        issue.issueBook()
    elif choice==2:
         issue.ShowIssueBooks()
    elif choice==3:
        issue.returnBook()
    elif choice==4:
         return
    else:
        print("wrong choice....enter ur choice again")
        x=input("enter any key to continueY/N:")

