def square_number():
    try:
        number = input("Enter a number to square: ")
        number = int(number)
        squared_number = number ** 2
        print(f"The square of {number} is {squared_number}.")
        
    except ValueError:
        # If a ValueError occurs ask user to enter valid input
        print("Please enter a valid number.")

# Call the function to start the program
square_number()
