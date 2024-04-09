class Employee:

    def __init__(self, name, emp_number):
        self.name = name
        self.emp_number = emp_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_emp_number(self):
        return self.emp_number

    def set_emp_number(self, emp_number):
        self.emp_number = emp_number

    def __str__(self):
        return f"Employee Name: {self.name}, Employee Number: {self.emp_number}"


class ProductionWorker(Employee):

    def __init__(self, name, emp_number, shift_number, hourly_rate):
        super().__init__(name, emp_number)
        self.shift_number = shift_number
        self.hourly_rate = hourly_rate

    def get_shift_number(self):
        return self.shift_number

    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def get_hourly_rate(self):
        return self.hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def __str__(self):
        return f"Name: {self.get_name()}, Employee Number: {self.get_emp_number()}, Shift Number: {self.get_shift_number()}, Hourly Pay Rate: {self.get_hourly_rate()}"

def main():

    # Creating an instance of ProductionWorker
    worker = ProductionWorker("", "", 0, 0.0)

     # Prompting the user for data
    name = input("Enter employee name: ")
    emp_number = input("Enter employee number: ")
    shift_number = int(input("Enter shift number (1 for day, 2 for night): "))
    hourly_rate = float(input("Enter hourly pay rate: "))

    # Setting data using object's methods
    worker.set_name(name)
    worker.set_emp_number(emp_number)
    worker.set_shift_number(shift_number)
    worker.set_hourly_rate(hourly_rate)

    # Displaying the data
    print("\nEmployee Information:")
    print(worker)
main()
