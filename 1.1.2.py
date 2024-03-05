# Random number guessing program
import random # import the random function
def main():
   random_number = random.randint(1,100)
   # create loop
   while True:
        try:
            user_number = int(input("Guess a number between 1-100: "))
            # prompt when user guesses number while also breaking the loop
            if user_number == random_number:
                print("Nice job, You guessed the correct number.")
                break
            elif abs(random_number - user_number) <= 5:
                print("Very Hot")
            elif abs(random_number - user_number) <= 15:
                print("Hot")
            elif abs(random_number - user_number) <= 25:
                print("Cool") 
            elif user_number < 0:
                print("No numbers less than 1!")
            elif user_number > 100:
                print("No numbers greater than 100!")
            else: print("cold")
         # prompt if user enters somethinf other than number 
        except ValueError:
            print("Enter a valid number between 1-100.")
main()