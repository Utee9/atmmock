import random
from datetime import datetime
now = datetime.now()
dt_date = now.strftime("%B %d, %Y")
dt_time = now.strftime("%H:%M")


allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

 
def account_num_gen():
    print("Generating Account Number: ")
    return random.randrange(2000000001, 2999999999)

def transaction():        
    print("These are the available options: ")
    print('1. Withdraw')
    print('2. Cash Deposit')
    print('3. Complaint')

    selectedOption = int(input("Please select an option: "))

    if(selectedOption == 1):
        print("You selected %s" %selectedOption)
        amount = input("How much would you like to withdraw?: \n")
        print("Take your cash")
        print("Thanks for banking with us")     


    elif(selectedOption == 2):
        print("You selected %s" %selectedOption)
        deposit = int(input("How much would you like to deposit?: \n"))
        print("Your current balance is: %d" %deposit) 
        

    elif(selectedOption == 3):
        print("You selected %s" %selectedOption)
        print("What issue would you like to report? Please type below: ")
        issue = input("> ")
        print("Thank you for contacting us") 
        
    else:
        print("Invalid option selected, please try again")


def register():
    name = input("Please input your name: ")
    email = input("Please input your email: ")
    password = input("Please input your password: ")
    allowedUsers.append(name)
    allowedPassword.append(password)
    print("You're now registered, now you can login")
    account_no = account_num_gen()
    print("Your account number is:", account_no)
    login()

def login():
    name = input("Input your name \n")

    if(name in allowedUsers):
        password = input("Your password? \n")
        userId = allowedUsers.index(name)

        if(password == allowedPassword[userId]):
            print('Welcome %s' %name)
            transaction()
        else:
            print("Password incorrect, please try again")
    else:
        print("Name not found!")
        print("Or would you like to create a new account?")
        prompt = input("1. Yes \n2. No\n")
        if (prompt == "1"):
            register()
        else:
            print("Name not found, please try again")

print("Welcome to MyATM!")
print("Today's date is", dt_date)
print("And the time is", dt_time)

print("\nWhat would you like to do?")
print("1. Create a new account")
print("2. Login")

select_opt = input("Please select an option: ")
if (select_opt == "1"):
    register()
elif (select_opt == "2"):
    login()
else:
    print("Invalid option, please try again")