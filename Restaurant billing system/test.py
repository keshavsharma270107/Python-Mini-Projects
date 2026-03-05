import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class RestaurantApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Restaurant Management System")
        self.geometry("800x500")
        self.resizable(False, False)

        # ---------------- Data ----------------
        self.menu = {
            "Burger": 120,
            "Pizza": 250,
            "Pasta": 180,
            "Sandwich": 100,
            "Coffee": 80,
            "Cold Drink": 60
        }

        self.order = {}

        # ---------------- UI ----------------
        self.create_widgets()

    def create_widgets(self):

        # Left frame (Menu)
        self.menu_frame = ctk.CTkFrame(self, width=350)
        self.menu_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.menu_label = ctk.CTkLabel(
            self.menu_frame,
            text="Menu",
            font=("Arial", 20, "bold")
        )
        self.menu_label.pack(pady=10)

        for item, price in self.menu.items():
            btn = ctk.CTkButton(
                self.menu_frame,
                text=f"{item}  -  ₹{price}",
                command=lambda i=item: self.add_item(i)
            )
            btn.pack(pady=5, padx=10, fill="x")

        # Right frame (Order)
        self.order_frame = ctk.CTkFrame(self)
        self.order_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.order_label = ctk.CTkLabel(
            self.order_frame,
            text="Your Order",
            font=("Arial", 20, "bold")
        )
        self.order_label.pack(pady=10)

        self.order_text = ctk.CTkTextbox(self.order_frame, width=380, height=250)
        self.order_text.pack(padx=10, pady=5)

        self.total_label = ctk.CTkLabel(
            self.order_frame,
            text="Total : ₹0",
            font=("Arial", 16, "bold")
        )
        self.total_label.pack(pady=10)

        self.btn_frame = ctk.CTkFrame(self.order_frame)
        self.btn_frame.pack(pady=10)

        self.clear_btn = ctk.CTkButton(
            self.btn_frame,
            text="Clear Order",
            command=self.clear_order
        )
        self.clear_btn.grid(row=0, column=0, padx=10)

        self.place_btn = ctk.CTkButton(
            self.btn_frame,
            text="Place Order",
            command=self.place_order
        )
        self.place_btn.grid(row=0, column=1, padx=10)

    # ---------------- Functions ----------------

    def add_item(self, item):

        if item in self.order:
            self.order[item] += 1
        else:
            self.order[item] = 1

        self.update_order_display()

    def update_order_display(self):

        self.order_text.delete("1.0", "end")

        total = 0

        for item, qty in self.order.items():
            price = self.menu[item]
            cost = price * qty
            total += cost

            line = f"{item}  x{qty}  =  ₹{cost}\n"
            self.order_text.insert("end", line)

        self.total_label.configure(text=f"Total : ₹{total}")

    def clear_order(self):
        self.order.clear()
        self.order_text.delete("1.0", "end")
        self.total_label.configure(text="Total : ₹0")

    def place_order(self):

        if not self.order:
            self.order_text.insert("end", "\nNo items selected!\n")
            return

        self.order_text.insert("end", "\nOrder Placed Successfully!\n")


# ---------------- Run App ----------------

if __name__ == "__main__":
    app = RestaurantApp()
    app.mainloop()