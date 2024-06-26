import random
users = {}

def create():
    id = random.randint(10000,19999)
    money = int(input("Enter your money: "))
    users[id] = money
    print("Successfully Created Account! Your ID number is ", id)

def check():
    id_no = int(input("Enter your ID Number: "))
    found = False  
    
    for u, b in users.items():
        if u == id_no:
            print("Welcome ID NO.", u , " Your Current Balance is: ", b)
            found = True
            break
    
    if not found:
        print("You are not registered in our bank!")

def deposit():
    id_no = int(input("Enter your ID Number: "))
    dep_ammount = int(input("Enter the money you want to deposit: "))
    for u, b  in users.items():
        if u == id_no:
            new = b + dep_ammount
            if dep_ammount < 0:
                print("You cannot Deposit Negative Numbers!")
                break
            elif dep_ammount > 0:
                users.update({u : new})
                print("Welcome! ID NO.", u , "You have successfully deposited ", dep_ammount , "To your bank account, your new balance is " , new)
                break
        else: 
            print("Sorry, We Couldn't find your account")
            break

def withdraw():
    id_no = int(input("Enter your ID Number: "))
    withdraw_ammount = int(input("Enter the money you want to Withdraw: "))
    for u, b  in users.items():
        if u == id_no:
            new = b - withdraw_ammount
            if b < withdraw_ammount:
                print("Insufficient Funds on your Account!")
                break
            elif b >= withdraw_ammount:
                users.update({u : new})
                print("Welcome! ID NO.", u , "You have successfully withdrew ", withdraw_ammount , "From your bank account, your new balance is " , new)
                break
        else: 
            print("Sorry, We Couldn't find your account")
            break

def delete():
    id_no = int(input("Enter your ID Number: "))
    keys_to_delete = []
    for u in users.keys():
        if u == id_no:
            choice = input("Are you sure you want to delete this account?Yes or No: ")
            choice.lower
            if choice == "yes":
                    keys_to_delete.append(u)
    for u in keys_to_delete:
        del users[u]
        print("Successfully Deleted Account No.", u)
        break

active = True

while active is True:
    print("*********************************************")
    print("*****        WELCOME TO PYBANK         ******")
    print("***** ENTER NO. 1 TO CREATE AN ACCOUNT ******")
    print("***** ENTER NO. 2 TO CHECK YOU BALANCE ******")
    print("*****      ENTER NO. 3 TO DEPOSIT      ******")
    print("*****     ENTER NO. 4 TO WITHDRAW      ******")
    print("***** ENTER NO. 5 TO DELETE AN ACCOUNT ******")
    print("*****        ENTER NO. 6 EXIT          ******")
    choose = int(input("Enter your choice!: "))
    if choose == 1:
        create()
    elif choose == 2:
        check()
    elif choose == 3:
        deposit()
    elif choose == 4:
        withdraw()
    elif choose == 5:
        delete()
    elif choose == 6:
        print(users)
