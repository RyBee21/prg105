class InvalidInputError(Exception):
    """Custom exception class for invalid input."""


def get_valid_number():
    try:
        number = float(input("Please enter a number: "))
    except ValueError:
        raise InvalidInputError("Invalid input. Please enter a valid number.")
    else:
        return number
    finally:
        print("answer has been submitted")


def main():
    try:
        number = get_valid_number()
    except InvalidInputError as e:
        print(f"Error: {e}")
    else:
        print(f"Input is valid. You entered: {number}")
    finally:
        print("End of program execution.")


if __name__ == "__main__":
    main()
