import customtkinter as ctk


class ExpenseTracker(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Daily Expense Tracker")
        self.geometry("520x500")
        self.resizable(False, False)

        # ---------------- data ----------------

        self.expenses = []   # list of dicts

        # ---------------- UI ----------------

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        title = ctk.CTkLabel(
            self.main_frame,
            text="Daily Expense Tracker",
            font=("Arial", 20)
        )
        title.pack(pady=10)

        # ---- input area ----

        form = ctk.CTkFrame(self.main_frame)
        form.pack(pady=10)

        self.amount_entry = ctk.CTkEntry(form, placeholder_text="Amount")
        self.amount_entry.grid(row=0, column=0, padx=5, pady=5)

        self.category_entry = ctk.CTkEntry(form, placeholder_text="Category")
        self.category_entry.grid(row=0, column=1, padx=5, pady=5)

        self.note_entry = ctk.CTkEntry(form, placeholder_text="Note")
        self.note_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        add_btn = ctk.CTkButton(
            self.main_frame,
            text="Add Expense",
            command=self.add_expense
        )
        add_btn.pack(pady=10)

        # ---- total ----

        self.total_label = ctk.CTkLabel(
            self.main_frame,
            text="Total: 0",
            font=("Arial", 16)
        )
        self.total_label.pack(pady=5)

        # ---- list area ----

        self.list_frame = ctk.CTkScrollableFrame(self.main_frame, height=220)
        self.list_frame.pack(fill="x", pady=10)

        self.message_label = ctk.CTkLabel(self.main_frame, text="")
        self.message_label.pack()


    # ---------------- logic ----------------

    def add_expense(self):

        amount_text = self.amount_entry.get().strip()
        category = self.category_entry.get().strip()
        note = self.note_entry.get().strip()

        if not amount_text or not category:
            self.message_label.configure(text="Amount and category are required")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            self.message_label.configure(text="Invalid amount")
            return

        expense = {
            "amount": amount,
            "category": category,
            "note": note
        }

        self.expenses.append(expense)

        self.amount_entry.delete(0, "end")
        self.category_entry.delete(0, "end")
        self.note_entry.delete(0, "end")

        self.message_label.configure(text="")

        self.refresh_list()
        self.update_total()


    def refresh_list(self):

        for w in self.list_frame.winfo_children():
            w.destroy()

        for i, exp in enumerate(self.expenses, start=1):

            text = f"{i}. ₹{exp['amount']}  |  {exp['category']}"

            if exp["note"]:
                text += f"  |  {exp['note']}"

            lbl = ctk.CTkLabel(
                self.list_frame,
                text=text,
                anchor="w"
            )
            lbl.pack(fill="x", padx=5, pady=2)


    def update_total(self):

        total = sum(e["amount"] for e in self.expenses)
        self.total_label.configure(text=f"Total: ₹{total:.2f}")


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ExpenseTracker()
    app.mainloop()