import random


number_to_guess = random.randint(1, 100)

print()
ask = input("Do you wish to play 'Guess the number' game (yes or no):").lower()
print()

while True:
    if ask == 'yes':
        try:
            guess = int(input('Guess the number between 1 and 100 : '))

            if guess < number_to_guess:
                print("Too low !")
                print()
            
            elif guess > number_to_guess:
                print("Too High !")
                print()

            else:
                print()
                print("Congratulations, You guessed the right number.")
                break

        except ValueError:
            print()
            print("Please enter a Valid Number.")  

    elif ask == 'no':
        print("Thank You for Playing 😄") 

    else:
        print("Invalid Answer.") 