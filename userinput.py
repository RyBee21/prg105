# Program that breaks down total budget into 8 different categories

# Asks for users spending in total and in different categories
total_budget = int(input("What is your total budget sir?"))
rent = int(input("What is your monthly rent?"))
utilities = int(input("What is your spending on utilities?"))
groceries = int(input("How much do you spend on groceries?"))
transportation = int(input("Monthly costs on transportation or gas?"))
health_care = int(input("What is your spending on healthcare?"))
personal_care = int(input("What is your spending on personal care?"))
clothing = int(input("How much do you have in your budget for clothing?"))
debt = int(input("How much debt do you have?"))

# Calculates the remaining budget after deducting each category expense
remaining_budget = total_budget - rent - utilities - groceries - transportation - health_care - personal_care - clothing + debt

# Calculates the percent of the remaining budget for each category
pct_rent = (rent / total_budget) * 100
pct_utilities = (utilities / total_budget) * 100
pct_groceries = (groceries / total_budget) * 100
pct_transportation = (transportation / total_budget) * 100
pct_health_care = (health_care / total_budget) * 100
pct_personal_care = (personal_care / total_budget) * 100
pct_clothing = (clothing / total_budget) * 100

# Displays the breakdown
print("Hello user!, here is the breakdown of your budget:\n")
print(f"     Rent: {pct_rent:.2f}%")
print(f"     Utilities: {pct_utilities:.2f}%")
print(f"     Groceries: {pct_groceries:.2f}%")
print(f"     Transportation: {pct_transportation:.2f}%")
print(f"     Health Care: {pct_health_care:.2f}%")
print(f"     Personal Care: {pct_personal_care:.2f}%")
print(f"     Clothing: {pct_clothing:.2f}%")
print(f"     Debt: -{debt}")
print(f"Remaining Budget: {remaining_budget}")
