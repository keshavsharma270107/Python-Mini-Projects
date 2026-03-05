import tkinter as tk
root = tk.Tk()
root.title("Calculator")

from tkinter import font
ui_font = font.Font(size=14)

entry = tk.Entry(root, font = ui_font, width = 25, borderwidth= 5 , justify= "right")
entry.grid(row =0, column = 0, columnspan= 4, padx = 10, pady = 10, sticky = "nsew")

first_number = None
operation = None

def button_click(number):
    current = int(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def Addition():
    global first_number, operation
    first_number= int(entry.get())
    operation = "+"
    entry.delete(0, tk.END)

def Subtraction():
    global first_number, operation
    first_number= int(entry.get())
    operation = "-"
    entry.delete(0, tk.END)

def Multiplication():
    global first_number, operation
    first_number= int(entry.get())
    operation = "x"
    entry.delete(0, tk.END)

def Division():
    global first_number, operation
    first_number= int(entry.get())
    operation = "/"
    entry.delete(0, tk.END)

def equal_to(event = None):

    if entry.get() == "":
        return
    
    
    second_number = int(entry.get())
    entry.delete(0, tk.END)

    if operation == "+" :
        entry.insert(0, first_number+second_number)

    elif operation == "-" :
        entry.insert(0, first_number-second_number)
    
    elif operation == "x" :
        entry.insert(0, first_number*second_number)

    elif operation == "/" :
        entry.insert(0, first_number/second_number)

root.bind('<Return>', equal_to)

for i in range(5):        # rows: 0 to 4
    root.grid_rowconfigure(i, weight=1)

for i in range(4):        # columns: 0 to 3
    root.grid_columnconfigure(i, weight=1)

button_2 = tk.Button(root, text = '2', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(2))
button_1 = tk.Button(root, text = '1', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(1))
button_3 = tk.Button(root, text = '3', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(3))
button_4 = tk.Button(root, text = '4', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(4))
button_5 = tk.Button(root, text = '5', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(5))
button_6 = tk.Button(root, text = '6', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(6))
button_7 = tk.Button(root, text = '7', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(7))
button_8 = tk.Button(root, text = '8', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(8))
button_9 = tk.Button(root, text = '9', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(9))
button_0 = tk.Button(root, text = '0', padx = 20, pady = 20, font = ui_font, command = lambda: button_click(0))

button_7.grid(row=1, column = 0, sticky = "nsew")
button_8.grid(row=1, column = 1, sticky = "nsew")
button_9.grid(row=1, column = 2, sticky = "nsew")

button_4.grid(row=2, column = 0, sticky = "nsew")
button_5.grid(row=2, column = 1, sticky = "nsew")
button_6.grid(row=2, column = 2, sticky = "nsew")

button_1.grid(row=3, column = 0, sticky = "nsew")
button_2.grid(row=3, column = 1, sticky = "nsew")
button_3.grid(row=3, column = 2, sticky = "nsew")

button_0.grid(row=4, column = 0, sticky = "nsew")

add_button = tk.Button(root, text= "+" , padx = 20, pady = 20, command = Addition)
subtract_button = tk.Button(root, text= "-" , padx = 20, pady = 20, command = Subtraction)
multiply_button = tk.Button(root, text= "x" , padx = 20, pady = 20, command = Multiplication)
Divide_button = tk.Button(root, text= "/" , padx = 20, pady = 20, command = Division)
Equal_button = tk.Button(root, text = "=", padx = 20, pady = 20, command = equal_to)
clear_button = tk.Button(root, text = "C", padx = 20, pady = 20, command = button_clear)

add_button.grid(row = 1, column = 3, sticky = "nsew")
subtract_button.grid(row = 2, column = 3, sticky = "nsew")
multiply_button.grid(row = 3, column = 3, sticky = "nsew")
Divide_button.grid(row = 4, column = 2, sticky = "nsew")

Equal_button.grid(row = 4 , column= 3, sticky = "nsew")
clear_button.grid(row = 4 , column= 1, sticky = "nsew")

root.mainloop()