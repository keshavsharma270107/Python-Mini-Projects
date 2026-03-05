import tkinter as tk
from tkinter import messagebox


class RestaurantApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # -------- Data --------
        self.menu = {
            "Burger": 120,
            "Pizza": 250,
            "Pasta": 180,
            "Sandwich": 100,
            "Coffee": 80,
            "Cold Drink": 60
        }

        self.order = {}

        # -------- UI --------
        self.create_widgets()

    def create_widgets(self):

        # Left frame (menu)
        self.menu_frame = tk.Frame(self.root, width=300, bd=2, relief="groove")
        self.menu_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.menu_label = tk.Label(
            self.menu_frame,
            text="Menu",
            font=("Arial", 18, "bold")
        )
        self.menu_label.pack(pady=10)

        for item, price in self.menu.items():
            btn = tk.Button(
                self.menu_frame,
                text=f"{item}  -  ₹{price}",
                width=25,
                command=lambda i=item: self.add_item(i)
            )
            btn.pack(pady=5)

        # Right frame (order)
        self.order_frame = tk.Frame(self.root, bd=2, relief="groove")
        self.order_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.order_label = tk.Label(
            self.order_frame,
            text="Your Order",
            font=("Arial", 18, "bold")
        )
        self.order_label.pack(pady=10)

        self.order_text = tk.Text(self.order_frame, height=12, width=45)
        self.order_text.pack(padx=10, pady=5)

        self.total_label = tk.Label(
            self.order_frame,
            text="Total : ₹0",
            font=("Arial", 14, "bold")
        )
        self.total_label.pack(pady=10)

        self.button_frame = tk.Frame(self.order_frame)
        self.button_frame.pack(pady=10)

        self.clear_btn = tk.Button(
            self.button_frame,
            text="Clear Order",
            width=12,
            command=self.clear_order
        )
        self.clear_btn.grid(row=0, column=0, padx=10)

        self.place_btn = tk.Button(
            self.button_frame,
            text="Place Order",
            width=12,
            command=self.place_order
        )
        self.place_btn.grid(row=0, column=1, padx=10)

    # -------- Functions --------

    def add_item(self, item):

        if item in self.order:
            self.order[item] += 1
        else:
            self.order[item] = 1

        self.update_order_display()

    def update_order_display(self):

        self.order_text.delete(1.0, tk.END)

        total = 0

        for item, qty in self.order.items():
            price = self.menu[item]
            cost = price * qty
            total += cost

            line = f"{item}  x{qty}  =  ₹{cost}\n"
            self.order_text.insert(tk.END, line)

        self.total_label.config(text=f"Total : ₹{total}")

    def clear_order(self):
        self.order.clear()
        self.order_text.delete(1.0, tk.END)
        self.total_label.config(text="Total : ₹0")

    def place_order(self):

        if not self.order:
            messagebox.showinfo("Info", "No items selected!")
            return

        messagebox.showinfo("Success", "Order placed successfully!")
        self.clear_order()


# -------- Run App --------

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()