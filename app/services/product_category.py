import os
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from employee import Employee
import sqlite3


class ProductCategory:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.geometry("1148x548+200+155")
        self.main_window.title("Category")
        self.main_window.config(bg="white")
        self.main_window.focus_force()

        # calling title / name / fill / frame
        self.title_label()
        self.name_label()
        #self.category_frame()

        # calling variables
        self.var_cat_id = StringVar()
        self.var_name = StringVar()



        self.image_left = Image.open('../../images/category.jpg')
        self.image_left = self.image_left.resize((500, 275), Image.LANCZOS)
        self.image_left = ImageTk.PhotoImage(self.image_left)
        self.label_image_left = Label(self.main_window, image=self.image_left)
        self.label_image_left.place(x=50, y=220)

        self.image_right = Image.open('../../images/cat.jpg')
        self.image_right = self.image_right.resize((500, 275), Image.LANCZOS)
        self.image_right = ImageTk.PhotoImage(self.image_right)
        self.label_image_right = Label(self.main_window, image=self.image_right)
        self.label_image_right.place(x=600, y=220)

        entry_txt = Entry(
            self.main_window,textvariable=self.var_name, font=("goudy old style", 18), bg="#F5F5DC", fg="black")
        entry_txt.place(x=50, y=175, width=275)
        button_add = Button(self.main_window,text="ADD", font=("goudy old style", 11), bg="green", fg="white",
                            cursor="hand2", command=self.add_category)
        button_add.place(x=350, y=175, width=100)
        button_delete = Button(
            self.main_window, text="Delete", font=("goudy old style", 11), bg="red", fg="white", cursor="hand2")
        button_delete.place(x=500, y=175, width=100)


        # Entry and Buttons
        self.create_entry_and_buttons()

        # Category Table
        self.create_category_table()


    def title_label(self):
        """creating title"""
        title = Label(self.main_window, text="Product Category", font=("goudy old style", 30), bg="#0f4d7d", fg="white")
        title.place(x=50, y=25, width=1050)

    def name_label(self):
        name_label = Label(
            self.main_window, text="Enter Category Name Here", font=("goudy old style", 25), bg="white", fg="black")
        name_label.place(x=50, y=100, width=600)

    def create_entry_and_buttons(self):
        entry_txt = Entry(self.main_window, textvariable=self.var_name, font=("goudy old style", 18), bg="#F5F5DC",
                          fg="black")
        entry_txt.place(x=50, y=175, width=275)



    def create_category_table(self):
        category_frame = Frame(self.main_window, bd=3, relief=RIDGE)
        category_frame.place(x=680, y=100, width=410, height=100)

        scrolly = Scrollbar(category_frame, orient=VERTICAL)
        scrollx = Scrollbar(category_frame, orient=HORIZONTAL)

        self.category_table = ttk.Treeview(category_frame, columns=("ID", "Name"), yscrollcommand=scrolly.set,
                                           xscrollcommand=scrollx.set)

        self.category_table.pack(fill=BOTH, expand=1)
        #self.category_table.bind("<ButtonRelease-1>", self.get_data)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        self.category_table.heading("ID", text="ID")
        self.category_table.heading("Name", text="Name")
        self.category_table["show"] = "headings"
        self.category_table.column("ID", width=90)
        self.category_table.column("Name", width=100)
        self.category_table.pack(fill=BOTH, expand=1)

    def add_category(self):
        # Get the text from the entry and add it to the Text widget
        category_text = self.var_name.get()
        category_text += '\n'  # Add a newline for separation
        self.main_window.nametowidget('.!frame.!text').insert('end', category_text)


if __name__ == '__main__':
    app = Tk()
    stock_it_instance = ProductCategory(app)
    app.mainloop()
