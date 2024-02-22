#  BMI Calculator 

# Globals: Metric conversions

global KILOGRAM 
KILOGRAM = 0.453592

global METER
METER = 0.0254

# Gathers required imformation: Weight and height 
weight = int(input("What is your current weight in lbs?: "))
height = int(input("What is your height in inches?: (12 inches = 1 foot)") )

# Function that calculates bmi
def calculate_bmi(weight, height):
    # Converts weight from pounds to kilograms & height from inches to meters 
    weight_kg = weight * KILOGRAM
    height_m = height * METER

    bmi = weight_kg / height_m**2
    return calculate_bmi
bmi_calculated = calculate_bmi(weight, height)

# Outputs 
