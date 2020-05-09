import random
#staff.txt
#customer.txt
bs=open("staff.txt",'a+')
bc=open("customer.txt",'a+')

def staffLogin():
    print("WELCOME TO SN-BANK LOGIN")
    while True:
        print("\nEnter 'login' to Login\n"
              "Enter 'create' to Register as Staff\n"
              "Enter 'check' to check your account details\n"
              "Enter 'logout' to Close App")
        login = input("Enter option:\n")
        if login == "create":
            name = input("Full Name:")
            bs.write(name)
            bs.write("\n")
            email=input("Email:")
            bs.write(email)
            bs.write("\n")
            username1 = input("Username:")
            bs.write(username1)
            bs.write("\n")
            password = input("password:")
            bs.write(password)
            bs.write("\n")
            bs.close()
            print("Username and Password Saved !!")

        elif login == "login":
            loginusername = input("Enter your username:")
            loginpassword = input("Enter your password")
            fo = open("staff.txt", "r+")
            str = fo.read()
            # Close opened file
            fo.close()

            if loginusername != fo and loginpassword != fo:
                print("incorrect password or username")
                # error message to show, keep trying again
            elif loginusername == fo and loginpassword == fo:
                print("Login Successful")
                # create and store the login session
                # create new bank account
                print("1.Create New Bank Account"
                      "2.Check Your Amount Details")
                option = input()
                if option == "create":
                    AcctName = input("Enter your Account Name:")
                    bc.write(AcctName)
                    bc.write('\n')
                    openningBal = input("Opening Balance:")
                    bc.write(openningBal)
                    bc.write('\n')
                    accttype = input("Your Account Type:")
                    bc.write(accttype)
                    bc.write('\n')
                    acctemail = input("Your Account Email")
                    bc.write(acctemail)
                    bc.write('\n')
                    # generate a random 10 digits acct no. and save it in customer txt file
                    s = "0123456789"
                    password = 10
                    p = "".join(random.sample(s, password))
                    bc.write(p)
                    bc.close()
                    print("Your 10 digit Account Number is:",p)
                # to check users account details
        elif login == "check":
            checkaccountbalance = input("Enter your Account Number:")
                    # fect the users account number and present it
                    # fect the users account balance
            fo = open("customer.txt", "r+")
            str = fo.read()
            print("Your Account Details are : ", str)
            # Close opened file
            fo.close()

        elif login == "logout":
            print("logout")
            exit()

staffLogin()
