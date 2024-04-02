class Person:
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    # get  methods
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number

    # set methods
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number


# Creating instances
person1 = Person("John Doe", "123 Main St, Manhattan, New York", 30, "123-456-7890")
person2 = Person("Eric Brzegowy", "123 cool street, Algonquin, Illinois", 19, "223-333-4545")
person3 = Person("Charolette Brzegowy", "777 Oak St, Missori, Subway", 20, "777-777-777")

# Displaying data
print("Person 1:")
print("Name:", person1.get_name())
print("Address:", person1.get_address())
print("Age:", person1.get_age())
print("Phone Number:", person1.get_phone_number())
print("\n")

print("Person 2:")
print("Name:", person2.get_name())
print("Address:", person2.get_address())
print("Age:", person2.get_age())
print("Phone Number:", person2.get_phone_number())
print("\n")

print("Person 3:")
print("Name:", person3.get_name())
print("Address:", person3.get_address())
print("Age:", person3.get_age())
print("Phone Number:", person3.get_phone_number())
