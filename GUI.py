import tkinter
from tkinter import messagebox
from Restaurant import Restaurant
from main_dessert import Dessert
from main_Dishes import MainDishes
from Appetizers import Appetizer



class MyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Restaurant")

        # -------- Frames --------
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(padx=10, pady=5)
        self.mid_frame.pack(padx=10, pady=5)
        self.bottom_frame.pack(padx=10, pady=5)

        # -------- Input fields --------
        tkinter.Label(self.top_frame, text="Customer Name:").pack(side="left")
        self.name_entry = tkinter.Entry(self.top_frame, width=10)
        self.name_entry.pack(side="left")

        tkinter.Label(self.top_frame, text="Phone:").pack(side="left")
        self.phone_entry = tkinter.Entry(self.top_frame, width=10)
        self.phone_entry.pack(side="left")

        tkinter.Label(self.top_frame, text="Table:").pack(side="left")
        self.table_entry = tkinter.Entry(self.top_frame, width=5)
        self.table_entry.pack(side="left")

        tkinter.Label(self.top_frame, text="Special Request:").pack(side="left")
        self.special_entry = tkinter.Entry(self.top_frame, width=15)
        self.special_entry.pack(side="left")
        # -------- Listbox + Scrollbar --------
        self.listbox = tkinter.Listbox(self.mid_frame, height=6, width=30)
        self.listbox.pack(side="left")

        self.scrollbar = tkinter.Scrollbar(self.mid_frame, orient=tkinter.VERTICAL)
        self.scrollbar.pack(side="right", fill=tkinter.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # -------- Buttons --------
        self.app_button = tkinter.Button(
            self.bottom_frame,
            text="Appetizers",
            command=self.load_appetizers )

        self.main_button = tkinter.Button(
            self.bottom_frame,
            text="Main Dish",
            command=self.load_main_dish)

        self.des_button = tkinter.Button(
            self.bottom_frame,
            text="Dessert",
            command=self.load_dessert )

        self.add_button = tkinter.Button(
            self.bottom_frame,
            text="Add Item",
            command=self.add_item )

        self.show_button = tkinter.Button(
            self.bottom_frame,
            text="bill",
            command=self.display_info)

        self.quit_button = tkinter.Button(
            self.bottom_frame,
            text="Quit",
            command=self.main_window.destroy)

        self.save_button = tkinter.Button(
            self.bottom_frame,
            text="Save to File",
            command=self.save_to_file)

        self.save_button.pack(side="left", padx=5)
        self.app_button.pack(side="left", padx=5)
        self.main_button.pack(side="left", padx=5)
        self.des_button.pack(side="left", padx=5)
        self.add_button.pack(side="left", padx=5)
        self.show_button.pack(side="left", padx=5)
        self.quit_button.pack(side="left", padx=5)
        self.save_button.pack(side="left", padx=5)
        # -------- Data --------
        self.current_object = None



    # -------- Helper --------
    def validate_inputs(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        table = self.table_entry.get()

        if name == "" or phone == "" or table == "":
            raise ValueError("All fields are required")

        return name, phone, table

    # -------- Load menus --------
    def load_appetizers(self):
        try:
            name, phone, table = self.validate_inputs()
            self.current_object = Appetizer(name, phone, table, [], "")
            self.load_menu()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_main_dish(self):
        try:
            name, phone, table = self.validate_inputs()
            self.current_object = MainDishes(name, phone, table, [], "")
            self.load_menu()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_dessert(self):
        try:
            name, phone, table = self.validate_inputs()
            self.current_object = Dessert(name, phone, table, [], "")
            self.load_menu()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_menu(self):
        self.listbox.delete(0, tkinter.END)
        menu_items = self.current_object.load_menu()

        for item in menu_items:
            self.listbox.insert(tkinter.END, item)

    # -------- Callback functions --------
    def add_item(self):
        index = self.listbox.curselection()

        if not index:
            messagebox.showerror("Error", "Select an item first")
            return

        item = self.listbox.get(index)
        self.current_object.add_item(item)

        messagebox.showinfo("Added", "Item added successfully")

    def display_info(self):
        if self.current_object is None:
            messagebox.showerror("Error", "No order created")
            return
        self.current_object.num=self.table_entry.get()
        self.current_object.special_request = self.special_entry.get()
        info= self.current_object.display_info()
        messagebox.showinfo("Order Info", info)

    def save_to_file(self):
        if self.current_object is None:
            messagebox.showerror(title="Error", message="No order created")
            return

        try:
            name = self.name_entry.get().strip()
            phone = self.phone_entry.get().strip()
            table = self.table_entry.get().strip()
            special = self.special_entry.get().strip()

            order_list = self.current_object.order_list

            with open("orders.txt", "a") as f:
                print("----- Order -----", file=f)
                print("Name:", name, file=f)
                print("Phone:", phone, file=f)
                print("Table:", table, file=f)
                print("Special Request:", special, file=f)

                print("Items:", file=f)
                if order_list:
                    for item in order_list:
                        print("-", item, file=f)
                else:
                    print("None", file=f)

                print(file=f)

            messagebox.showinfo(title="Saved", message="Order saved to orders")# saved to file

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

my_gui=MyGUI()
tkinter.mainloop()