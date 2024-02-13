# define different parts of day
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# empty list to store heart rate data
heart_rates = []

# User Input for Heart Rate
for time_slot in time_slots:
    heart_rate_str = input(f"Enter your heart rate in BPM in the {time_slot}: ")
    
    # Convert input to an integer number 
    heart_rate = int(heart_rate_str)
    
    # Append a sublist to heart_rates with time slot and heart rate
    heart_rates.append([time_slot, heart_rate])

# Calculate Average Heart Rate
total_heart_rate = 0
for entry in heart_rates:
    total_heart_rate += entry[1]

average_heart_rate = total_heart_rate / len(heart_rates)

# Print the recorded heart rates and the average heart rate
for entry in heart_rates:
    print(f"Your heart rate in the {entry[0]}: {entry[1]} BPM")

print(f"Average heart rate today: {average_heart_rate:.2f} BPM")