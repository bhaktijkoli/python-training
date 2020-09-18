# GUI Programing
# Tkinter

import tkinter as tk
from tkinter import messagebox

## Welcome Window
def show_welcome():
    welcome = tk.Tk()
    welcome.title("Welcome ADMIN")
    welcome.geometry("200x200")
    welcome.mainloop()


## Login Window
# 1. Intialize Root Window
root = tk.Tk()
root.title("Login Application")
root.geometry("200x200")

# 2. Application Logic
def button1Click():
    username = entry1.get()
    password = entry2.get()
    if username == 'admin' and password == 'admin':
        messagebox.showinfo("Login Application", "Login Successfull!")
        root.destroy()
        show_welcome()
    else:
        messagebox.showerror("Login Application", "Login Failed!")

def button2Click():
    if messagebox.askokcancel("Login Application", "Do you want to quit?"):
        root.destroy()

# 3. Intialize widgets
label1 = tk.Label(root, text="Username")
label2 = tk.Label(root, text="Password")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
button1 = tk.Button(root, text="Login", command=button1Click)
button2 = tk.Button(root, text="Quit", command=button2Click)

# 4. Placement of widgets (pack, grid, place)
label1.grid(row=1, column=1, pady=10)
label2.grid(row=2, column=1, pady=10)
entry1.grid(row=1, column=2)
entry2.grid(row=2, column=2)
button1.grid(row=3, column=2)
button2.grid(row=3, column=1)

# 5. Running the main looper
root.mainloop()
print("END")