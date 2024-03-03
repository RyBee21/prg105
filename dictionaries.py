# Program that display each letter of your word as a Nato term
def main():
    # Nato Dictionary 
    nato_dict = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliet",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-Ray",   
        "Y": "Yankee",
        "Z": "Zulu"
    }
    # Gets word from user
    user_word = input("Please enter a word: ")
    # Convert input word to uppercase 
    user_word = user_word.upper()

        # Iterate through each letter of user word
    for letter in user_word:
        # Check if the letter is in the dictionary
        if letter in nato_dict:
            # Print the corresponding NATO phonetic term
            print(nato_dict[letter])

# Call the function with the user input
main()
