# create list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# create empty list
steps = []

# Step 3: User Input
for day in days:
    user_input = int(input(f"How many steps did you take on {day}: "))
    steps.append(user_input)

# Display Daily Steps
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")

# display Total Steps
total_steps = sum(steps)
print(f"Total steps for the week: {total_steps} steps")

# display Average Steps
average = round(total_steps / len(steps))
print(f"Average steps per day: {average} steps")

