class Pet:
    # Class variable
    vet_name = "Nates pet hospital"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter and Setter for owner_first_name
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
    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    def set_owner_last_name(self, value):
        self.__owner_last_name = value
    def set_pet_id(self, value):
        self.__pet_id = value
    def set_pet_name(self, value):
        self.__pet_name = value
    def set_pet_type(self, value):
        self.__pet_type = value
    # Method to print student details
    def print_owner_details(self):
        print("Owner details:", vars(self))

    # Method to print basic info about the owner
    def display_pet_info(self):
        print("Pet Information:")
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print("Pet ID:", self.__pet_id)
        print("Pet Name:", self.__pet_name)
        print("Pet Type:", self.__pet_type)
        print("Vet Name:", Pet.vet_name)
        


# Creating pet objects
pet1 = Pet("Bob", "Mick", "6746", "Esla")
pet2 = Pet("Jeff", "cantwell", "1254", "gracie", "Cat")
pet3 = Pet("Nolan", "James", "9878", "Piper", "Bird")

#checking properties
def check_property(pet_obj, prop_name):
    print("pet1 has owner_first_name property")
    print(hasattr(pet1, "__owner_first_name"))
    print("pet1 has owner_last_name property ")
    print(hasattr(pet1, "__owner_last_name"))
# Using setter method for pet1
pet1.set_pet_type("Lizard")

# Displaying pet information
pet1.display_pet_info()
pet2.display_pet_info()
pet3.display_pet_info()




