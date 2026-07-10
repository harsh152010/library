library=[]
issue_books=[]

def add():
    book=input("Enter book name : ")
    with open("lib.txt","a") as f:
        f.write(book + "\n")
    print("Succesfully added")
def remove():
    library.clear()   # Purani list empty karo

    with open("lib.txt", "r") as a:
        re = a.readlines()

    for i in re:
        library.append(i.strip())

    r = input("Enter book name : ")

    if r in library:
        library.remove(r)
        print("Successfully removed")
    else:
        print("Book does not exist")

    with open("lib.txt", "w") as f:
        for book in library:
            f.write(book + "\n")
    
def search():
    library.clear()
    with open("lib.txt","r")as f:
        src=f.readlines()
        for i in src:
            library.append(i.strip())


    s=input("Enter book name : ")
    if(s in library):
        print("\n Book found")
        print("\nBook name : ",s)
    else:
        print("\nbook does not found")
def show():
        library.clear()
        with open("lib.txt","r") as f:
             read=f.readlines()
             for i in read:
                 library.append(i.strip())
        if len(library) == 0:
           print("No books available")
        else:
           print("\nAvailable Books:")
           for i in range(len(library)):
                 print(i+1, ".", library[i])
def issue():
    library.clear()
    with open("lib.txt","r") as f:
        iss=f.readlines()
        for i in iss:
            library.append(i.strip())
    
    i=input("Enter the book name : ")
    if(i in library):
        library.remove(i)
        issue_books.append(i)
        with open("issue.txt","a") as a:
            a.write(i +"\n")
                

        print("succcesfully issued")
    else:
        print("book not available")
    with open("lib.txt","w") as b:
        for j in library:
            b.write(j + "\n")

def return1():
    issue_books.clear()
    with open("issue.txt","r") as f:
        r=f.readlines()
        for i in r:
            issue_books.append(i.strip())
    rr=input("Enter the book name : ")
    if(rr in issue_books):
        library.append(rr)
        issue_books.remove(rr)
        with open("lib.txt","a") as a:
                a.write(rr +"\n")
        print("successfully returned")
    else:
        print("Book was not issued")
    with open("issue.txt","w") as b:
        for j in issue_books:
            b.write(j + "\n")




while True:
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Show All Books")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    c=int(input("\nEnter your choice : "))
    
    if(c==1):
        add()
    elif(c==2):
        remove()
    elif(c==3):
        search()
    elif(c==4):
        show()
    elif(c==5):
        issue()
    elif(c==6):
        return1()
    elif(c==7):
        exit()
    else:
        print("invalid choice")
    r=input("\nDo you want to continue y/n : ")
    if(r=="y" or r=="Y"):
        continue
    else:
        exit()