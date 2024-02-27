# Conversion constants
POUND_TO_KG = 0.453592
INCH_TO_METER = 0.0254

def main():
    # Input
    weight_pounds = get_valid_input("Enter your weight in pounds: ")
    height_inches = get_valid_input("Enter your height in inches: ")

    # Conversion to Metric
    weight_kg = weight_pounds * POUND_TO_KG
    height_meters = height_inches * INCH_TO_METER

    # BMI Calculation
    bmi = calculate_bmi(weight_kg, height_meters)

    # Display results
    print(f"Your BMI is: {bmi:.2f}")
    display_bmi_category(bmi)
# Check for valid numerical inputs
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Input must be a non-negative number.")
            return value
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid numerical value.")
# calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)
# display what BMI category user is in 
def display_bmi_category(bmi):
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You are in the normal weight category.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
# Run the program
if __name__ == "__main__":
    main()


 