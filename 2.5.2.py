def main():
    try:
        while True:
            # prompt the user the enter password
            password = input("Please enter password:")
            # Checks password is between 8-20 characters
            if 8 <= len(password) <= 20:
                # Checks password has an uppercase letter
                if any(char.isupper() for char in password):
                    # Checks password has a lowercare letter
                    if any(char.islower() for char in password):
                        # Checks password has a number
                        if any(char.isdigit() for char in password):
                             # Checks passwords has a symbol
                            if any(char in "!@#$%&*" for char in password):
                                # promps the user to enter password again if it meets all criteria 
                                confirm_password = input("Please re-enter password to confirm:")
                                if password == confirm_password:
                                    print("Password successfully set!")
                                    break # loop breaks once password is set
                                 # the else statments display a message if the password does not meet a certain criteria 
                                else:
                                    print("Passwords do not match. Please try again.")
                            else:
                                print("Password must contain at least one of these sybols: !@#$%&*")
                        else:
                            print("Password must contain at least one digit")
                    else:
                        print("Password must contain at least one lowercase letter")
                else:
                    print("Password must contain at least one uppercase letter")
            else:
                print("Password must be between 8-20 characters")
    # exept statment handles any other exceptions that could occur
    except ValueError:
        print("An error occurred try again:")

main()