# 99 bottles of beer on the wall song
# There are 99 bottles curretly on the wall 

bottles = 99

# While loops that takes the bottles off the wall and passes them around 

while bottles > 2:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        bottles -= 1

# Changes the ending to make it grammatically correct 
        
print("2 bottles of beer on the wall, 2 bottles of beer.")
print("Take one down, pass it around, 1 bottle of beer on the wall.\n")
print("1 bottle of beer on the wall, 1 bottle of beer.")
print("Take one down, pass it around, 1 bottle of beer on the wall.\nNo bottles of beer on the wall!")
