# create custom song
def custom_song(star_name, place, feeling, color, verb, sound, other_name, adjective):
    print("\n\n")
    print(f"Twinkle, twinkle, little {star_name},")
    print(f"How I wonder what you are!")
    print(f"Up above the {place} so high,")
    print(f"Like a diamond in the sky.")
    print()
    print(f"Twinkle, twinkle, little {star_name},")
    print(f"How I wonder what you are!")
    print(f"{feeling} like a {color} {verb},")
    print(f"{sound} the world with joy and mirth.")
    print(f"Up above the {place} so high,")
    print(f"Like a diamond in the sky.")
    print()
    print(f"Twinkle, twinkle, little {star_name},")
    print(f"How I wonder what you are!")
    print(f"{other_name} is {adjective} and {color},")
    print(f"{other_name} is my joy and my mirth.")
    print(f"Up above the {place} so high,")
    print(f"Like a diamond in the sky.")
    print()
    print(f"Twinkle, twinkle, little {star_name},")
    print(f"How I wonder what you are!")

# Collect user input
star_name = input("Enter a name for the star: ")
place = input("Enter a place: ")
feeling = input("Enter a feeling: ")
color = input("Enter a color: ")
verb = input("Enter a verb: ")
sound = input("Enter a sound: ")
other_name = input("Enter another name: ")
adjective = input("Enter an adjective: ")

# Call the custom_song function with user inputs
custom_song(star_name, place, feeling, color, verb, sound, other_name, adjective)

