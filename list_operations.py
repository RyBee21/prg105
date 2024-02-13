# Ticket sales

# Seats currently for sale 
seats_available = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

# flag that checks if the shopper is done 
shopping = "None"

# Loops the user a question to see if they want to purchase a seat 
while shopping != "0":
    for seat in seats_available:
        print(seat)

# Promts user to enter their purchase 
    shopping = input("What would you like? type 0 if finished:")
  
# Removes a seat if it has been purchased 
    if shopping in seats_available:
        seats_available.remove(shopping)

# Checks to see if the place is sold out 
    if len(seats_available) == 0:
            print("You are done!") # Lets user know they are done
            shopping = "0" # Exits the program
