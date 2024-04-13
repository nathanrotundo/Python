# Define a class named Pet
class Pet:
    # The initializer method to create a new Pet object with kind, breed, and name
    def __init__(self, kind, breed, name):
        # private and specific to each pet
        self.__kind = kind
        self.__breed = breed
        self.__name = name
    # Getter methods 
    def get_kind(self):
        return self.__kind
    def get_breed(self):
        return self.__breed
    def get_name(self):
        return self.__name
    # Setter methods 
    def set_kind(self, kind):
        self.__kind = kind 
    def set_breed(self, breed):
        self.__breed = breed
    def set_name(self, name):
        self.__name = name
    # Prints pet details.
    def print_pet_details(self):
        print("Pet Details:", vars(self))
    def print_info(self):
           print(f"{self.get_kind()} {self.get_breed()}\n{self.get_name()}")

def main():
    # Create three Pet objects with example data.
    pet = Pet("Dog", "Golden Retreiver", "Elsa")
    pet.print_pet_details()
    # Display the name of the class.
    print(f"Class Name: {Pet.__name__}")
    # Displays the type of object
    print(f"Type of pet: {type(pet)}")
    # Return the module name in which the Pet class is defined.
    print(f"Module Name: {Pet.__module__}")
   
main()
