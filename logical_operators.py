# Input for integers 

a = int(input("What number do you want to start with?"))
b = int(input("What is the second number you want to use?"))

# and operators 

if a > 0 and b > 0:
    print("Both of the numbers is greater than 0: True")
else:
    print("Both of these numbers is greater than 0: False")

if a > 0 and b > 100:
    print("Both of these numbers are greater than 100: True")
else:
    print("Both of these numbers are greater than 100: False")

# or operator 

if a % 2 == 0 or b % 2 == 0:
    print("One of the numbers is even: True")
else:
    print("One of the numbers is even: False ")

if a < 100 or b < 100:
    print("One of these numbers is less than 100: True")
else:
    print("One of these numbers is less than 100: False")

# not operator
if not a == b:
    print("Numbers are equal: False")
else:
    print("They are equal: True")

if not a == 0:
    print("a is equal to 0: False")
else:
    print("a is equal to 0: True")





