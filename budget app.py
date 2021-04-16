class Budget:
    balance = 0

    def __init__ (self,category):
            self.category= category
       

    def Deposit(cls):
        print("How much would you like to deposit?")
        amount = [int(input("Enter Amount: "))]
        print("Deposit Successful!!!")
        balance = amount
        print(f"Balance:{balance}")


    def Withdrawal(cls):
        print("How much would you like to withdraw?")
        amount = int(input("Enter Amount: " ))
        print("Withdrawal successful!!!")
        


    def Transfer(cls):
        print("How much would you like to Transfer?")
        amount= int(input("Enter Amount:  "))
        print("what category would you like to transfer to?")
        Enter_category = input("Enter Category:  ")
        print("Transfer Successful!!!")


    def Check_Balance(cls): 
        print("your balance is: ")
        
  
Food= Budget("food")
Clothing= Budget("clothing")
Entertainment= Budget("Entertainment")

print("WELCOME TO YOUR BUDGET APP")
from datetime import date

today= date.today()
print("Today's date:",today)

from datetime import datetime
now= datetime.now()
current_time = now.strftime("%H:%M+%S")
print("Current Time =",current_time )

print("What category would you like to access?")

print("1 Food")
print("2 Clothing")
print("3 Entertainment")

option = int(input("Enter option:  "))

if option == 1:
    print("What operation would you like to carry out?")
    print("1 Deposit")
    print("2 Withdrawal")
    print("3 Transfer")
    print("4 Check Balance")

    option= int(input("Enter option:  "))

    if option == 1:
        Food.Deposit()

    elif option == 2:
        Food.Withdrawal()

    elif option == 3:
        Food.Transfer()

    elif option== 4:
        Food.Check_Balance()


if option == 2:
    print("What operation would you like to carry out?")
    print("1 Deposit")
    print("2 Withdrawal")
    print("3 Transfer")
    print("4 Check Balance")

    option= int(input("Enter option:  "))

    if option == 1:
        Clothing.Deposit()

    elif option == 2:
        Clothing.Withdrawal()

    elif option == 3:
        Clothing.Transfer()

    elif option == 4:
        Clothing.Check_Balance()


if option == 3:
    print("What operation would you like to carry out?")
    print("1 Deposit")
    print("2 Withdrawal")
    print("3 Transfer")
    print("4 Check Balance")

    option= int(input("Enter option:  "))

    if option == 1:
        Entertainment.Deposit()

    elif option == 2:
        Entertainment.Withdrawal()

    elif option == 3:
        Entertainment.Transfer()

    elif option == 4:
        Entertainment.Check_Balance()
    