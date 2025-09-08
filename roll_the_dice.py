import random

def one_die():

    d = random.randint(1, 6)

    for x in dice_faces1[d]:
        print(x)
    print()

    print(f'({d})')


def two_dice():

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        for i in dice_faces1[d1]:
            print(i)
        
        for j in dice_faces2[d2]:
            print(j)
        print()

        print(f'({d1}, {d2})')
        print()


dice_faces1 = {
    1: ("---------",
        "|       |",
        "|   ●   |",
        "|       |",
        "---------"),
    2: ("---------",
        "| ●     |",
        "|       |",
        "|     ● |",
        "---------"),
    3: ("---------",
        "| ●     |",
        "|   ●   |",
        "|     ● |",
        "---------"),
    4: ("---------",
        "| ●   ● |",
        "|       |",
        "| ●   ● |",
        "---------"),
    5: ("---------",
        "| ●   ● |",
        "|   ●   |",
        "| ●   ● |",
        "---------"),
    6: ("---------",
        "| ●   ● |",
        "| ●   ● |",
        "| ●   ● |",
        "---------"),
}

dice_faces2 = {
    1: ("---------",
        "|       |",
        "|   ●   |",
        "|       |",
        "---------"),
    2: ("---------",
        "| ●     |",
        "|       |",
        "|     ● |",
        "---------"),
    3: ("---------",
        "| ●     |",
        "|   ●   |",
        "|     ● |",
        "---------"),
    4: ("---------",
        "| ●   ● |",
        "|       |",
        "| ●   ● |",
        "---------"),
    5: ("---------",
        "| ●   ● |",
        "|   ●   |",
        "| ●   ● |",
        "---------"),
    6: ("---------",
        "| ●   ● |",
        "| ●   ● |",
        "| ●   ● |",
        "---------"),
}


print()
print("🎲 Let's Play 🎲")
print()

while True:

    choice = input("Do you wish to Roll the dice ? (yes/no) : ").lower()
    print()

    if choice == 'yes':
        ask = int(input("How many dice you want to play with (1 or 2): "))

        if ask == 1:
            one_die()

        elif ask == 2:
            two_dice()

        else:
            print("PLEASE CHOOSE 1 OR 2 !!")

    elif choice == 'no':
        print("Thank You for Playing 😄")
        print()
        break

    else:
        print("Invalid Choice ☹️")
        print()