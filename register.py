# Theng Rachana.py
al_acc = "Helloworld168@gmail.com"
phone_number = "12345678"
al_pass = "@H123580"
re_account = ""
re_password = ""
username=""
re_phone_number=""
def Login():
    print("Enter account")
    condition = input("Chose option\n1.Enter with email\n2.Enter with Phone number\n ==>")
    if str(condition)=='1':
        account = input("Account:")
        password = input("Password")
        if str(account)==al_acc and str(password)==al_pass:
            print("Thank You")
        elif str(account)!=al_acc and str(password)==password:
            print("Incorrect email or password")
        else:
            if str(account)==str(re_account) and str(password)==str(re_password):
                print("Login Successful")
            elif str(account)!=str(re_account):
                print("Incorrect email")
            elif str(password)!=str(re_password):
                print("Incorrect password")
            else:
                print("Incorrect email or password")
    elif str(condition)=='2':
        phone = input("Phone number:")
        password = input("Password:")
        if str(phone)==phone_number and str(password)==al_pass:
            print("Thank You")
        elif str(phone)==phone_number or str(password)!=al_pass:
            print("Check your phone number or password again")
        else:
            if str(phone) == str(re_phone_number) and str(password) == str(re_password):
                print("Login Successful")
            elif str(phone) != str(re_phone_number):
                print("Incorrect phone number")
            elif str(password) != str(re_password):
                print("Incorrect password")
            else:
                print("Incorrect email or password")
def Register():
    print("Enter Username")
    fname = input("Enter first name:")
    lname = input("Enter last name:")
    username = str(fname + " " + lname)
    re_account = input("Create email:")
    re_password = input("Create password:")
    re_phone_number = input("Enter Phone number:")
    print("Here register successful")
    print("Username:"+username)
    print("Register email:"+re_account)
    print("Register password:"+re_password)
    print("Register phone number:"+re_phone_number)
while True:
    print("1.Login\n2.Register\n3.Exit")
    option = int(input("Choose option:"))
    if option == 1:
        Login()
    elif option == 2:
        Register()
    elif option == 3:
        break
    else:
        print("Invalid option try again")


