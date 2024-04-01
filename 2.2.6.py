def main():
    try:
        # Create a list to store flowers in
        flowers = []
        print("Enter flower names. When you are finished, type 'done'.")
        
        while True:
            flower = input("Enter a flower name: ")
            if flower == "done":
                break  # Breaks the loop once user inputs 'done'
            flowers.append(flower)  # Adds flowers to the empty list
        
        flowers.sort()  # Sorts the list of flowers alphabetically
        print("List of flowers:")
        index = 1
        for flower in flowers:
            print(f"{index}. {flower}")
            index += 1
        
        search = input("Type a flower to search for: ")
        if search in flowers:
            print(f"{search} found in the list.")
        else:
            print(f"{search} not found in the list.")
        
        try:
            number = int(input("Enter number to access the corresponding flower: "))
            if 1 <= number <= len(flowers):  # Check if number is within valid range
                print(f"Flower number {number}: {flowers[number - 1]}")
            else:
                print("You must input a valid number")
        except ValueError:
            print("Oops! Please enter a number.")
    except Exception:
        print("Oops! Looks like an error occurred.")
    
main()