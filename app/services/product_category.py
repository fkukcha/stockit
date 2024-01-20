import os
from tkinter import *
from tkinter import ttk, messagebox

from PIL import Image, ImageTk
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
        self.category_frame = self.create_category_table()

        # calling variables
        self.var_cat_id = StringVar()
        self.var_name = StringVar()


        # creates image on the left
        self.image_left = Image.open('../../images/category.jpg')
        self.image_left = self.image_left.resize((500, 275), Image.LANCZOS)
        self.image_left = ImageTk.PhotoImage(self.image_left)
        self.label_image_left = Label(self.main_window, image=self.image_left)
        self.label_image_left.place(x=50, y=220)

        # creates image on the right
        self.image_right = Image.open('../../images/cat.jpg')
        self.image_right = self.image_right.resize((500, 275), Image.LANCZOS)
        self.image_right = ImageTk.PhotoImage(self.image_right)
        self.label_image_right = Label(self.main_window, image=self.image_right)
        self.label_image_right.place(x=600, y=220)

        # entry and buttons
        self.create_entry_and_buttons()

        # category table
        self.create_category_table()


    def title_label(self):
        """creates title"""
        title = Label(self.main_window, text="Product Category", font=("goudy old style", 30), bg="#0f4d7d", fg="white")
        title.place(x=50, y=25, width=1050)

    def name_label(self):
        """creates label"""
        name_label = Label(
            self.main_window, text="Enter Category Name Here", font=("goudy old style", 25), bg="white", fg="black")
        name_label.place(x=50, y=100, width=600)

    def create_entry_and_buttons(self):
        """creates entry text + buttons"""
        entry_txt = Entry(self.main_window, textvariable=self.var_name, font=("goudy old style", 18), bg="#F5F5DC",
                          fg="black")
        entry_txt.place(x=50, y=175, width=275)
        entry_txt = Entry(
            self.main_window, textvariable=self.var_name, font=("goudy old style", 18), bg="#F5F5DC", fg="black")
        entry_txt.place(x=50, y=175, width=275)
        button_add = Button(self.main_window, text="ADD", font=("goudy old style", 11), bg="green", fg="white",
                            cursor="hand2", command=self.add_category)
        button_add.place(x=350, y=175, width=100)
        button_delete = Button(
            self.main_window, text="Delete", font=("goudy old style", 11), bg="red", fg="white", cursor="hand2")
        button_delete.place(x=500, y=175, width=100)



    def create_category_table(self):
        """creates + heading"""
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

        self.category_table.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        self.category_table.heading("ID", text="ID")
        self.category_table.heading("Name", text="Name")
        self.category_table["show"] = "headings"
        self.category_table.column("ID", width=90)
        self.category_table.column("Name", width=100)
        self.category_table.pack(fill=BOTH, expand=1)

        return category_frame

        # functions for database

    def add_category(self):
        """adding categories"""
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category name is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from category where name=?", (self.var_name.get(),))
                row = cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This category name is already taken", parent=self.main_window)
                else:
                    cursor.execute("Insert into category (Name) VALUES (?)", (self.var_name.get(),))
                    db_connection.commit()
                    messagebox.showinfo("Success", "Category added successfully.", parent=self.main_window)
                    # Refresh the category table after adding a new category
                    self.show_categories()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def show_categories(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            cursor.execute("Select * from category")
            rows = cursor.fetchall()
            self.category_table.delete(*self.category_table.get_children())

            for row in rows:
                self.category_table.insert('', END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def delete_category(self):
        """deleteing categories"""
        focus_category_table = self.category_table.focus()
        if not focus_category_table:
            messagebox.showerror("Error", "Please select a category to delete.", parent=self.main_window)
            return

        confirm = messagebox.askyesno("Confirm", "Do you really want to delete this category?",
                                      parent=self.main_window)
        if confirm:
            # Get the ID of the selected category
            category_id = self.category_table.item(focus_category_table, "values")[0]

            # Add your code to delete the category using the category_id (Delete category from the database)

            # After deleting --> update the category table
            self.show_categories()

    def get_data_category(self, event):
        focus_category_table = self.category_table.focus()
        content = self.category_table.item(focus_category_table)
        row = content["values"]
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])


if __name__ == '__main__':
    app = Tk()
    stock_it_instance = ProductCategory(app)
    app.mainloop()
