# Defines the square function which holds its the area 
def square(side):
    sq_area = side * side 
    print(f"The area of the square is {str(sq_area)} square units.")

# Defines the circle function which holds its area
def circle(radius):
    cir_area = 3.14 * radius**2
    print(f"The area of the circle is {str(cir_area)} square units.")

# Calculates the areas 
square(4)
circle(5)
