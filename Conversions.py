# Variables for kilogram values 

kg_val_1 = 10.50
kg_val_2 = 30.77
kg_val_3 = 68.89
kg_val_4 = 249.11

# Conversion Factor: 1 kg = 2.20462 lb
conversion_factor = 2.20462

# Calculations 
lb_1 = kg_val_1 * conversion_factor
lb_2 = kg_val_2 * conversion_factor
lb_3 = kg_val_3 * conversion_factor
lb_4 = kg_val_4 * conversion_factor

# Output 
print(f"{kg_val_1} kilograms is equal to {lb_1:.2f} pounds.")
print(f"{kg_val_2} kilograms is equal to {lb_2:.2f} pounds.")
print(f"{kg_val_3} kilograms is equal to {lb_3:.2f} pounds.")
print(f"{kg_val_4} kilograms is equal to {lb_4:.2f} pounds.")
