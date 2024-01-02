import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class Sales:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.geometry("1148x548+200+155")
        self.main_window.title("Sales")
        self.main_window.config(bg="white")
        self.main_window.focus_force()

        self.var_invoice = StringVar()

        self.create_title_label()
        self.create_invoice_label()
        self.invoice_entry()
        self.search_button()
        self.clear_button()
        self.sales_frame()
        self.bill_frame()
        self.right_image()
        self.image_label = Label(self.main_window, image=self.menu_image, borderwidth=0, highlightthickness=0)
        self.image_label.place(x=700, y=110)

    def create_title_label(self):
        title = Label(self.main_window, text="View Customer Bills", font=("goudy old style", 30), bg="#184a45",
                      fg="white", bd=3, relief=RIDGE)
        title.pack(side=TOP, fill=X, padx=10, pady=20)

    def create_invoice_label(self):
        invoice = Label(self.main_window, text="Invoice No.", font=("times new roman", 15), bg="white")
        invoice.place(x=50, y=100)

    def invoice_entry(self):
        entry = Entry(self.main_window, textvariable=self.var_invoice, font=("goudy old style", 15),
                      bg="lightyellow", fg="black")
        entry.place(x=160, y=100, width=180)

    def search_button(self):
        search_button = Button(self.main_window, text="Search", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2")
        search_button.place(x=360, y=100, width=120, height=28)

    def clear_button(self):
        clear_button = Button(self.main_window, text="Clear", font=("times new roman", 15, "bold"), bg="lightgray", cursor="hand2")
        clear_button.place(x=490, y=100, width=120, height=28)

    def sales_frame(self):
        sales_frame = Frame(self.main_window, bd=3, relief=RIDGE)
        sales_frame.place(x=50, y=140, width=200, height=330)

        scrolly = Scrollbar(sales_frame, orient=VERTICAL)
        sales_list = Listbox(sales_frame, font=("goudy old styöe", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=sales_list.yview)
        sales_list.pack(fill=BOTH, expand=1)

    def bill_frame(self):
        bill_frame = Frame(self.main_window, bd=3, relief=RIDGE)
        bill_frame.place(x=280, y=140, width=410, height=330)

        title2 = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 20), bg="orange")
        title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        bill_list = Text(bill_frame, font=("goudy old style", 15), bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=bill_list.yview)
        bill_list.pack(fill=BOTH, expand=1)

    def right_image(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        menu_image_path = self.get_image_path(current_dir, 'cat2.jpg')
        original_image = Image.open(menu_image_path)

        # Resize the image as needed (replace 'new_width' and 'new_height' with your desired dimensions)
        new_width = 450
        new_height = 300
        resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

        self.menu_image = ImageTk.PhotoImage(resized_image)

    @staticmethod
    def get_image_path(current_dir, image_name):
        parent_dir = os.path.dirname(current_dir)
        return os.path.join(parent_dir, 'images', image_name)


if __name__ == "__main__":
    app = Tk()
    employee_instance = Sales(app)
    app.mainloop()
