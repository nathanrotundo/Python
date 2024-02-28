def factorial(n):
    # factoral for 1 and 0
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)

def main():
    # Input from user
    user_input = input("Enter a non-negative integer number: ")
    
    try:
        # Make input an integer number
        n = int(user_input)
        
        # Check if the input is positive 
        if n >= 0:
            # Calculate factorial and print result
            result = factorial(n)
            print(f"The factorial of {n} is {result}.")
        else:
            print("Please enter a positive integer number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer number.")

if __name__ == "__main__":
    main()