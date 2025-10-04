import tkinter as tk
import random

number = random.randint(1, 100)

def check_guess():
    user_input = entry.get()
    if user_input.strip() == "":
        result_label.config(text="⚠️ Please enter a number!", fg="red")
        return
    try:
        guess = int(user_input)
        if guess < number:
            result_label.config(text="Too low! Try again 😅", fg="blue")
        elif guess > number:
            result_label.config(text="Too high! Try again 😬", fg="orange")
        else:
            result_label.config(text=f"🎉 Correct! The number was {number}", fg="green")
    except ValueError:
        result_label.config(text="⚠️ Please enter a valid number!", fg="red")

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg="#f2f2f2")

tk.Label(root, text="Guess the Number (1–100)", font=("Arial", 14, "bold"), bg="#f2f2f2").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=10)
tk.Button(root, text="Check", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=check_guess).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
result_label.pack(pady=10)

root.mainloop()
