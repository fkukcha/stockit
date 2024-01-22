from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class Product:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.geometry("1148x548+200+155")
        self.main_window.title("Inventory Management System")
        self.main_window.config(bg="white")
        self.main_window.focus_force()

        self.search_by = StringVar()
        self.search_text = StringVar()

        # category attributes
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()

        self.category_product_frame()

        self.show_products()

    def category_product_frame(self):
        product_Frame = Frame(self.main_window, bd=3, relief=RIDGE)
        product_Frame.place(x=10, y=10, width=450, height=480)

        Label(product_Frame, text="Manage Product Details", font=("goody old style", 18), bg="#0f4d7d",
              fg="white").pack(side=TOP, fill=X)

        # Column1
        Label(product_Frame, text="Category", font=("goody old style", 18), bg="white").place(x=30, y=60)
        Label(product_Frame, text="Supplier", font=("goody old style", 18), bg="white").place(x=30,
                                                                                              y=110)
        Label(product_Frame, text="Name", font=("goody old style", 18), bg="white").place(x=30,
                                                                                          y=160)
        Label(product_Frame, text="Price", font=("goody old style", 18), bg="white").place(x=30, y=210)
        Label(product_Frame, text="Quantity", font=("goody old style", 18), bg="white").place(x=30, y=260)
        Label(product_Frame, text="Status", font=("goody old style", 18), bg="white").place(x=30, y=310)

        # Column2
        combo_box_cat = ttk.Combobox(
            product_Frame, textvariable=self.var_cat, values=self.cat_list, state="readonly", justify=CENTER,
            font=("goody old style", 15)
        )
        combo_box_cat.place(x=150, y=60, width=200)
        combo_box_cat.current(0)

        combo_box_sup = ttk.Combobox(
            product_Frame, textvariable=self.var_sup, values=self.sup_list, state="readonly", justify=CENTER,
            font=("goody old style", 15)
        )
        combo_box_sup.place(x=150, y=110, width=200)
        combo_box_sup.current(0)

        Entry(product_Frame, textvariable=self.var_name,
              font=("goody old style", 15), bg="light yellow").place(x=150, y=160, width=200)

        Entry(product_Frame, textvariable=self.var_price,
              font=("goody old style", 15), bg="light yellow").place(x=150, y=210, width=200)

        Entry(product_Frame, textvariable=self.var_qty,
              font=("goody old style", 15), bg="light yellow").place(x=150, y=260, width=200)

        combo_box_status = ttk.Combobox(
            product_Frame, textvariable=self.var_status, values=("Active", "Inactive"), state="readonly",
            justify=CENTER, font=("goody old style", 15)
        )
        combo_box_status.place(x=150, y=310, width=200)
        combo_box_status.current(0)

        # Add, update, delete, clear buttons
        add_button = Button(product_Frame, text="Add", command=self.add_product, font=("goody old style", 15),
                            bg="#2196f3", fg="black", cursor="hand2")
        add_button.place(x=10, y=400, width=100, height=40)

        update_button = Button(
            product_Frame, text="Update", command=self.update_products, font=("goody old style", 15), bg="#4caf50",
            fg="black", cursor="hand2"
        )
        update_button.place(x=120, y=400, width=100, height=40)

        delete_button = Button(
            product_Frame, text="Delete", command=self.delete_product, font=("goody old style", 15), bg="#f44336",
            fg="black", cursor="hand2"
        )
        delete_button.place(x=230, y=400, width=100, height=40)

        clear_button = Button(
            product_Frame, text="Clear", command=self.clear_product_data, font=("goody old style", 15), bg="#607d8b",
            fg="black", cursor="hand2"
        )
        clear_button.place(x=340, y=400, width=100, height=40)

        search_label_frame = LabelFrame(self.main_window, text="Search Product", font=("goudy old style", 12, "bold"),
                                        bd=2, relief=RIDGE, bg="white", fg="black")
        search_label_frame.place(x=480, y=10, width=600, height=80)

        combo_box_search = ttk.Combobox(search_label_frame, textvariable=self.search_by,
                                        values=("Select", "Category", "Supplier", "Name"), state="readonly",
                                        justify=CENTER, font=("goody old style", 15))
        combo_box_search.place(x=10, y=10, width=180)
        combo_box_search.current(0)

        # Search text
        search_text = Entry(search_label_frame, textvariable=self.search_text, font=("goody old style", 15),
                            bg="light yellow", fg="black")
        search_text.place(x=200, y=10)

        # Search button
        style = ttk.Style()
        style.configure("Search.TButton", background="black", foreground="black")
        search_button = ttk.Button(
            search_label_frame, text="Search", command=self.search_product, style="Search.TButton", cursor="hand2"
        )
        search_button.place(x=435, y=10, width=150, height=31)

        # Product Texttable
        p_frame = Frame(self.main_window, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)
        product_scroll_x = Scrollbar(p_frame, orient=HORIZONTAL)
        product_scroll_y = Scrollbar(p_frame, orient=VERTICAL)

        # Product database columns
        self.product_table = ttk.Treeview(p_frame, columns=(
            "PID", "Category", "Supplier", "Name", "Price", "Qty", "Status"),
                                          yscrollcommand=product_scroll_y.set, xscrollcommand=product_scroll_x.set)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        product_scroll_x.pack(side=BOTTOM, fill=X)
        product_scroll_y.pack(side=RIGHT, fill=Y)
        product_scroll_x.config(command=self.product_table.xview)
        product_scroll_y.config(command=self.product_table.yview)

        headings = ("PID", "Category", "Supplier", "Name", "Price", "Qty", "Status")
        column_width = {"PID": 10, "Category": 60, "Supplier": 60, "Name": 35, "Price": 20, "Qty": 10, "Status": 25}

        for heading in headings:
            self.product_table.heading(heading, text=heading)
            self.product_table.column(heading, width=column_width.get(heading, 50))

        self.product_table["show"] = "headings"

    # ==========================================================================

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()
        try:
            cursor.execute("Select Name from Category")
            cat = cursor.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            cursor.execute("Select Name from Supplier")
            sup = cursor.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
            print(sup)

        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def add_product(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if (self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_sup.get() == "Select" or
                    self.var_name.get() == ""):
                messagebox.showerror("Error", "All fields are required", parent=self.main_window)
            else:
                cursor.execute("Select * from Product where Name=?", (self.var_name.get(),))
                row = cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Product already present, try different", parent=self.main_window)
                else:
                    cursor.execute(
                        "Insert into Product (Category, Supplier, Name, Price, Qty, Status) values(?, ?, ?, ?, ?, ?) ",
                        (self.var_cat.get(), self.var_sup.get(), self.var_name.get(), self.var_price.get(),
                         self.var_qty.get(), self.var_status.get()))
                    db_connection.commit()
                    messagebox.showinfo("Success", "Product added successfully.", parent=self.main_window)
                    self.show_products()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def get_data(self, event):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6])

    def update_products(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select product from list!", parent=self.main_window)
            else:
                cursor.execute("Select * from Product where PID=?", (self.var_pid.get(),))
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product!", parent=self.main_window)
                else:
                    cursor.execute(
                        'Update Product set Category=?, Supplier=?, Name=?, Price=?, Qty=?, Status=? where PID=?',
                        (self.var_cat.get(), self.var_sup.get(), self.var_name.get(), self.var_price.get(),
                         self.var_qty.get(), self.var_status.get(), self.var_pid.get()))
                    db_connection.commit()
                    messagebox.showinfo("Success", "Product updated successfully.", parent=self.main_window)
                    self.show_products()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def show_products(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            cursor.execute("Select * from Product")
            rows = cursor.fetchall()
            self.product_table.delete(*self.product_table.get_children())

            for row in rows:
                self.product_table.insert('', END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def delete_product(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select Product from list!", parent=self.main_window)
            else:
                cursor.execute("Select * from Product where PID=?", (self.var_pid.get(),))
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product!", parent=self.main_window)
                else:
                    confirm = messagebox.askyesno("Confirm", "Do you really want to delete?",
                                                  parent=self.main_window)
                    if confirm:
                        cursor.execute("delete from Product where PID=?", (self.var_pid.get(),))
                        db_connection.commit()
                        messagebox.showinfo("Delete", "Product deleted successfully", parent=self.main_window)
                        self.clear_product_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def clear_product_data(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.search_text.set("")
        self.search_by.set("Select")
        self.show_products()

    def search_product(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.search_by.get() == "Search":
                messagebox.showerror("Error", "Select an option please.", parent=self.main_window)
            elif self.search_text.get() == "":
                messagebox.showerror("Error", "Search input is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from Product where " + self.search_by.get() + " LIKE '%" +
                               self.search_text.get() + "%'")
                rows = cursor.fetchall()

                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.main_window)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)


if __name__ == "__main__":
    app = Tk()
    product_instance = Product(app)
    app.mainloop()
