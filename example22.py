# GUI Calculator Program
import tkinter as tk

# Intialize window
window = tk.Tk()
window.title("Calculator")

# Application Logic
result = tk.StringVar()
def add(value):
    result.set(result.get() + value)
def peform():
    result.set(eval(result.get()))
def clear():
    result.set("")

# Initialize Widgets
label1 = tk.Label(window, textvariable=result)
button1 = tk.Button(window, text="1", padx=10, pady=10, bg="white", fg="black", command=lambda : add("1"))
button2 = tk.Button(window, text="2", padx=10, pady=10, bg="white", fg="black",command=lambda : add("2"))
button3 = tk.Button(window, text="3", padx=10, pady=10, bg="white", fg="black",command=lambda : add("3"))

button4 = tk.Button(window, text="4", padx=10, pady=10, bg="white", fg="black",command=lambda : add("4"))
button5 = tk.Button(window, text="5", padx=10, pady=10, bg="white", fg="black",command=lambda : add("5"))
button6 = tk.Button(window, text="6", padx=10, pady=10, bg="white", fg="black",command=lambda : add("6"))

button7 = tk.Button(window, text="7", padx=10, pady=10, bg="white", fg="black",command=lambda : add("7"))
button8 = tk.Button(window, text="8", padx=10, pady=10, bg="white", fg="black",command=lambda : add("8"))
button9 = tk.Button(window, text="9", padx=10, pady=10, bg="white", fg="black",command=lambda : add("9"))

button0 = tk.Button(window, text="0", padx=10, pady=10, bg="white", fg="black",command=lambda : add("0"))
button_dot = tk.Button(window, text=".", padx=10, pady=10, bg="#eee", fg="black",command=lambda : add("."))
button_equal = tk.Button(window, text="=", padx=10, pady=10, bg="green", fg="white",command=peform)
button_clear = tk.Button(window, text="C", padx=10, pady=10, bg="white", fg="black",command=clear)

button_multiply = tk.Button(window, text="*", padx=10, pady=10, bg="#eee", fg="black",command=lambda : add("*"))
button_minus = tk.Button(window, text="-", padx=10, pady=10, bg="#eee", fg="black",command=lambda : add("-"))
button_add = tk.Button(window, text="+", padx=10, pady=10, bg="#eee", fg="black",command=lambda : add("+"))
# Placement of Widgets
# Row0
label1.grid(row=0, column=0, columnspan=3, sticky="W")
# Row1
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)
# Row2
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)
# Row3
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_add.grid(row=3, column=3)
# Row4
button_clear.grid(row=4, column=0)
button0.grid(row= 4, column=1)
button_dot.grid(row= 4, column=2)
button_equal.grid(row= 4, column=3)
# Main Loop
window.mainloop()