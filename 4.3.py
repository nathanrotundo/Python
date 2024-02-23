def calculate_interest(principal, rate, time):
    # Calculate simple interest using the formula
    calculated_interest = (principal * rate * time) / 100
    
    # Print the result in a user-friendly format
    print(f"The simple interest for a principal amount of ${principal:,.2f} \
at an interest rate of {rate}% over a period of {time} years is: ${calculated_interest:,.2f}")
    
    # Return the calculated interest
    return calculated_interest

# Get input from the user
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate as a whole number (5% would be 5): "))
investment_time = int(input("Enter the investment time in whole years: "))

# Call the function with user input
calculate_interest(principal_amount, interest_rate, investment_time)