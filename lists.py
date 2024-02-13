# Lists for the days in the week 
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",  "Sunday"]

# Creats empty steps list meant to add the users steps to
steps = []

# Puts the users steps into the steps lists
# Displays the steps taken in each week 

for day in week:
    steps_taken = int(input(f"How many steps did you take on {day}? "))
    steps.append(steps_taken)
    print(f"You took {steps_taken} steps on {day}")

    


# Prints total and average steps taken 
    
print("Total steps taken through the week: "+str(sum(steps)))
print("Average steps taken per day: "+str(sum(steps)/len(week)))


