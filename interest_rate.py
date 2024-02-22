# Program that caluclate interest


# Defines a function to calculate interest
def calculate_interest(principal_amt, rate, time):
    interest = principal_amt * rate * time / 100
    return interest

# Gathers what the users intial amount is and how long it has been making interest
principal_amt = float(input("Enter the intial amount of money started with: "))
rate = float(input("What is the rate you were given: "))
time = float(input("Enter how long your money has been saved for: "))

# Stores result in result varibale 
result = calculate_interest(principal_amt, rate, time)

# Prints the  gathered information 
print (f"""\nThe simple interest for a principal amount of {principal_amt:,.2f}
at an interest of {rate}%
over a period of {time} years is:
{result:,.2f}""")
       
  
