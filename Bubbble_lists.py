# Program that sorts user generated list with bubble sort

# Accepts 5 names from user and stores it in names list 
names = []
for i in range (1,5):
    names.append(input("What names would you like to write down on the list?"))
print(names)

# Sorts list using  Bubble Sort algorithm 
# Flag to track if a swap has occured 
swapped = True 

# Loops until the list is swapped 
while swapped:
    swapped = False 
    for i in range(len(names - 1)):
        if numbers[i] > numbers[i + 1]:
            swapped = True 
            names[i], names[i + 1] = numbers(i + 1), numbers[i]

# Prints bubble sort algorith output 
print(names)

# Reverses sorted list
names.reverse()

#prints the reveresed list 
print(names)
