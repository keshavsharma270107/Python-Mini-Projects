import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class RestaurantApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Restaurant management system")
        self.geometry("800x500")
        self.resizable(False, False)

        self.menu = {

            "Starters" :{
            "Burger" : 60,
            "Pizza" : 150,
            "French Fries" : 90,
            "White Sauce Pasta" : 90, 
            "Fried Momos" : 50,
            "Steamed Momos" : 50,
            'Soft Drink' : 40,
            "Cold Coffee" : 40,
            "Hot Coffee" : 40
            },

            "Main Course" :{
            "Daal Makhni" : 120,
            "Paneer BUtter Masala" : 150,
            "Fried Rice" : 120,
            "Mixed Veg" : 120,
            "Stuffed Naan (2 pcs)" : 60,
            "Rumali Roti (2 pcs)" : 60,
            }
}
        self.order = {}

        self.left_frame = ctk.CTkFrame(self, width=300)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.show_category_screen()
        self.create_order_panel()


        # ----------------------Left Side Of Screen-------------------------

    def clear_left_frame(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()

    def show_category_screen(self):
        self.clear_left_frame()
        
        title = ctk.CTkLabel(
            self.left_frame,
            text="Select Category",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=20)

        starters_btn = ctk.CTkButton(
            self.left_frame,
            text="Starters",
            height=40,
            command=lambda: self.show_items_screen("Starters")
        )
        starters_btn.pack(pady=15, padx=20, fill="x")

        main_btn = ctk.CTkButton(
            self.left_frame,
            text="Main Course",
            height=40,
            command=lambda: self.show_items_screen("Main Course")
        )
        main_btn.pack(pady=15, padx=20, fill="x")

    def show_items_screen(self, category):

        self.clear_left_frame()

        title = ctk.CTkLabel(
        self.left_frame,
        text=category,
        font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        for item, price in self.menu[category].items():
            btn = ctk.CTkButton(
                self.left_frame,
                text=f"{item}  -  ₹{price}",
                command=lambda i=item, c=category: self.add_item(c, i)
            )
            btn.pack(pady=5, padx=10, fill="x")
    
        back_btn = ctk.CTkButton(
            self.left_frame,
            text="← Back to Categories",
            fg_color="gray",
            command=self.show_category_screen
        )
        back_btn.pack(pady=15, padx=10, fill="x")   



        # ------------------------Right Side-------------------------

    def create_order_panel(self):

        title = ctk.CTkLabel(
            self.right_frame,
            text="Your Order",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        self.order_text = ctk.CTkTextbox(self.right_frame, height=250)
        self.order_text.pack(padx=10, pady=10, fill="x")

        self.total_label = ctk.CTkLabel(
            self.right_frame,
            text="Total : ₹0",
            font=("Arial", 15, "bold")
        )
        self.total_label.pack(pady=5)


        btn_frame = ctk.CTkFrame(self.right_frame)
        btn_frame.pack(pady=10)

        clear_btn = ctk.CTkButton(
                btn_frame,
                text="Clear Order",
                command=self.clear_order
            )
        clear_btn.grid(row=0, column=0, padx=10)

        place_btn = ctk.CTkButton(
            btn_frame,
            text="Place Order",
            command=self.place_order
            )
        place_btn.grid(row=0, column=1, padx=10)

    def add_item(self, category, item):

        key = f"{item}"

        if key in self.order:
            self.order[key]["qty"] += 1
        else:
            self.order[key] = {
                "price": self.menu[category][item],
                "qty": 1
            }

        self.update_order_display()

    def update_order_display(self):

        self.order_text.delete("1.0", "end")

        total = 0

        for item, data in self.order.items():
            qty = data["qty"]
            price = data["price"]
            cost = qty * price
            total += cost

            self.order_text.insert(
                "end",
                f"{item}  x{qty}  =  ₹{cost}\n"
            )

        self.total_label.configure(text=f"Total : ₹{total}")

    def clear_order(self):

        self.order.clear()
        self.order_text.delete("1.0", "end")
        self.total_label.configure(text="Total : ₹0")

    def place_order(self):

        if not self.order:
            self.order_text.insert("end", "\nNo items selected!\n")
            return

        self.order_text.insert("end", "\nOrder placed successfully!\n")





if __name__ == "__main__":
    app = RestaurantApp()
    app.mainloop()
