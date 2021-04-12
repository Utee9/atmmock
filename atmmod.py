from datetime import datetime
now = datetime.now()
dt_date = now.strftime("%B %d, %Y")
dt_time = now.strftime("%H:%M:%S")

name = input("What is your name? \n")

allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome %s ' %name)
        print("Today's date is: ", dt_date)
        print("And the time is ", dt_time)
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

    else:
        print ('Password incorrect, please try again')

else:

    print("Name not found, please try again")