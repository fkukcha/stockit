import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class Product:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.geometry("1100x500+220+130")
        self.main_window.title("Inventory Management System")
        self.main_window.config(bg="white")
        self.main_window.focus_force()

        self.search_by = StringVar()
        self.search_text = StringVar()

        # category attributes
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        self.category_product_frame()

    def category_product_frame(self):
        product_Frame = Frame(self.main_window, bd=3, relief=RIDGE)
        product_Frame.place(x=10, y=10, width=450, height=480)

        title = Label(product_Frame, text ="Manage Product Details", font=("goudy old style", 18),bg="#0f4d7d", fg="white").pack(side=TOP, fill= X)

        # Column1
        lbl_category = Label(product_Frame, text ="Category", font=("goudy old style", 18), bg="white").place(x=30,y=60)
        lbl_supplier = Label(product_Frame, text ="Supplier", font=("goudy old style", 18), bg="white").place(x=30,y=110)
        lbl_product_name = Label(product_Frame, text ="Name", font=("goudy old style", 18), bg="white").place(x=30,y=160)
        lbl_price = Label(product_Frame, text ="Price", font=("goudy old style", 18), bg="white").place(x=30,y=210)
        lbl_qty = Label(product_Frame, text ="Quantity", font=("goudy old style", 18), bg="white").place(x=30,y=260)
        lbl_status = Label(product_Frame, text ="Status", font=("goudy old style", 18), bg="white").place(x=30,y=310)


        # Column2
        combo_box_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat,
                                        values=("Select"), state="readonly", justify=CENTER,
                                        font=("goudy old style", 15))
        combo_box_cat.place(x=150,y=60, width=200)
        combo_box_cat.current(0)

        combo_box_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup,
                                        values=("Select"), state="readonly", justify=CENTER,
                                        font=("goudy old style", 15))
        combo_box_sup.place(x=150,y=110, width=200)
        combo_box_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name,
                                        font=("goudy old style", 15), bg="lightyellow").place(x=150, y=160, width=200)

        txt_price = Entry(product_Frame, textvariable=self.var_price,
                                        font=("goudy old style", 15), bg="lightyellow").place(x=150, y=210, width=200)

        txt_qty = Entry(product_Frame, textvariable=self.var_qty,
                                        font=("goudy old style", 15), bg="lightyellow").place(x=150, y=260, width=200)

        combo_box_status = ttk.Combobox(product_Frame, textvariable=self.var_status,
                                        values=("Active", "Inactive"), state="readonly", justify=CENTER,
                                        font=("goudy old style", 15))
        combo_box_status.place(x=150,y=310, width=200)
        combo_box_status.current(0)

        # Add, update, delete, clear buttons
        add_button = Button(product_Frame, text="Add", font=("goudy old style", 15), bg="#2196f3", fg="black",
                            cursor="hand2")
        add_button.place(x=10, y=400, width=100, height=40)

        update_button = Button(product_Frame, text="Update", font=("goudy old style", 15), bg="#4caf50", fg="black",
                               cursor="hand2")
        update_button.place(x=120, y=400, width=100, height=40)

        delete_button = Button(product_Frame, text="Delete", font=("goudy old style", 15), bg="#f44336", fg="black",
                               cursor="hand2")
        delete_button.place(x=230, y=400, width=100, height=40)

        clear_button = Button(product_Frame, text="Clear", font=("goudy old style", 15), bg="#607d8b", fg="black",
                              cursor="hand2")
        clear_button.place(x=340, y=400, width=100, height=40)


        search_label_frame = LabelFrame(self.main_window, text="Search Product", font=("goudy old style", 12, "bold"),
                                        bd=2, relief=RIDGE, bg="white", fg="black")
        search_label_frame.place(x=480, y=10, width=600, height=80)


        combo_box_search = ttk.Combobox(search_label_frame, textvariable=self.search_by,
                                        values=("Select", "Category", "Supplier", "Name"), state="readonly",
                                        justify=CENTER, font=("goudy old style", 15))
        combo_box_search.place(x=10, y=10, width=180)
        combo_box_search.current(0)

        # Search text
        search_text = Entry(search_label_frame, textvariable=self.search_text, font=("goudy old style", 15),
                            bg="lightyellow", fg="black")
        search_text.place(x=200, y=10)

        # Search button

        style = ttk.Style()
        style.configure("Search.TButton", background="green", foreground="white")
        search_button = ttk.Button(search_label_frame, text="Search", style="Search.TButton", cursor="hand2")
        search_button.place(x=420, y=10, width=150, height=31)


        # Product Texttable

        p_frame = Frame(self.main_window, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)
        product_scroll_x = Scrollbar(p_frame, orient=HORIZONTAL)
        product_scroll_y = Scrollbar(p_frame, orient=VERTICAL)

        # Product database columns
        self.product_table = ttk.Treeview(p_frame, columns=(
            "P ID", "Category", "Supplier", "Name", "Price", "Qty", "Status"),
                                          yscrollcommand=product_scroll_y.set, xscrollcommand=product_scroll_x.set)
        self.product_table.pack(fill=BOTH, expand=1)

        product_scroll_x.pack(side=BOTTOM, fill=X)
        product_scroll_y.pack(side=RIGHT, fill=Y)
        product_scroll_x.config(command=self.product_table.xview)
        product_scroll_y.config(command=self.product_table.yview)

        headings = ("P ID", "Category", "Supplier", "Name", "Price", "Qty", "Status")

        for heading in headings:
            self.product_table.heading(heading, text=heading)
            self.product_table.column(heading, width=100)

        self.product_table["show"] = "headings"


if __name__ == "__main__":
    app = Tk()
    product_instance = Product(app)
    app.mainloop()
