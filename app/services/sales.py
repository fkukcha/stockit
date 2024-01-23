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
        self.bill_list=[]

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
        self.show()

    def create_title_label(self):
        title = Label(self.main_window, text="View Customer Bills", font=("helvetica", 30), bg="#184a45",
                      fg="white", bd=3, relief=RIDGE)
        title.pack(side=TOP, fill=X, padx=10, pady=20)

    def create_invoice_label(self):
        invoice = Label(self.main_window, text="Invoice No.", font=("helvetica", 15), bg="white")
        invoice.place(x=50, y=100)

    def invoice_entry(self):
        entry = Entry(self.main_window, textvariable=self.var_invoice, font=("helvetica", 15),
                      bg="lightyellow", fg="black")
        entry.place(x=160, y=100, width=180)

    def search_button(self):
        search_button = Button(self.main_window, text="Search", command=self.search, font=("helvetica", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2")
        search_button.place(x=360, y=100, width=120, height=28)

    def clear_button(self):
        clear_button = Button(self.main_window, text="Clear", command=self.clear, font=("helvetica", 15, "bold"), bg="lightgray", cursor="hand2")
        clear_button.place(x=490, y=100, width=120, height=28)

    def sales_frame(self):
        sales_frame = Frame(self.main_window, bd=3, relief=RIDGE)
        sales_frame.place(x=50, y=140, width=200, height=330)

        scrolly = Scrollbar(sales_frame, orient=VERTICAL)
        self.sales_list = Listbox(sales_frame, font=("helvetica", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)

    def bill_frame(self):
        bill_frame = Frame(self.main_window, bd=3, relief=RIDGE)
        bill_frame.place(x=280, y=140, width=410, height=330)

        title2 = Label(bill_frame, text="Customer Bill Area", font=("helvetica", 20), bg="orange")
        title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        self.bill_area = Text(bill_frame, bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

    def right_image(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)
        menu_image_path = self.get_image_path(parent_dir, 'cat2.jpg')
        original_image = Image.open(menu_image_path)

        # Resize the image as needed (replace 'new_width' and 'new_height' with your desired dimensions)
        new_width = 450
        new_height = 300
        resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

        self.menu_image = ImageTk.PhotoImage(resized_image)

        # ============================================================

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0, END)
        # print(os.listdir('../stockit'))
        for i in os.listdir('../../bills'):
            # print(i.split('.'), i.split('.')[-1])
            if i.split('.')[-1] == 'txt':
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        index_ = self.sales_list.curselection()
        file_name = self.sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0', END)
        fp = open(f'../../bills/{file_name}', 'r')
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice no. should be required", parent=self.main_window)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f'../../bills/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent=self.main_window)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)

    @staticmethod
    def get_image_path(current_dir, image_name):
        parent_dir = os.path.dirname(current_dir)
        return os.path.join(parent_dir, 'images', image_name)


if __name__ == "__main__":
    app = Tk()
    employee_instance = Sales(app)
    app.mainloop()
