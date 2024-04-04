class Pet:
    def __init__(self, type, breed, name):
        self.__type = type
        self.__breed = breed
        self.__name = name

    # Get methods
    def get_type(self):
        return self.__type

    def get_breed(self):
        return self.__breed

    def get_name(self):
        return self.__name

    # Set methods
    def set_type(self, type):
        self.__type = type

    def set_breed(self, breed):
        self.__breed = breed

    def set_name(self, name):
        self.__name = name

    def print_details(self):
        print("Pet Details:")
        print("Type:", self.__type)
        print("Breed:", self.__breed)
        print("Name:", self.__name)


# Creating instances of the Pet class
pet1 = Pet("Dog", "Shiba Inu", "Doge")
pet2 = Pet("Cat", "Tabby", "Max")
pet3 = Pet("Bird", "Parrot", "Patty")

# Calling print_details method for each object
pet1.print_details()
print()
pet2.print_details()
print()
pet3.print_details()
print()

# Demonstration of a Special Method or Function

print("Class of pet1 object:", type(pet1))
