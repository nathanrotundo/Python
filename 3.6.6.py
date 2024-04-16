class InvalidInputError(Exception):
    # Custom exception implementation
    pass
    def main():
        while True:
            try:
            # Asks user for input
                user_input = input("Enter a number: ")
                if not user_input.isdigit():
                    raise InvalidInputError("Invalid input, enter a number.")
            except Exception as e:
            # Code that runs if an exception occurs
             print(f"An error occurred: {e}")
            else:
            # Confirm valid input
                print("Valid input:", user_input)
                break  # Exits the loop if input is valid
            finally:
            # indicates program has been executed
                print("Program has been executed.")

    main()