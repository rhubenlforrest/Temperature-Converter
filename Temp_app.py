import tkinter as tk
from tkinter import messagebox

def convert_temp():
    try:
        c = float(c_entry.get())
        f = (c * 9/5) + 32
        result_label.config(text=f"{c} °C = {f} °F")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# GUI
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")
root.config(bg="#ffe0b2")

title = tk.Label(root, text="Celsius → Fahrenheit", font=("Arial", 16, "bold"), bg="#ffe0b2")
title.pack(pady=10)

c_entry = tk.Entry(root, font=("Arial", 14))
c_entry.pack(pady=5)
c_entry.insert(0, "Enter °C")

convert_btn = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_temp)
convert_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#ffe0b2")
result_label.pack(pady=10)

root.mainloop()