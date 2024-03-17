# Python program to get a single character from the user and return its ASCII value
def main():
    user_input = input("Enter a character: ")
    #loop to ensure input is only one character
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")
        if len(user_input) == 1:
            ascii_value = ord(user_input)
            #print the ASCII value 
            print(f"The ASCII value of {user_input} is {ascii_value}")
main()

