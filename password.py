has_upper = False
has_lower = False
has_digit = False
has_symbol = False
password_complete = False

def main():
    global has_upper, has_lower, has_digit, has_symbol, password_complete

    print("""Password Requirements:\n
    Between 8 to 20 characters long.\n
    Contains at least one uppercase letter.\n
    Contains at least one lowercase letter.\n
    Includes at least one number.\n
    Includes at least one symbol from the set: !@#$%&*\n""")

    
    while not password_complete:
        password = input("Please enter a password: ")
        try:
            # Reset flags for each password input
            has_upper = False
            has_lower = False
            has_digit = False
            has_symbol = False

            # We have to see if password meets criteria
            # Starting with the length of password
            if 8 <= len(password) <= 20:

                # Then checks for upper case
                for c in password:
                        if c.isupper():
                            has_upper = True
                            break
                        else: print("please have one upper case letter")
                # Lower case
                for c in password:
                        if c.islower():
                            has_lower = True
                            break
                        else:
                             print("Needs lower case")
                # Digits
                for c in password:
                        if c.isdigit():
                            has_digit = True
                            break
                        else: print("Forgetting a digit")
                # Symbols
                # Checks for symbols 
                has_symbol = False
                symbol = ['!', '@', '#', '$', '%', '&', '*']
                for s in symbol:
                    for c in password:
                        if s == c:
                            has_symbol = True
                            break
                else:
                    print("you need to include a symbol")
                    continue
            else:
                 print("Needs to be between 8-20 chartacters")

            if has_upper and has_lower and has_digit and has_symbol:
                confirm_password = input("Confirm password: ")
                if confirm_password == password:
                    print("Password has been set")
                    password_complete = True
                    break
                else:
                    print("Passwords do not match")
            else: 
                print("Retry and follow criteria")
    
        except ValueError:
            print("Value error")

    main()
