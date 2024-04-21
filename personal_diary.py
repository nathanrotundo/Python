def main():
    # Prompt the user to enter the current date and time and a journal entry
    date_time = input("Enter the current date and time: ")
    diary_entry = input("Diary entry: ")

    # Open or create a file named diary.txt
    with open("diary.txt", "a") as file:
        # Write the provided date and time into the file
        file.write(date_time)
        file.write("\n")  # Write a blank line after date and time
        # Write the diary entry into the file
        file.write(diary_entry)
        file.write("\n")  # Write a blank line after entry


main()