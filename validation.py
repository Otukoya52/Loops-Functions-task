def have_account_validation(have_account):
    if have_account:
        
        try:
            int(have_account)
            return True

        except ValueError:
            print("Please select option 1 or 2. \n")
            return False

    else:
        print("Please select an option. \n")
        return False

def account_number_validation(account_number):

    if account_number:
        
        try:

            int(account_number)
            
            if len(str(account_number)) == 10:
                return True

        except ValueError:

            return False

        except TypeError:
            
            False

    else:
        print("Account number is a required field! \n")
        return False

def selected_option_validation(selected_option):
    
    if selected_option:
        
        try:
            int(selected_option)
            return True

        except ValueError:
            print("Please select an option from the above \n")
            return False
        
        except TypeError:
            print("Please select an option from the above \n")
            return False

    else:
        print("Please select an option from the above \n")
        return False

def deposit_amount_validation(deposit_amount):

    if deposit_amount:

        try:
            
            int(deposit_amount)
            return True

        except ValueError:

            print("Invalid amount inputted")
            return False

        except TypeError:
            print("Invalid amount inputted")
            return False
            
    else:
        print("Please input an amount to deposit \n")
        return False

def withdraw_amount_validation(withdraw_amount):

    if withdraw_amount:

        try:
            
            int(withdraw_amount)
            return True

        except ValueError:

            print("Invalid amount inputted")
            return False

        except TypeError:
            print("Invalid amount inputted")
            return False
            
    else:
        print("Please input an amount to withdraw \n")
        return False

def other_operations_validation(options):

    if options:

        try:
            
            int(options)
            return True

        except ValueError:

            print("Invalid option selected")
            return False

        except TypeError:
            print("Invalid option selected")
            return False
            
    else:
        print("Please select an option to continue \n")
        return False