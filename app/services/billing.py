import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from employee import Employee
from sales import Sales
from product import Product
from product_category import ProductCategory
from supplier import Supplier


class BillClass:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.geometry("1350x700+0+0")
        self.main_window.title("StockIt")
        self.main_window.config(bg="white")
        self.opened_windows = {}  # Dictionary to store opened windows

        # Get the current directory of the script
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)

        # Title
        title_image_path = self.get_image_path(parent_dir, 'logo1.png')
        self.icon_title = PhotoImage(file=title_image_path)
        title = Label(self.main_window, text="StockIT", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Logout button
        logout_button = Button(
            self.main_window, text="Logout", font=("times new roman", 15, "bold"), bg="red", cursor="hand2"
        )
        logout_button.place(x=1150, y=10, height=50, width=150)

        # Clock
        self.clock_label = Label(self.main_window, text="Welcome to StockIT\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                                 font=("times new roman", 15), bg="#4d636d", fg="white")
        self.clock_label.place(x=0, y=70, relwidth=1, height=30)

        # Product Frame
        self.var_search = StringVar()
        product_frame1 = Frame(self.main_window, bd=4, relief=RIDGE, bg="white")
        product_frame1.place(x=10, y=110, width=410, height=550)

        product_title1 = Label(product_frame1, text="All Products", font=("goudy old style", 20, "bold"),
                               bg="#262626", fg="white")
        product_title1.pack(side=TOP, fill=X)

        product_frame2 = Frame(product_frame1, bd=2, relief=RIDGE, bg="white")
        product_frame2.place(x=2, y=42, width=398, height=90)

        label_search = Label(product_frame2, text="Search Product | By Name", font=("times new roman", 15, "bold"),
                             bg="white", fg="green")
        label_search.place(x=2, y=5)

        label_search = Label(product_frame2, text="Product Name", font=("times new roman", 15, "bold"), bg="white")
        label_search.place(x=2, y=45)

        text_search = Entry(product_frame2, textvariable=self.var_search,
                            font=("times new roman", 15), bg="lightyellow")
        text_search.place(x=128, y=47, width=150, height=22)

        button_search = Button(product_frame2, text="Search", font=("goudy old style", 15), bg="#2196f3", fg="white",
                               cursor="hand2")
        button_search.place(x=285, y=45, width=100, height=25)

        button_show_all = Button(product_frame2, text="Show All", font=("goudy old style", 15), bg="#083531",
                                 fg="white", cursor="hand2")
        button_show_all.place(x=285, y=10, width=100, height=25)

        product_frame3 = Frame(product_frame1, bd=3, relief=RIDGE)
        product_frame3.place(x=2, y=140, width=398, height=375)

        scrolly = Scrollbar(product_frame3, orient=VERTICAL)
        scrollx = Scrollbar(product_frame3, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(product_frame3, columns=("pid", "name", "price", "qty", "status"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="PID")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="QTY")
        self.product_table.heading("status", text="Status")
        self.product_table["show"] = "headings"
        self.product_table.column("pid", width=90)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("qty", width=100)
        self.product_table.column("status", width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        # self.product_table.bind("<ButtonRelease-1>", self.get_data)
        label_note = Label(product_frame1, text="Note: Enter 0 quantity to remove product from the cart",
                           font=("goudy old style", 12), anchor='w', bg="white", fg="red")
        label_note.pack(side=BOTTOM, fill=X)

    @staticmethod
    def get_image_path(current_dir, image_name):
        parent_dir = os.path.dirname(current_dir)
        return os.path.join(parent_dir, 'images', image_name)


if __name__ == '__main__':
    app = Tk()
    stock_it_instance = BillClass(app)
    app.mainloop()
