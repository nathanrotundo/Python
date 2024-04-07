class Person:
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number
    def get_info(self):
        return f"Name:{self.name}, Adress:{self.address}, Age:{self.age}, Phone Number:{self.phone_number}"
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_age(self):
        return self.age
    def get_phone_number(self):
        return self.phone_number
    def set_name(self, name):
        self.name = name
    def set_address(self, address):
        self.address = address
    def set_age(self, age):
        self.age = age
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number


# Creating instances of the Person class
person1 = Person("Cliff Cantwell", "406 John Ave", 30, "847-345-3453")
person2 = Person("Bob Smith", "125 Center St", 21, "815-132-4456")
person3 = Person("Steve Adams", "456 Green St", 45, "227-555-9002")

# Displays info for each person
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())