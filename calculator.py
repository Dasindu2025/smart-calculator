import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Calculation Logic
# -------------------------------
def calculate(operator):
    try:
        first_number = float(entry_first.get())
        second_number = float(entry_second.get())
        result = None

        if operator == '+':
            result = first_number + second_number

        elif operator == '-':
            result = first_number - second_number

        elif operator == '*':
            result = first_number * second_number

        elif operator == '/':
            if second_number == 0:
                messagebox.showerror("Error", "Can't divide by zero")
                return
            result = first_number / second_number

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# -------------------------------
# UI Setup
# -------------------------------
window = tk.Tk()
window.title("Smart Calculator")
window.geometry("300x250")
window.resizable(False, False)

# -------------------------------
# Input Fields
# -------------------------------
tk.Label(window, text="First Number").pack(pady=5)
entry_first = tk.Entry(window)
entry_first.pack()

tk.Label(window, text="Second Number").pack(pady=5)
entry_second = tk.Entry(window)
entry_second.pack()

# -------------------------------
# Buttons
# -------------------------------
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="+", width=5, command=lambda: calculate('+')).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="-", width=5, command=lambda: calculate('-')).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="*", width=5, command=lambda: calculate('*')).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="/", width=5, command=lambda: calculate('/')).grid(row=0, column=3, padx=5)

# -------------------------------
# Result Label
# -------------------------------
result_label = tk.Label(window, text="Result: ", font=("Arial", 12))
result_label.pack(pady=15)

# -------------------------------
# Run App
# -------------------------------
window.mainloop()
