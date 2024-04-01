def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                    "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    try:
        index = int(input("Enter the index of the artist you want to replace: "))
        new_artist = input("Enter a new artist name: ")
        top_artists[index] = new_artist
        print("Updated list:", top_artists)
    except ValueError:
        print("please enter a valid number")
    except IndexError:
        print("Please enter a number within the range of artists")
main()