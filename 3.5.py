# Ask user to input 5 names
names_list = []
for _ in range(5):
    name = input("Enter a name: ")
    names_list.append(name)

# Bubble Sort to alphabetically sort the names
n = len(names_list)
for i in range(n):
    for j in range(0, n-i-1):
        if names_list[j] > names_list[j+1]:
            names_list[j], names_list[j+1] = names_list[j+1], names_list[j]

# Reverse the sorted list
names_list.reverse()

# Display the reversed and sorted names
print("Reversed and sorted names:", names_list)

    