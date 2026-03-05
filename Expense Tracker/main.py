import customtkinter as ctk
from datetime import datetime


class ExpenseTracker(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Daily Expense Tracker")
        self.geometry("500x420")
        self.resizable(False, False)

        self.categories = ["Study", "Food", "Clothes", "Travel",  "Electronics" ,"Miscellenous" ,  ]
        self.selected_category = None

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill = "both", expand = True, padx = 15, pady = 15)
        
        title = ctk.CTkLabel(
            self.main_frame,
            text="Select Category",
            font=("Arial", 18)
        )
        title.pack(pady=10)

        self.category_frame = ctk.CTkFrame(self.main_frame)
        self.category_frame.pack(pady=10)

        self.category_buttons = []

        for i, cat in enumerate(self.categories):
            btn = ctk.CTkButton(
                self.category_frame,
                text=cat,
                width=100,
                command=lambda c=cat: self.select_category(c)
            )
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            self.category_buttons.append(btn)

            self.selected_label = ctk.CTkLabel(
            self.main_frame,
            text="Selected: None"
        )
        self.selected_label.pack(pady=5)

        # input area

        self.amount_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Amount"
        )
        self.amount_entry.pack(pady=5)

        self.note_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Small note"
        )
        self.note_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(
            self.main_frame,
            text="Add Expense",
            command=self.add_expense
        )
        self.add_button.pack(pady=10)

        self.message_label = ctk.CTkLabel(self.main_frame, text="")
        self.message_label.pack(pady=5)


    def select_category(self, category):

        self.selected_category = category
        self.selected_label.configure(text=f"Selected: {category}")
        self.message_label.configure(text="")

    def add_expense(self):

        if self.selected_category is None:
            self.message_label.configure(text="Please select a category")
            return

        amount_text = self.amount_entry.get().strip()
        note = self.note_entry.get().strip()

        if not amount_text:
            self.message_label.configure(text="Enter amount")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            self.message_label.configure(text="Invalid amount")
            return

        self.save_to_file(self.selected_category, amount, note)

        self.amount_entry.delete(0, "end")
        self.note_entry.delete(0, "end")

        self.message_label.configure(text="Saved successfully")


    def save_to_file(self, category, amount, note):

        filename = f"{category.lower()}.txt"

        time_str = datetime.now().strftime("%Y-%m-%d %H:%M")

        line = f"{time_str} | {amount} | {note}\n"

        with open(filename, "a") as f:
            f.write(line)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")

    app = ExpenseTracker()
    app.mainloop()