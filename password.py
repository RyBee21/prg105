def main():
    valid = False 
    print("""Password Requirements:\n
    Between 8 to 20 characters long.\n
    Contains at least one uppercase letter.\n
    Contains at least one lowercase letter.\n
    Includes at least one number.\n
    Includes at least one symbol from the set: !@#$%&*\n""")
    while not valid:
        valid = True
        password = input("Please enter a password: ")
        try:
            if len(password) < 8:
                print("password too short")
                valid = False
            elif len(password) > 21:
                print("password too long")
                valid = False
            has_upper = False
            for c in password:
                    if c.isupper():
                        has_upper = True
            if has_upper == False:  
                 print("Please have one upper case letter")   
                 valid = False
            # Lower case
            has_lower = False
            for c in password:
                    if c.islower():
                        has_lower = True    
            if has_lower == False:
                 print("Please have one lower case letter")
                 valid = False
            # Digits
            has_digit = False
            for c in password:
                    if c.isdigit():
                        has_digit = True     
            if has_digit == False:
                 print("Needs digit")
                 valid = False
            # Symbols
            # Checks for symbols 
            has_symbol = False
            symbol = ['!', '@', '#', '$', '%', '&', '*']
            for s in symbol:
                for c in password:
                    if s == c:
                        has_symbol = True          
            if has_symbol == False:
                 print("Needs symbol")
                 valid = False
            if valid == True:
                print("Thank you now please confirm password")
            confirm_password = input("Please confirm password: ")
            if confirm_password == password:
                valid = True
                print("Password has been set")  
            else:
                print("Passwords do not match")
           
        except ValueError:
            print("Value error")

main()
