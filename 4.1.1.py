def two_letter_combinations(characters):
    # Generator function to produce all combinations of "x" "y" "z"
    for char in characters:
        for char2 in characters:
            yield char + char2 # Yeild turns funtion into a generator function

def main():
    # List of characters
    characters = ['x', 'y', 'z']

    # Call the generator function and print each combination
    print("All possible two-letter combinations:")
    for characters in two_letter_combinations(characters):
        print(characters)


main()