
# Function to square a number
def square_number():
 
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    
    except ValueError:
        # Tells user number is not valid
        print("Not a valid number")
       # gives the user another chance to enter a valid number
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    
square_number()
