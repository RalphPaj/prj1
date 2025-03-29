import tkinter as tk
from tkinter import simpledialog, messagebox

def greet_user():
    name = simpledialog.askstring("Input", "Enter your name:")
    if name:
        messagebox.showinfo("Greeting", f"Hello, {name}!")

root = tk.Tk()
root.withdraw()  

greet_user()
