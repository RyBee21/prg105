def main():
    total = 0.0
    count = 0

    try:
        with open("sales_totals.txt", "r") as file:
            for line in file:
                try:
                    # Convert each line to a float after stripping newline character
                    value = float(line.strip())
                    total += value
                    count += 1
                    # Formats and displays each number
                    print(f"Number: {value:.2f}")
                except ValueError:
                    print(f"Error: Could not convert '{line.strip()}' to float.")
    except FileNotFoundError:
        print("Error: File 'sales_totals.txt' not found.")
    except IOError:
        print("Error: Unable to read the file.")

    # Calculates and displays the total, count, and average
    if count > 0:
        average = total / count
        print(f"\nTotal: {total:.2f}")
        print(f"Entries: {count}")
        print(f"Average: {average:.2f}")
    else:
        print("\nNo valid numbers found in the file.")

if __name__ == "__main__":
    main()
