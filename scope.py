#  BMI Calculator 

# Globals: Metric conversions

global KILOGRAM 
KILOGRAM = 0.453592

global METER
METER = 0.0254

# Gathers required information: Weight and height 
weight = int(input("What is your current weight in lbs?: "))
height = int(input("What is your height in inches?: (12 inches = 1 foot)") )

# Function that calculates bmi
def calculate_bmi(weight, height):
    # Converts weight from pounds to kilograms & height from inches to meters 
    weight_kg = weight * KILOGRAM
    height_m = height * METER

    calculate_bmi = weight_kg / height_m**2
    return calculate_bmi

# Stores the bmi 
bmi_calculated = float(calculate_bmi(weight, height))

# Outputs 

#Prints the calculated BMI
print(bmi_calculated)

# Checks to see where user fits on the BMI and displays 
if bmi_calculated < 18.5:
        print("Your BMI is Underweight.")

elif 18.5 <= bmi_calculated <= 24.9:
        print("Your BMI is at a Healthy Weight")
   
elif 25.0 <= bmi_calculated <= 29.9:
       print("Your BMI is Overweight")

elif bmi_calculated >= 30:
       print("Your BMI is Obese")

else:
       print("Please recheck your entered values")
