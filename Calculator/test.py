import tkinter as tk

root = tk.Tk()
root.title("Calculator")

# ---------------- Display ----------------

entry = tk.Entry(root, width=25, borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ---------------- Logic ----------------

first_number = None
operation = None


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_add():
    global first_number, operation
    first_number = int(entry.get())
    operation = "+"
    entry.delete(0, tk.END)


def button_subtract():
    global first_number, operation
    first_number = int(entry.get())
    operation = "-"
    entry.delete(0, tk.END)


def button_equal():
    second_number = int(entry.get())
    entry.delete(0, tk.END)

    if operation == "+":
        entry.insert(0, first_number + second_number)
    elif operation == "-":
        entry.insert(0, first_number - second_number)


# ---------------- Buttons ----------------

button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))

button_add_btn = tk.Button(root, text="+", padx=20, pady=20, command=button_add)
button_sub_btn = tk.Button(root, text="-", padx=20, pady=20, command=button_subtract)
button_equal_btn = tk.Button(root, text="=", padx=20, pady=20, command=button_equal)
button_clear_btn = tk.Button(root, text="C", padx=20, pady=20, command=button_clear)

# ---------------- Layout ----------------

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_add_btn.grid(row=1, column=3)
button_sub_btn.grid(row=2, column=3)
button_equal_btn.grid(row=3, column=3)
button_clear_btn.grid(row=4, column=1, columnspan=2)

root.mainloop()