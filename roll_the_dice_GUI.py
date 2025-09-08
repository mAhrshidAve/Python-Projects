import tkinter as tk
import random

# Dice faces (same as your console version)
dice_faces = {
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

# Function to roll one die
def one_die():
    d = random.randint(1, 6)
    dice_display1.config(text="\n".join(dice_faces[d]))
    dice_display2.config(text="")  # clear second dice
    result_label.config(text=f"Result: ({d})")

# Function to roll two dice
def two_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    dice_display1.config(text="\n".join(dice_faces[d1]))
    dice_display2.config(text="\n".join(dice_faces[d2]))
    result_label.config(text=f"Result: ({d1}, {d2})")

# GUI setup
root = tk.Tk()
root.title("🎲 Roll the Dice 🎲")
root.geometry("400x400")

title_label = tk.Label(root, text="🎲 Let's Play 🎲", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Dice displays
dice_display1 = tk.Label(root, text="", font=("Courier", 14), justify="left")
dice_display1.pack()

dice_display2 = tk.Label(root, text="", font=("Courier", 14), justify="left")
dice_display2.pack()

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_one = tk.Button(button_frame, text="Roll 1 Die", font=("Arial", 12), command=one_die)
btn_one.grid(row=0, column=0, padx=10)

btn_two = tk.Button(button_frame, text="Roll 2 Dice", font=("Arial", 12), command=two_dice)
btn_two.grid(row=0, column=1, padx=10)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit)
exit_btn.pack(pady=10)

root.mainloop()