def main():
    # Use the capitalize() method to capitalize the first letter of the string
    # Example: "python" -> "Python"
    string1 = "python"
    result1 = string1.capitalize()
    print(result1)

    # Use the center() method to center the string in a string of specified width
    # Example: "python" -> "  python  "
    string2 = "python"
    result2 = string2.center(10, '*')
    print(result2)

    # Use the endswith() method to check if the string ends with a specified substring
    # Example: Check if "python" ends with "on"
    string3 = "python"
    result3 = string3.endswith("on")
    print(result3)

    # Use the find() method to find the first occurrence of a substring in the string
    # Example: Find the position of "th" in "python"
    string4 = "python"
    result4 = string4.find("th")
    print(result4)

    # Use the isalnum() method to check if all characters in the string are alphanumeric
    # Example: Check if "python3" is alphanumeric
    string5 = "python3"
    result5 = string5.isalnum()
    print(result5)

    # Use the isalpha() method to check if all characters in the string are alphabetic
    # Example: Check if "python" is alphabetic
    string6 = "python"
    result6 = string6.isalpha()
    print(result6)

    # Use the islower() method to check if all characters in the string are lowercase
    # Example: Check if "python" is in lowercase
    string7 = "python"
    result7 = string7.islower()
    print(result7)

    # Use the isspace() method to check if all characters in the string are whitespaces
    # Example: Check if "   " is all whitespace
    string8 = "   "
    result8 = string8.isspace()
    print(result8)

    # Use the isupper() method to check if all characters in the string are uppercase
    # Example: Check if "PYTHON" is in uppercase
    string9 = "PYTHON"
    result9 = string9.isupper()
    print(result9)

    # Use the join() method to join elements of an iterable with the string as the separator
    # Example: Join ["Python", "is", "fun"] with "-" as separator
    iterable1 = ["Python", "is", "fun"]
    separator = "-"
    result10 = separator.join(iterable1)
    print(result10)

    # Use the lower() method to convert all characters in the string to lowercase
    # Example: Convert "PYTHON" to lowercase
    string11 = "PYTHON"
    result11 = string11.lower()
    print(result11)

    # Use the lstrip() method to remove leading characters (spaces by default)
    # Example: Remove leading spaces from "  python"
    string12 = "  python"
    result12 = string12.lstrip()
    print(result12)

    # Use the rstrip() method to remove trailing characters (spaces by default)
    # Example: Remove trailing spaces from "python  "
    string13 = "python  "
    result13 = string13.rstrip()
    print(result13)

    # Use the replace() method to replace all occurrences of a substring with another substring
    # Example: Replace "python" with "snake" in "I love python"
    string14 = "I love python"
    result14 = string14.replace("python", "snake")
    print(result14)

    # Use the rfind() method to find the highest index of a substring
    # Example: Find the highest index of "n" in "python"
    string15 = "python"
    result15 = string15.rfind("n")
    print(result15)

    # Use the split() method to split the string at a specified separator
    # Example: Split "python-is-fun" at "-"
    string16 = "python-is-fun"
    result16 = string16.split("-")
    print(result16)

    # Use the startswith() method to check if the string starts with a specified substring
    # Example: Check if "python" starts with "py"
    string17 = "python"
    result17 = string17.startswith("py")
    print(result17)

    # Use the strip() method to remove both leading and trailing characters (spaces by default)
    # Example: Remove spaces from "  python  "
    string18 = "  python  "
    result18 = string18.strip()
    print(result18)

    # Use the swapcase() method to swap the case of all characters in the string
    # Example: Swap case of "Python"
    string19 = "Python"
    result19 = string19.swapcase()
    print(result19)

    # Use the title() method to convert the first character of each word to uppercase
    # Example: Convert "python is fun" to title case
    string20 = "python is fun"
    result20 = string20.title()
    print(result20)

    # Use the upper() method to convert all characters in the string to uppercase
    # Example: Convert "python" to uppercase
    string21 = "python"
    result21 = string21.upper()
    print(result21)
main()