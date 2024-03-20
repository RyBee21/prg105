def main():
    # Prompts user to enter flower names
    flower_list = []
    while True:
        flower = input("Enter a flower name (type 'done' to finish): ")
        if flower.lower() == 'done':
            break
        flower_list.append(flower)

    # Sort the flower list
    flower_list.sort()

    # Print the sorted flower list with numbers
    print("Sorted list of flowers:")
    count = 0
    for flower in flower_list:
        count += 1
        print(f"{count}. {flower}")
        

    # searches for a specific flower
    search_flower = input("Enter a flower to search for: ")
    if search_flower in flower_list:
        print(f"{search_flower} is found in the list.")
    else:
        print(f"{search_flower} is not found in the list.")

    # Access by index
    while True:
        try:
            index = int(input("Enter a number to access the corresponding flower: "))
            if 1 <= index <= len(flower_list):
                print(f"Flower at index {index}: {flower_list[index -1]}")
                break
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Index out of range. Please enter a valid index.")
        except:
            print("Error has occured")
main()
