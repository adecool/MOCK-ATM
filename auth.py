import datetime
import random

# variable constant

CHECK_BALANCE = 1
DEPOSIT = 2
WITHDRAWAL = 3
COMPLAINTS = 4
CHANGE_PASSWORD = 5
FIXED = 1
SAVINGS = 2
CURRENT = 3
YES = 1
NO = 2
QUIT = 6
REGISTER = 1
LOGIN = 2


database = {}


def main():
    
    current_time()
    choice = init()

    if choice == 1:
        register()
    elif choice == 2:
        login()
    else:
        print('invalid option')        
        
        
    # Transaction Logic   

    
def Another_Trans():
    print('________________')
    print('1. YES')
    print('2. NO')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < YES or choice > NO:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice              

def init():

    print('Welcome to Python_Bank')
    print()
    print('1. REGISTER')
    print('2. LOGIN')
    print()

    # Get the user's choice.
    haveAccount = int(input('Enter your choice: '))

    # Validate the choice.
    while haveAccount < REGISTER or haveAccount > LOGIN:
        haveAccount = int(input('Enter a valid choice: '))  
    return haveAccount    


def login():
    print('**********Login**************')
 
    accountNumberFromUser = int(input("Enter your account number: "))
    password = input('Enter your secret password: ')

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                Select_Transaction(userDetails)
              
            else: 
                print('Invalid account or password')
                login()
    
      

def register():

    print('*********Register***********')

    first_name = input('What is your first name? ')
    last_name = input('What is your last name? ')
    email = input('Enter your email: ')
    password = input('Enter your secret password: ')

    accountNumber = generateAccountNum()
    
    database[accountNumber] = [first_name, last_name, email, password]

    #store customer data in dict
    
    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")   
    login() 
    return database

    
def Select_Account_Type():
    print()
    print('Select Account Type')
    print('---------------------------')
    print('1. FIXED')
    print('2. SAVINGS')
    print('3. CURRENT')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < FIXED or choice > CURRENT:
        choice = int(input('Enter a valid choice: '))
    return choice 

def generateAccountNum():

    num = random.randint(1111111111, 9999999999)
    return num


       

def current_time():
    x = datetime.datetime.now()
    print(x)  

def changePassword():
    print('####changing password####')
    accountNumberFromUser = int(input("Enter your account number: "))
    password = input('Enter your secret password: ')
    newPassword = input('Enter a new password')

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                userDetails[3] = newPassword
    print(f'Dear Customer your new password is {newPassword}')
    login()


def Select_Transaction(user):
    

    print('Welcome %s %s ' % ( user[0], user[1] ) ) 
    print('Select Transaction Type')
    print('---------------------------')
    print('1. CHECK BALANCE')
    print('2. DEPOSIT')
    print('3. WITHDRAWAL')
    print('4. COMPLAINTS')
    print('5. CHANGE PASSWORD')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < CHECK_BALANCE or choice > CHANGE_PASSWORD:
        choice = int(input('Enter a valid choice: '))

    
    


    
    # a variable constant
    ACC_BALANCE = 2000
    Acct = Select_Account_Type()

    while choice != QUIT:
        if choice == 1:
            print(f'Account Balance: N{ACC_BALANCE}')

        elif choice == 2:
            print('Enter Amount to be deposited')
            DEPOSIT = int(input('Enter Amount: '))
            BALANCE += DEPOSIT
            print(f'Account Balance: N{ACC_BALANCE}')

        elif choice == 3:
            print('Enter Amount to withdraw')
            Withdraw = int(input('Enter Amount: '))
            if ACC_BALANCE < Withdraw:
                print('Sorry Customer')
                print('insufficient balance to complete this transaction')
            else:    
                ACC_BALANCE -= Withdraw
                print('TAKE YOUR CASH')
                print(f'Account Balance: N{ACC_BALANCE}')

        elif choice == 4:
            issues = input('What issue will you like to report?: ')    
            print("Thank you for contacting us") 
        elif choice == 5:
            changePassword()       
        print('Do YOU WANT OT PERFORM ANOTHER TRANSACTION')
        

        another = Another_Trans()
        if another == 1:    
            choice = Select_Transaction()
        else:
            print('_____________________')
            print('Dear Customer....')
            print('Thank you for banking with us')
            choice = QUIT 
main()