import random

database = {}

def init():
    
    print("Welcome to MyBank")


    accountinquiry = int(input("Do you have an Account with us?: 1 (yes) 2 (no)"))

    if(accountinquiry == 1):
        login()
    elif(accountinquiry == 2):
       register()
    else:
        print("Invalid option selected")
        init()

def register():
    print("__Register__")
    email = input("What is your email adress: \n ")
    first_name = input("What is your first name:\n  ")
    last_name = input("What is your last name:\n  ")
    password= input("Create a password \n")

    accountnumber = generateaccountnumber()

    database[accountnumber] = [first_name, last_name, email, password]

    print("Your account has been created")
    print("===== ====== ====== =====")
    print("Your account number is:%d" % accountnumber)
    print("Keep your account number safe")
    print("======= ======== =========")

    login()



def login():
    print("Login to your account")
    database = {}
    useraccountnumber = int(input("What is your account number?: \n"))
    password = input("What is your password?: \n")

    for accountnumber, database in database.items():
        if(accountnumber == useraccountnumber):
            if(userdetails[3] == password):
                bankoperations()
                
        print("Invalid account number or password!")
        login()




def bankoperations():
    print("Welcome %s " % (user[0], user[1]))
    
    option= int(input("What would you like to do?: (1) deposit (2) withdrawal (3) logout (4) exit \n"))
    
    if(option == 1):
        depositoperation()
    
    elif(option == 2):
        Withdrawaloperation()
    
    elif(option == 3):
        logout()

    elif(option == 4):
        exit()
    
    else:
        
        print("Invalid option selected")
        bankoperation(user)

    

def Withdrawaloperation():
    print("Withdrawal")
   

def depositoperation():
    print("Deposit operations")


def generateaccountnumber():

    return random.randrange(1111111111,9999999999)


def logout():
    login()



init()
