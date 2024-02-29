def get_word(nato_alphabet):
    user_word = input("please Enter a word")
    for letter in user_word.upper():
        if letter.isalpha():  # Check if the character is a letter
            print(nato_alphabet.get(letter, letter))  # Print NATO term or the letter itself if not found

def main():
    nato_alphabet = {
        "A": "Aplha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliette",
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
main()
get_word(nato_alphabet)
