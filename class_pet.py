class Pet:
    vet_name = "Ry Bee's Veterinary Office"  

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Get methods
    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    # Set methods
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name

    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    def display_pet_info(self):
        print(self.__owner_first_name, self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)

def main():
    # Function to check property existence
    def check_property(pet, property_name):
        return hasattr(pet, property_name)


    # Creating pets
    pet1 = Pet("Jackson", "Joe", 1, "Buddy")
    pet2 = Pet("Charolette", "Web", 2, "Tabby", "Cat")
    pet3 = Pet("Barack", "Obama", 3, "Albert", "Raccoon")

    # Using setter method for pet1
    pet1.set_pet_type("Fish")

    # Displaying information for each pet
    pet1.display_pet_info()
    print()

    pet2.display_pet_info()
    print()

    pet3.display_pet_info()
    print()

    # Checking property existence
    print("Checking property existence:")
    print("Owner first name in pet1:", check_property(pet1, "_Pet__owner_first_name"))
    print("Owner last name in pet2:", check_property(pet2, "_Pet__owner_last_name"))
    print("Pet type in pet3:", check_property(pet3, "_Pet__pet_type"))

main()
