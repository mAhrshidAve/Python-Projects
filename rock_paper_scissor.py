import random

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ['r', 'p', 's']
while True:
    print()
    user_choice = input("Rock, Paper, or Scissors ? (r/p/s):").lower()
    if user_choice not in choices:
        print()
        print("Invalid Choice.")
        continue

    computer_choice = random.choice(choices)

    print()
    print(f'You Chose {emojis[user_choice]}')
    print()
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print()
        print("It's a TIE !")
    elif (
        (user_choice == 'r' and computer_choice == 's') or \
        (user_choice == 's' and computer_choice == 'p') or \
        (user_choice == 'p' and computer_choice == 'r')):
        print()
        print("You Win !!")
    else:
        print()
        print("You Lose !!")

    print()
    should_continue = input("Do you want to Continue ? (yes/no):").lower()

    if should_continue == 'no':
        print()
        print("Thanks for Playing, it was fun !")
        break