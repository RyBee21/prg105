def main():
    # Collect book titles
    titles = []
    while len(titles) < 10:
        try:
            title = input("Enter a book title: ").title()
            titles.append(title)
        except ValueError:
            print("Please enter a valid input.")

    # Create a sorted list
    sorted_titles = sorted(titles)

    # Display the titles
    print("Sorted list of book titles:")
    for title in sorted_titles:
        print(title)
main()
