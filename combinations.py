def two_letter_combinations(characters):
    # Nested loops iterate over each character in the list twice
    for char1 in characters:
        for char2 in characters:
            # two-letter combination
            combination = char1 + char2
            # Yields the combination 
            yield combination

def main():
    # List of characters
    characters = ['a', 'b', 'c',]
    
    # Calls the generator function
    combinations_generator = two_letter_combinations(characters)
    
    # Iterate over the generator to print each combination
    for combination in combinations_generator:
        print(combination)

# Call the main function to execute the program
main()
