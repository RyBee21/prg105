def main():
    # Prompting user for date, time, and diary entry
    date_time = input("Enter the current date and time: ")
    entry = input("Enter your diary entry: ")

    # Opening diary.txt file 
    with open('diary.txt', "a") as diary_file:
        # Writing date, time, and entry to the file
        diary_file.write(date_time + "\n")
        diary_file.write(entry + "\n")
        diary_file.write("\n") 

    print("Diary entry recorded successfully.")

if __name__ == "__main__":
    main()
