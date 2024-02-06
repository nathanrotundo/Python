# Create a list of 20 seats
seats = list(range(1, 21))

# Display the available seats
print("Available seats:", seats[:])
while seats:
    seat_number_input = input("Enter seat number to purchase. Enter '0' to finish: ")
    
    if seat_number_input == '0':
        break

    if seat_number_input.isdigit():
        seat_number = int(seat_number_input)
        
        if 1 <= seat_number <= 20:
            if seat_number in seats:
                seats.remove(seat_number)  # delete purchased seat 
                print(f"Seat {seat_number} has been purchased!")
                print("Available seats:", seats)
           #display when user inputs number already chosen
            else:
                print("Seat already sold, please choose another available seat.")
        #display when user inputs number not between 1-20
        else:
            print("Invalid seat number, select a seat between 1 and 20.")
   # display when user inputs non-numbers
    else:
        print("Invalid input, enter a valid seat number.")
# display when no seats remain
print("All seats have been sold. Thank you!")