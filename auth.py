import random
from datetime import datetime
import validation
import database
from getpass import getpass

def init():

    print("Welcome to BankThemeji \n")

    now = datetime.now()
    thisTime = now.strftime("%a %d-%m-%Y %I:%M:%S %p")
    print('Current Session:', thisTime)
 
    have_account = input("\n Do you have an account with us?:>> \n 1. (Yes) \n 2. (No) \n")
    
    is_valid_have_account = validation.have_account_validation(have_account)
    
    if is_valid_have_account:

        if int(have_account) == 1:
            login()

        elif int(have_account) == 2:
            register()

        else:
            print("You have selected an invalid option \n")
            init()

    else:
        print("You have selected an invalid option \n")
        init()


def login():
    
    print("********** Login **********")
    
    account_number_from_user = input('What is your account number?: \n')
    
    is_valid_account_number = validation.account_number_validation(account_number_from_user)
    
    if is_valid_account_number:
        
        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)
        
        if user:
            bank_operation(user)

        else:
            print ('Invalid Account Number or Password \n')
            login()
    else:
        print("Account number invalid: Account number should be up to 10 digits and only integers")
        init()
    

def register():

    print("********** Register **********")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("create a password for yourself \n")
    account_balance = input("What is your account balance \n")

    account_number = generating_account_number()
    
    is_user_created = database.create(account_number, first_name, last_name, email, password, account_balance)
    
    if is_user_created:

        print("Your Account Has been created")
        print(" === ===== ====== ===== ===")
        print(f"Your account number is: {account_number}")
        print("Make sure you keep it safe")
        print(" === ===== ====== ===== ===")

        login()

    else:
        print("Something went wrong. Please try again")
        register()


def bank_operation(user_details):

    print (f"Welcome {user_details[0], user_details[1]}")

    selected_option = input("What would you like to do? \n 1. Check Balance \n 2. Deposit \n 3. Withdraw \n 4. Logout \n 5. Exit \n")
    
    is_valid_selected_option = validation.selected_option_validation(selected_option)
    
    if is_valid_selected_option:
    
        if int(selected_option) == 1:
            get_current_balance(user_details)

        elif int(selected_option) == 2:
        
            deposit_operation(user_details)

        elif int(selected_option) == 3:
        
            withdrawal_operation(user_details)

        elif int(selected_option) == 4:
        
            logout()
        
        elif int(selected_option) == 5:
        
            exit()

        else:
            print("You have selected an invalid option")
            bank_operation(user_details)
    else:
        bank_operation(user_details)


def get_current_balance(user_details):
    print (f"Your balance is {user_details[4]}")
    other_operations(user_details)


def deposit_operation(user_details):

    deposit_amount = int(input("How much would you like to deposit?: \n"))
    
    is_valid_deposit_amount = validation.deposit_amount_validation(deposit_amount)
    
    if is_valid_deposit_amount:

        user_details[4] += int(deposit_amount)
        print("Deposit Successful!")
        print(f"Your balance is #{user_details[4]}")

    else:
        deposit_operation(user_details)


def withdrawal_operation(user_details):
    print (f"Your balance is {user_details[4]}")
    
    withdraw_amount = input('How much would you like to withdraw?: \n')

    is_valid_withdraw_amount = validation.withdraw_amount_validation(withdraw_amount)
    
    if is_valid_withdraw_amount:

        if int(withdraw_amount) > user_details[4]:

            print (f"You do not have sufficient funds. Your balance is {user_details[4]}")
    
        else:
            user_details[5] -= int(withdraw_amount)
            print("Withdrawal Successful")
            print (f"Your balance is now {user_details[4]}")

        other_operations(user_details)
    
    else:
        withdrawal_operation(user_details)


def other_operations(user_details):
    
    options = input("Would you like to perform another operation? \n 1. Yes \n 2. No \n")
    
    is_valid_options = validation.other_operations_validation(options)
    
    if is_valid_options:

        if int(options) == 1:
        
            bank_operation(user_details)

        elif int(options) == 2:
        
            login()
    
        else:
            print("You have selected an invalid option")
            other_operations(user_details)

    else:
        other_operations(user_details)


def logout():
    login()


def exit():
    init()
    

def generating_account_number():
    return random.randrange(1111111111, 9999999999)


init()