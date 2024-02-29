# Gets word from user
user_word = input("Please enter a word: ")
# Convert input word to lowercase 
user_word = user_word.upper()


# Itterates through each letter and displays its Nato term 
def main(user_word):
    # Nato Dictionary 
    nato_dict = {
        "A": "Aplha",
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
    # Iterate through each letter of users word
    for letter in user_word:
        # Check if the letter is in dictionary
        if letter in nato_dict:
            # Print the corresponding NATO phonetic term
            print(nato_dict[letter])

# Call the function with the user input
main(user_word)
