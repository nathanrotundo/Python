# code to sort a list of ten book titles alphabetically
def main():
    # make a list to store titles
    titles = [] 
    print("Please enter 10 book titles:")
    # while the number of titles is less than 10 the loop will continue 
    while len(titles) < 10:
        title = input(f"Enter title {len(titles) + 1}: ")
        titles.append(title) # adds each title to the list
        if len(titles) > 10:
            break # breaks loop once the user as inputed 10 titles

    # Sort the list of titles alphabetically
    sorted_titles = sorted(titles)

    # Display the sorted titles
    print("Sorted list of book titles:")
    for title in sorted_titles:
        print(title)

main()