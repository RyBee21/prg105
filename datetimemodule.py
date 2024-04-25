from datetime import datetime

def main():
    try:

        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        birthday = datetime(birth_year, month, day)
        birth_year = str(birth_year + 10)
        current_date = datetime.now()
        difference = current_date - birthday

        # Calculate the age in years
        age_years = difference.days // 365

        # Calculate the age in months
        age_months = difference.days // 30

        # Calculate the age in weeks
        age_weeks = difference.days // 7

        # Calculate the age in days
        age_days = difference.days

        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 
        print(f"Difference is {age_days} days")
        print(f"You are {age_years:.1f} years old, {age_months:.1f} months old, and {age_weeks:.1f} weeks old.")
        
    except ValueError:
        print("Invalid input. Please enter valid numerical values for year, month, and day.")
        main() 
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()
