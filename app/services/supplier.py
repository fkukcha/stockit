from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class Supplier:
    def __init__(self, main_window):
        self.main_window = main_window
        self.initialize_gui()

        # Supplier attributes
        self.supplier_invoice_num = StringVar()
        self.supplier_contact = StringVar()
        self.supplier_name = StringVar()

        # Title
        self.create_title_label()

        # Supplier attribute labels
        self.create_labels()

        # Supplier attribute entries
        self.create_entries()

        # Supplier description entry
        self.create_description_entry()

    def initialize_gui(self):
        self.setup_main_window()
        self.setup_search_widgets(self.main_window)
        self.create_supplier_details_frame()

    def setup_main_window(self):
        self.main_window.geometry("1148x548+200+155")
        self.main_window.title("Supplier")
        self.main_window.config(bg="white")
        self.main_window.focus_force()

    def create_title_label(self):
        title = Label(self.main_window, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d",
                      fg="white")
        title.place(x=50, y=10, width=1000, height=40)

    def create_labels(self):
        labels_info = [
            ("Invoice Nr.", 50, 80), ("Contact", 50, 160), ("Name", 50, 120), ("Description", 50, 200)
        ]

        for text, x, y in labels_info:
            label = Label(self.main_window, text=text, font=("goudy old style", 15), bg="white", fg="black")
            label.place(x=x, y=y)

    def create_entries(self):
        entries_info = [
            (self.supplier_invoice_num, 180, 80, 180), (self.supplier_name, 180, 120, 180),
            (self.supplier_contact, 180, 160, 180)
        ]

        for variable, x, y, width in entries_info:
            entry = Entry(self.main_window, textvariable=variable, font=("goudy old style", 15), bg="lightyellow",
                          fg="black")
            entry.place(x=x, y=y, width=width)

    def setup_search_widgets(self, frame):
        # Search attributes
        self.search_by = StringVar()
        self.search_text = StringVar()

        # Options
        search_label = Label(frame, text="Invoice Nr.", font=("goudy old style", 15), bg="white")
        search_label.place(x=700, y=80)

        # Search text
        search_text = Entry(frame, textvariable=self.search_text, font=("goudy old style", 15),
                            bg="lightyellow", fg="black")
        search_text.place(x=800, y=80, width=160)

        # Search button
        search_button = Button(frame, text="Search", command=self.search_supplier, font=("goudy old style", 15),
                               bg="#4caf50", fg="white", cursor="hand2")
        search_button.place(x=980, y=79, width=100, height=28)

    def create_supplier_details_frame(self):
        # Supplier frame
        supplier_frame = Frame(self.main_window, bd=3, relief=RIDGE, bg="white")
        supplier_frame.place(x=700, y=120, width=380, height=350)

        self.create_supplier_table(supplier_frame)

        # Add, update, delete, clear buttons
        add_button = Button(self.main_window, text="Add", command=self.add_supplier, font=("goudy old style", 15),
                            bg="#2196f3", fg="black", cursor="hand2")
        add_button.place(x=180, y=370, width=110, height=35)

        update_button = Button(self.main_window, text="Update", command=self.update_supplier,
                               font=("goudy old style", 15), bg="#4caf50", fg="black", cursor="hand2")
        update_button.place(x=300, y=370, width=110, height=35)

        delete_button = Button(self.main_window, text="Delete", command=self.delete_supplier,
                               font=("goudy old style", 15), bg="#f44336", fg="black", cursor="hand2")
        delete_button.place(x=420, y=370, width=110, height=35)

        clear_button = Button(self.main_window, text="Clear", command=self.clear_supplier_data,
                              font=("goudy old style", 15), bg="#607d8b", fg="black", cursor="hand2")
        clear_button.place(x=540, y=370, width=110, height=35)

    def create_supplier_table(self, frame):
        # Supplier scrollbar
        supplier_scroll_x = Scrollbar(frame, orient=HORIZONTAL)
        supplier_scroll_y = Scrollbar(frame, orient=VERTICAL)

        # Supplier database columns
        self.supplier_table = ttk.Treeview(frame, columns=("Invoice Nr.", "Name", "Contact", "Description"),
                                           yscrollcommand=supplier_scroll_y.set,  xscrollcommand=supplier_scroll_x.set)
        self.supplier_table.pack(fill=BOTH, expand=1)
        self.supplier_table.bind("<ButtonRelease-1>", self.get_data)

        supplier_scroll_x.pack(side=BOTTOM, fill=X)
        supplier_scroll_y.pack(side=RIGHT, fill=Y)
        supplier_scroll_x.config(command=self.supplier_table.xview)
        supplier_scroll_y.config(command=self.supplier_table.yview)

        headings = ("Invoice Nr.", "Name", "Contact", "Description")
        column_widths = {"Invoice Nr.": 25, "Name": 75, "Contact": 40, "Description": 60}

        for heading in headings:
            self.supplier_table.heading(heading, text=heading)
            self.supplier_table.column(heading, width=column_widths.get(heading, 20))

        self.supplier_table["show"] = "headings"

        # Show suppliers in the table.
        self.show_suppliers()

    def create_description_entry(self):
        self.supplier_description = Text(self.main_window, font=("goudy old style", 15), bg="lightyellow", fg="black")
        self.supplier_description.place(x=180, y=200, width=470, height=120)

    def add_supplier(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.supplier_invoice_num.get() == "":
                messagebox.showerror("Error", "Supplier Invoice Number is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from Supplier where SupplierInvoiceNum=?", (self.supplier_invoice_num.get(),))
                row = cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Supplier Invoice Number is already taken",
                                         parent=self.main_window)
                else:
                    cursor.execute("Insert into Supplier (SupplierInvoiceNum, Name, Contact, Description) "
                                   "values(?, ?, ?, ?) ",
                                   (self.supplier_invoice_num.get(), self.supplier_name.get(),
                                    self.supplier_contact.get(), self.supplier_description.get("1.0", END)))
                    db_connection.commit()
                    messagebox.showinfo("Success", "Supplier added successfully.", parent=self.main_window)
                    self.show_suppliers()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def show_suppliers(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            cursor.execute("Select * from Supplier")
            rows = cursor.fetchall()
            self.supplier_table.delete(*self.supplier_table.get_children())

            for row in rows:
                self.supplier_table.insert('', END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def get_data(self, event):
        focus_supplier_table = self.supplier_table.focus()
        content = self.supplier_table.item(focus_supplier_table)
        row = content["values"]

        # Show data of supplier once clicked on a supplier.
        self.supplier_invoice_num.set(row[0])
        self.supplier_name.set(row[1])
        self.supplier_contact.set(row[2])
        self.supplier_description.delete("1.0", END)
        self.supplier_description.insert(END, row[3])

    def update_supplier(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.supplier_invoice_num.get() == "":
                messagebox.showerror("Error", "Supplier Invoice Number is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from Supplier where SupplierInvoiceNum=?", (self.supplier_invoice_num.get(),))
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Supplier Invoice Number!", parent=self.main_window)
                else:
                    cursor.execute("Update Supplier set Name=?, Contact=?, Description=? where SupplierInvoiceNum=?",
                                   (self.supplier_name.get(), self.supplier_contact.get(),
                                    self.supplier_description.get("1.0", END), self.supplier_invoice_num.get()))
                    db_connection.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully.", parent=self.main_window)
                    self.show_suppliers()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def delete_supplier(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.supplier_invoice_num.get() == "":
                messagebox.showerror("Error", "Supplier Invoice Number is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from Supplier where SupplierInvoiceNum=?", (self.supplier_invoice_num.get(),))
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Supplier Invoice Number is required!", parent=self.main_window)
                else:
                    cursor.execute("Select * from Supplier where SupplierInvoiceNum=?",
                                   (self.supplier_invoice_num.get(),))
                    row = cursor.fetchone()
                    if row is None:
                        messagebox.showerror("Error", "Invalid Supplier Invoice Number!", parent=self.main_window)
                    else:
                        confirm = messagebox.askyesno("Confirm", "Do you really want to delete?",
                                                      parent=self.main_window)
                        if confirm:
                            cursor.execute("delete from Supplier where SupplierInvoiceNum=?",
                                           (self.supplier_invoice_num.get(),))
                            db_connection.commit()
                            messagebox.showinfo("Delete", "Supplier deleted successfully", parent=self.main_window)
                        self.clear_supplier_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def clear_supplier_data(self):
        # Show data of supplier once clicked on a supplier.
        self.supplier_invoice_num.set("")
        self.supplier_name.set("")
        self.supplier_contact.set("")
        self.supplier_description.delete("1.0", END)
        self.search_text.set("")

        self.show_suppliers()

    def search_supplier(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.search_text.get() == "":
                messagebox.showerror("Error", "Invoice number is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from Supplier where SupplierInvoiceNum=?", (self.search_text.get(),))
                row = cursor.fetchone()

                if row is not None:
                    self.supplier_table.delete(*self.supplier_table.get_children())
                    self.supplier_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.main_window)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)


if __name__ == '__main__':
    app = Tk()
    supplier_instance = Supplier(app)
    app.mainloop()
