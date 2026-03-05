import tkinter as tk
from tkinter import ttk
from datetime import datetime


class ExpenseTracker(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Daily Expense Tracker")
        self.geometry("420x360")
        self.resizable(False, False)

        # ---------------- data ----------------

        self.categories = ["Study", "Food", "Clothes", "Travel"]
        self.selected_category = None

        # ---------------- UI ----------------

        main = ttk.Frame(self, padding=15)
        main.pack(fill="both", expand=True)

        title = ttk.Label(main, text="Select Category", font=("Arial", 14))
        title.pack(pady=5)

        # category buttons

        self.cat_frame = ttk.Frame(main)
        self.cat_frame.pack(pady=10)

        for i, cat in enumerate(self.categories):
            btn = ttk.Button(
                self.cat_frame,
                text=cat,
                command=lambda c=cat: self.select_category(c),
                width=12
            )
            btn.grid(row=i // 2, column=i % 2, padx=8, pady=8)

        self.selected_label = ttk.Label(main, text="Selected: None")
        self.selected_label.pack(pady=5)

        # inputs

        self.amount_entry = ttk.Entry(main)
        self.amount_entry.pack(pady=5, fill="x")
        self.amount_entry.insert(0, "Amount")

        self.note_entry = ttk.Entry(main)
        self.note_entry.pack(pady=5, fill="x")
        self.note_entry.insert(0, "Note")

        self.add_btn = ttk.Button(
            main,
            text="Add Expense",
            command=self.add_expense
        )
        self.add_btn.pack(pady=10)

        self.message_label = ttk.Label(main, text="")
        self.message_label.pack()

    # ---------------- logic ----------------

    def select_category(self, category):
        self.selected_category = category
        self.selected_label.config(text=f"Selected: {category}")
        self.message_label.config(text="")

    def add_expense(self):

        if self.selected_category is None:
            self.message_label.config(text="Please select a category")
            return

        amount_text = self.amount_entry.get().strip()
        note = self.note_entry.get().strip()

        if not amount_text or amount_text == "Amount":
            self.message_label.config(text="Enter amount")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            self.message_label.config(text="Invalid amount")
            return

        self.save_to_file(self.selected_category, amount, note)

        self.amount_entry.delete(0, tk.END)
        self.note_entry.delete(0, tk.END)

        self.message_label.config(text="Saved successfully")

    def save_to_file(self, category, amount, note):

        filename = f"{category.lower()}.txt"
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M")

        line = f"{time_str} | {amount} | {note}\n"

        with open(filename, "a") as f:
            f.write(line)


if __name__ == "__main__":
    app = ExpenseTracker()
    app.mainloop()