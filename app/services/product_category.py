import os
from tkinter import *
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

        # calling title / name / fill
        self.title_label()
        self.name_label()
        #self.fill_label()

        # calling variables
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        self.category_frame()

        self.image_left = Image.open('../../images/category.jpg')
        self.image_left = self.image_left.resize((500, 200), Image.LANCZOS)
        self.image_left = ImageTk.PhotoImage(self.image_left)
        self.label_image_left = Label(self.main_window, image=self.image_left)
        self.label_image_left.place(x=50, y=220)

        entry_txt = Entry(
            self.main_window,textvariable=self.var_name, font=("goudy old style", 18), bg="#F5F5DC", fg="black")
        entry_txt.place(x=50, y=175, width=275)
        button_add = Button(self.main_window,text="ADD", font=("goudy old style", 11), bg="green", fg="white",
                            cursor="hand2", command=self.add_category)
        button_add.place(x=350, y=175, width=100)
        button_delete = Button(
            self.main_window, text="Delete", font=("goudy old style", 11), bg="red", fg="white", cursor="hand2")
        button_delete.place(x=500, y=175, width=100)

    def title_label(self):
        """creating title"""
        title = Label(self.main_window, text="Product Category", font=("goudy old style", 30), bg="#0f4d7d", fg="white")
        title.place(x=50, y=25, width=1050)

    def name_label(self):
        name_label = Label(
            self.main_window, text="Enter Category Name Here", font=("goudy old style", 25), bg="white", fg="black")
        name_label.place(x=50, y=100, width=600)

    def category_frame(self):
        category_frame = Frame(self.main_window, bd=3, relief=RIDGE)
        category_frame.place(x=680, y=140, width=410, height=330)

        title2 = Label(category_frame, text="Product Category", font=("goudy old style", 20), bg="orange")
        title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(category_frame, orient=VERTICAL)
        bill_list = Text(category_frame, font=("goudy old style", 15), bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=bill_list.yview)
        bill_list.pack(fill=BOTH, expand=1)

    """def fill_label(self):
        # test for later change
        fill_label = Label(self.main_window, textvariable=self.var_name, font=("goudy old style", 40), bg="#0f4d7d", 
        fg="white")
        fill_label.place(x=50, y=300, width=1050)"""

    def add_category(self):
        # Get the text from the entry and add it to the Text widget
        category_text = self.var_name.get()
        category_text += '\n'  # Add a newline for separation
        self.main_window.nametowidget('.!frame.!text').insert('end', category_text)


if __name__ == '__main__':
    app = Tk()
    stock_it_instance = ProductCategory(app)
    app.mainloop()
