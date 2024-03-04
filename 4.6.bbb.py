def  main():
    # Nato Phonetic Alphabet 
    nato_alphabet = {"A": "Alpha", "B": "Bravo","c": "Charlie", "D": "Delta", "E": "Echo"
                 , "f": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett"
                 , "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar"
                 , "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango"
                 , "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"}



            
    # asks user to input a word .upper function to turn all letters to upercase
    user_word = input("Enter a word:").upper() 
        
    for key in user_word:
            # match each letter to its phonetic counterpart 
            if key in nato_alphabet:
                print(nato_alphabet[key])
            # prompt if user inputs something other than a letter
            if key not in nato_alphabet:
                print("only enter letters A-Z")

   

main()