import calendar
from datetime import datetime

def main():
    try:
        # Gets year
        current_year = datetime.now().year

        # Asks the user for birth month
        birth_month = int(input("Enter your birth month (as a number between 1 and 12): "))

        # Validates user input
        if birth_month < 1 or birth_month > 12:
            print("Invalid input. Please enter a number between 1 and 12.")
            return

        # Generates and displays the calendar for the birth month 
        print("\nCalendar for your birth month:\n")
        print(calendar.month(current_year, birth_month))

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    main()
