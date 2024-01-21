import os
import sqlite3
import sys
from tkinter import *
from tkinter import ttk, messagebox
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
        self.cart_list = []
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
            self.main_window, text="Logout", command=self.logout, font=("times new roman", 15, "bold"), bg="red",
            cursor="hand2"
        )
        logout_button.place(x=1150, y=10, height=50, width=150)

        # Clock
        self.clock_label = Label(self.main_window, text="Welcome to StockIT\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                                 font=("times new roman", 15), bg="#4d636d", fg="white")
        self.clock_label.place(x=0, y=70, relwidth=1, height=30)

        # Product Frame
        product_frame1 = Frame(self.main_window, bd=4, relief=RIDGE, bg="white")
        product_frame1.place(x=6, y=110, width=410, height=550)

        product_title1 = Label(product_frame1, text="All Products", font=("goudy old style", 20, "bold"),
                               bg="#262626", fg="white")
        product_title1.pack(side=TOP, fill=X)

        # Product Search Frame
        self.var_search = StringVar()
        product_frame2 = Frame(product_frame1, bd=2, relief=RIDGE, bg="white")
        product_frame2.place(x=2, y=42, width=398, height=90)

        label_search = Label(product_frame2, text="Search Product | By Name", font=("times new roman", 15, "bold"),
                             bg="white", fg="green")
        label_search.place(x=2, y=5)

        label_search = Label(product_frame2, text="Product Name", font=("times new roman", 15, "bold"), bg="white")
        label_search.place(x=2, y=45)

        text_search = Entry(product_frame2, textvariable=self.var_search,
                            font=("times new roman", 13), bg="lightyellow")
        text_search.place(x=128, y=47, width=150, height=22)

        button_search = Button(product_frame2, text="Search", command=self.search, font=("goudy old style", 15)
                               , bg="#2196f3", fg="white", cursor="hand2")
        button_search.place(x=285, y=45, width=100, height=25)

        button_show_all = Button(product_frame2, text="Show All", command=self.show, font=("goudy old style", 15),
                                 bg="#083531",
                                 fg="white", cursor="hand2")
        button_show_all.place(x=285, y=10, width=100, height=25)

        # Product Details Frame
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
        self.product_table.column("pid", width=50)
        self.product_table.column("name", width=90)
        self.product_table.column("price", width=90)
        self.product_table.column("qty", width=50)
        self.product_table.column("status", width=90)
        self.product_table.pack(fill=BOTH, expand=1)
        # self.product_table.bind("<ButtonRelease-1>", self.get_data)
        label_note = Label(product_frame1, text="Note: Enter 0 quantity to remove product from the cart",
                           font=("goudy old style", 12), anchor='w', bg="white", fg="red")
        label_note.pack(side=BOTTOM, fill=X)

        # Customer Frame
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        customer_frame = Frame(self.main_window, bd=4, relief=RIDGE, bg="white")
        customer_frame.place(x=420, y=110, width=530, height=70)

        customer_title = Label(customer_frame, text="Customer Details", font=("goudy old style", 15), bg="lightgray")
        customer_title.pack(side=TOP, fill=X)

        label_name = Label(customer_frame, text="Name", font=("times new roman", 15), bg="white")
        label_name.place(x=5, y=35)

        text_name = Entry(customer_frame, textvariable=self.var_cname, font=("times new roman", 13), bg="lightyellow")
        text_name.place(x=80, y=35, width=180)

        label_contact = Label(customer_frame, text="Contact No.", font=("times new roman", 15), bg="white")
        label_contact.place(x=270, y=35)

        text_contact = Entry(customer_frame, textvariable=self.var_contact, font=("times new roman", 13),
                             bg="lightyellow")
        text_contact.place(x=380, y=35, width=140)

        # Calc Cart Frame
        calc_cart_frame = Frame(self.main_window, bd=2, relief=RIDGE, bg="white")
        calc_cart_frame.place(x=420, y=190, width=530, height=360)

        # Calculator Frame
        self.var_calc_input = StringVar()

        calc_frame = Frame(calc_cart_frame, bd=9, relief=RIDGE, bg="white")
        calc_frame.place(x=5, y=10, width=268, height=340)

        txt_cal_input = Entry(calc_frame, textvariable=self.var_calc_input, font=('arial', 15, 'bold'), width=21,
                              bd=10, relief=GROOVE, state='readonly', justify=RIGHT)
        txt_cal_input.grid(row=0, columnspan=4)

        button_7 = Button(calc_frame, text='7', font=("arial", 15, 'bold'), command=lambda: self.get_input(7), bd=5,
                          width=4, pady=10, cursor="hand2")
        button_7.grid(row=1, column=0)
        button_8 = Button(calc_frame, text='8', font=("arial", 15, 'bold'), command=lambda: self.get_input(8), bd=5,
                          width=4, pady=10, cursor="hand2")
        button_8.grid(row=1, column=1)
        button_9 = Button(calc_frame, text='9', font=("arial", 15, 'bold'), command=lambda: self.get_input(9), bd=5,
                          width=4, pady=10, cursor="hand2")
        button_9.grid(row=1, column=2)
        button_sum = Button(calc_frame, text='+', font=("arial", 15, 'bold'), command=lambda: self.get_input('+'),
                            bd=5, width=4, pady=10, cursor="hand2")
        button_sum.grid(row=1, column=3)

        button_4 = Button(calc_frame, text='4', font=("arial", 15, 'bold'), command=lambda: self.get_input(4), bd=5,
                          width=4, pady=10, cursor="hand2")
        button_4.grid(row=2, column=0)
        button_5 = Button(calc_frame, text='5', font=("arial", 15, 'bold'), command=lambda: self.get_input(5), bd=5,
                          width=4, pady=10, cursor="hand2")
        button_5.grid(row=2, column=1)
        button_6 = Button(calc_frame, text='6', font=("arial", 15, 'bold'), command=lambda: self.get_input(6), bd=5,
                          width=4, pady=10, cursor="hand2")
        button_6.grid(row=2, column=2)
        button_sub = Button(calc_frame, text='-', font=("arial", 15, 'bold'), command=lambda: self.get_input('-'),
                            bd=5, width=4, pady=10, cursor="hand2")
        button_sub.grid(row=2, column=3)

        button_1 = Button(calc_frame, text='1', font=("arial", 15, 'bold'), command=lambda: self.get_input(1), bd=5,
                          width=4, pady=10, cursor="hand2")
        button_1.grid(row=3, column=0)
        button_2 = Button(calc_frame, text='2', font=("arial", 15, 'bold'), command=lambda: self.get_input(2), bd=5,
                          width=4, pady=10, cursor="hand2")
        button_2.grid(row=3, column=1)
        button_3 = Button(calc_frame, text='3', font=("arial", 15, 'bold'), command=lambda: self.get_input(3), bd=5,
                          width=4, pady=10, cursor="hand2")
        button_3.grid(row=3, column=2)
        button_mul = Button(calc_frame, text='*', font=("arial", 15, 'bold'), command=lambda: self.get_input('*'),
                            bd=5, width=4, pady=10, cursor="hand2")
        button_mul.grid(row=3, column=3)

        button_0 = Button(calc_frame, text='0', font=("arial", 15, 'bold'), command=lambda: self.get_input(0), bd=5,
                          width=4, pady=15, cursor="hand2")
        button_0.grid(row=4, column=0)
        button_c = Button(calc_frame, text='c', font=("arial", 15, 'bold'), command=self.clear_cal, bd=5, width=4,
                          pady=15, cursor="hand2")
        button_c.grid(row=4, column=1)
        button_eq = Button(calc_frame, text='=', font=("arial", 15, 'bold'), command=self.perform_cal, bd=5, width=4,
                           pady=15, cursor="hand2")
        button_eq.grid(row=4, column=2)
        button_div = Button(calc_frame, text='/', font=("arial", 15, 'bold'), command=lambda: self.get_input('/'),
                            bd=5, width=4, pady=15, cursor="hand2")
        button_div.grid(row=4, column=3)

        # Cart Frame
        cart_frame = Frame(calc_cart_frame, bd=3, relief=RIDGE)
        cart_frame.place(x=280, y=8, width=245, height=342)
        self.cart_title = Label(cart_frame, text="Cart \t Total Product: [0]", font=("goudy old style", 15),
                                bg="lightgray")
        self.cart_title.pack(side=TOP, fill=X)

        scrolly = Scrollbar(cart_frame, orient=VERTICAL)
        scrollx = Scrollbar(cart_frame, orient=HORIZONTAL)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty", "status"),
                                       yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cart_table.xview)
        scrolly.config(command=self.cart_table.yview)

        self.cart_table.heading("pid", text="PID")
        self.cart_table.heading("name", text="Name")
        self.cart_table.heading("price", text="Price")
        self.cart_table.heading("qty", text="QTY")
        self.cart_table.heading("status", text="Status")
        self.cart_table["show"] = "headings"
        self.cart_table.column("pid", width=40)
        self.cart_table.column("name", width=100)
        self.cart_table.column("price", width=90)
        self.cart_table.column("qty", width=40)
        self.cart_table.column("status", width=90)
        self.cart_table.pack(fill=BOTH, expand=1)
        self.cart_table.bind("<ButtonRelease-1>", self.get_data)

        # Add Cart Widgets Frame
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        add_cart_widgets_frame = Frame(self.main_window, bd=2, relief=RIDGE, bg="white")
        add_cart_widgets_frame.place(x=420, y=550, width=530, height=110)

        # Label 1
        label_product_name = Label(add_cart_widgets_frame, text="Product Name", font=("times new roman", 15),
                                   bg="white")
        label_product_name.place(x=5, y=5)
        text_product_name = Entry(add_cart_widgets_frame, textvariable=self.var_pname, font=("times new roman", 15),
                                  bg="lightyellow", state='readonly')
        text_product_name.place(x=5, y=35, width=190, height=25)

        # Label 2
        label_product_price = Label(add_cart_widgets_frame, text="Price Per Qty", font=("times new roman", 15),
                                    bg="white")
        label_product_price.place(x=230, y=5)
        text_product_price = Entry(add_cart_widgets_frame, textvariable=self.var_price, font=("times new roman", 15),
                                   bg="lightyellow", state='readonly')
        text_product_price.place(x=230, y=35, width=150, height=25)

        # Label 3
        label_product_qty = Label(add_cart_widgets_frame, text="Quantity", font=("times new roman", 15),
                                  bg="white")
        label_product_qty.place(x=390, y=5)
        text_product_qty = Entry(add_cart_widgets_frame, textvariable=self.var_qty, font=("times new roman", 15),
                                 bg="lightyellow")
        text_product_qty.place(x=390, y=35, width=120, height=25)

        # Label 4
        self.label_inStock = Label(add_cart_widgets_frame, text="In Stock", font=("times new roman", 15),
                                   bg="white")
        self.label_inStock.place(x=5, y=70)

        # Buttons
        btn_clear_cart = Button(add_cart_widgets_frame, text="Clear", font=("times new roman", 15, "bold"),
                                bg="lightgray", cursor="hand2")
        btn_clear_cart.place(x=180, y=70, width=150, height=30)

        btn_add_cart = Button(add_cart_widgets_frame, text="Add | Update Cart", command=self.add_update_cart,
                              font=("times new roman", 15, "bold"),
                              bg="orange", cursor="hand2")
        btn_add_cart.place(x=340, y=70, width=180, height=30)

        # Billing Area
        bill_frame = Frame(self.main_window, bd=2, relief=RIDGE, bg="white")
        bill_frame.place(x=953, y=110, width=410, height=410)

        bill_title = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 20, "bold"),
                           bg="#262626", fg="white")
        bill_title.pack(side=TOP, fill=X)

        scrolly = Scrollbar(bill_frame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(bill_frame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        # Billing Buttons
        bill_menu_frame = Frame(self.main_window, bd=2, relief=RIDGE, bg="white")
        bill_menu_frame.place(x=953, y=520, width=410, height=140)

        # Amount Button
        self.label_amount = Label(bill_menu_frame, text="Bill Amount\n[0]", font=("goudy old style", 15, "bold"),
                                  bg='#3f51b5', fg="white")
        self.label_amount.place(x=2, y=5, width=120, height=70)

        # Discount Button
        self.label_discount = Label(bill_menu_frame, text="Discount\n[5%]", font=("goudy old style", 15, "bold"),
                                    bg='#8bc34a', fg="white")
        self.label_discount.place(x=124, y=5, width=120, height=70)

        # Net Pay Button
        self.label_net_pay = Label(bill_menu_frame, text="Net Pay\n[0]", font=("goudy old style", 15, "bold"),
                                   bg='#607d8b', fg="white")
        self.label_net_pay.place(x=246, y=5, width=160, height=70)

        # Print Button
        button_print = Button(bill_menu_frame, text="Print", cursor="hand2", font=("goudy old style", 15, "bold"),
                              bg='lightgreen', fg="white")
        button_print.place(x=2, y=80, width=120, height=50)

        # Clear All Button
        button_clear_all = Button(
            bill_menu_frame, text="Clear All", cursor="hand2", font=("goudy old style", 15, "bold"), bg='gray',
            fg="white"
        )
        button_clear_all.place(x=124, y=80, width=120, height=50)

        # Generate Button
        button_generate = Button(
            bill_menu_frame, text="Generate Bill", cursor="hand2", font=("goudy old style", 15, "bold"), bg='#009688',
            fg="white"
        )
        button_generate.place(x=246, y=80, width=160, height=50)

        self.show()

        # Footer
        # footer = Label(self.main_window, bg="#4d636d", text="")
        # footer.pack(side=BOTTOM, fill=X)

        # ===================Functions============

    @staticmethod
    def get_image_path(current_dir, image_name):
        parent_dir = os.path.dirname(current_dir)
        return os.path.join(parent_dir, 'images', image_name)

    def get_input(self, num):
        xnum = self.var_calc_input.get() + str(num)
        self.var_calc_input.set(xnum)

    def clear_cal(self):
        self.var_calc_input.set('')

    def perform_cal(self):
        result = self.var_calc_input.get()
        self.var_calc_input.set(eval(result))

    def logout(self):
        self.main_window.destroy()
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)
        login_path = os.path.join(parent_dir, "authentication/login.py")
        os.system(f"{sys.executable} {login_path}")

    def show(self):
        con = sqlite3.connect(database=r"../../db/stockit.db")
        cur = con.cursor()
        try:
            cur.execute("select PID, Name, Price, Qty, Status from Product where Status='Active'")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.main_window)

    def search(self):
        con = sqlite3.connect(database=r"../../db/stockit.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Search input is required", parent=self.main_window)
            else:
                cur.execute("select PID, Name, Price, Qty, Status from Product where Name LIKE '%" +
                            self.var_search.get() + "%' and Status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.main_window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.main_window)

    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.label_inStock.config(text=f"In Stock [{str(row[3])}]")

    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror('Error', "Please select a product from the list", parent=self.main_window)
        elif self.var_qty.get() == '':
            messagebox.showerror('Error', "Quantity is required", parent=self.main_window)
        else:
            price_calc = int(self.var_qty.get()) * float(self.var_price.get())
            price_calc = float(price_calc)
            cart_data = [self.var_pid.get(), self.var_pname.get(), price_calc, self.var_qty.get()]
            # update cart
            present = 'no'
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_ += 1
            if present == 'yes':
                op = messagebox.askyesno('Confirm',
                                         "Product already present\nDo you want to Update or Remove from the Cart List",
                                         parent=self.main_window)
                if op == True:
                    if self.var_qty.get() == "0":
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][2] = price_calc  # price
                        self.cart_list[index_][3] = self.var_qty.get()  # quantity
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        bill_amount = 0
        net_pay = 0
        for row in self.cart_list:
            bill_amount = bill_amount + float(row[2])
        net_pay = bill_amount - ((bill_amount * 5) / 100)
        self.label_amount.config(text=f'Bill Amount\n{str(bill_amount)}')
        self.label_net_pay.config(text=f'Net Pay\n{str(net_pay)}')
        self.cart_title.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.cart_list:
                self.cart_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.main_window)


if __name__ == '__main__':
    app = Tk()
    stock_it_instance = BillClass(app)
    app.mainloop()
