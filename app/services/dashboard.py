import os
import sys
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from billing import BillClass
from employee import Employee
from sales import Sales
from product import Product
from product_category import ProductCategory
from supplier import Supplier
import time


class StockIT:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.geometry("1350x750+0+0")
        self.main_window.title("StockIt")
        self.main_window.config(bg="white")
        self.opened_windows = {}  # Dictionary to store opened windows

        # Get the current directory of the script
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)

        # Title
        title_image_path = self.get_image_path(parent_dir, 'shopping_venture.png')
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
                                 font=("helvetica", 15), bg="#4d636d", fg="white")
        self.clock_label.place(x=0, y=70, relwidth=1, height=30)

        # Menu frame
        menu_frame = Frame(self.main_window, bd=2, relief=RIDGE, bg="white")
        menu_frame.place(x=0, y=102, width=200, height=680)

        # Menu image
        menu_image_path = self.get_image_path(parent_dir, 'bg.png')
        menu_image = Image.open(menu_image_path)
        resized_menu_image = menu_image.resize((200, 200), Image.LANCZOS)
        self.menu_image_photo = ImageTk.PhotoImage(resized_menu_image)

        menu_image_label = Label(menu_frame, image=self.menu_image_photo)
        menu_image_label.pack(side=TOP, fill=X)

        # Menu label
        menu_label = Label(menu_frame, text="Menu", font=("times new roman", 20), bg="#009688")
        menu_label.pack(side=TOP, fill=X)

        # Menu options' image
        side_image_path = self.get_image_path(parent_dir, 'side_right_arrow.png')
        self.icon_side = PhotoImage(file=side_image_path)

        # Menu options
        option_to_method = {
            "Dashboard": self.dashboard,
            "Employee": self.employee,
            "Supplier": self.supplier,
            "ProdCategory": self.category,
            "Product": self.product,
            "Bills": self.sales,
            "Billing": self.billing
        }

        for option in option_to_method:
            menu_options_button = Button(
                menu_frame, text=option, command=option_to_method[option], image=self.icon_side, compound=LEFT, padx=5,
                anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2"
            )
            menu_options_button.pack(side=TOP, fill=X)

        # Dashboard content
        dashboard_icons_positions = [(300, 120), (650, 120), (1000, 120), (300, 300), (650, 300)]
        dashboard_icons_colors = ["#33bbf9", "#ff5722", "#009688", "#607d8b", "#ffc107"]
        dashboard_icons_labels = ["Total Employees\n[ 0 ]", "Total Suppliers\n[ 0 ]", "Total Categories\n[ 0 ]",
                                  "Total Products\n[ 0 ]", "Total Sales\n[ 0 ]"]
        self.dashboard_menu_labels = ["employee_label", "supplier", "category_label", "product_label", "sales_label"]

        for i in range(5):
            self.dashboard_menu_labels[i] = Label(self.main_window, text=dashboard_icons_labels[i], bd=5, relief=RIDGE,
                                                  bg=dashboard_icons_colors[i], fg="white",
                                                  font=("helvetica", 20, "bold"))
            self.dashboard_menu_labels[i].place(x=dashboard_icons_positions[i][0], y=dashboard_icons_positions[i][1],
                                                height=150, width=300)

        # Footer
        footer_label = Label(self.main_window, text="StockIT", font=("helvetica", 12), bg="#4d636d", fg="white")
        footer_label.pack(side=BOTTOM, fill=X)

        self.update_content()

    @staticmethod
    def get_image_path(current_dir, image_name):
        parent_dir = os.path.dirname(current_dir)
        return os.path.join(parent_dir, 'images', image_name)

    def destroy_all_windows(self):
        for window_key in self.opened_windows:
            self.opened_windows[window_key].destroy()
        self.opened_windows = {}  # Clear the dictionary after destroying windows

    def employee(self):
        self.destroy_all_windows()
        self.opened_windows["employee"] = Toplevel(self.main_window)
        self.opened_windows["employee"].overrideredirect(True)
        self.attach_window(self.opened_windows["employee"], self.adjust_window_position)
        self.employee_instance = Employee(self.opened_windows["employee"])

    def attach_window(self, window, adjust_window_position):
        # Get the position of main_window
        main_window_x = self.main_window.winfo_x()
        main_window_y = self.main_window.winfo_y()

        # Set the position of employee_window relative to main_window
        relative_x = 200
        relative_y = 155
        window.geometry(f"+{main_window_x + relative_x}+{main_window_y + relative_y}")

        # Raise employee_window to the top
        window.lift()

        # Bind main_window's movement to adjust employee_window's position
        self.main_window.bind("<Configure>", lambda event: adjust_window_position(window, event))

    @staticmethod
    def adjust_window_position(window, event):
        # Adjust employee_window's position when main_window is moved
        main_window_x = event.x
        main_window_y = event.y

        # Set the position of employee_window relative to main_window
        relative_x = 200  # Set the relative position based on your design
        relative_y = 131
        window.geometry(f"+{main_window_x + relative_x}+{main_window_y + relative_y}")

        # Raise employee_window to the top after adjustment
        window.lift()

    def supplier(self) -> None:
        self.destroy_all_windows()
        self.opened_windows["supplier"] = Toplevel(self.main_window)
        self.opened_windows["supplier"].overrideredirect(True)
        self.attach_window(self.opened_windows["supplier"], self.adjust_window_position)
        self.supplier_instance = Supplier(self.opened_windows["supplier"])

    def category(self):
        self.destroy_all_windows()
        self.opened_windows["category"] = Toplevel(self.main_window)
        self.opened_windows["category"].overrideredirect(True)
        self.attach_window(self.opened_windows["category"], self.adjust_window_position)
        self.category_instance = ProductCategory(self.opened_windows["category"])

    def product(self):
        self.destroy_all_windows()
        self.opened_windows["product"] = Toplevel(self.main_window)
        self.opened_windows["product"].overrideredirect(True)
        self.attach_window(self.opened_windows["product"], self.adjust_window_position)
        self.product_instance = Product(self.opened_windows["product"])

    def sales(self):
        self.destroy_all_windows()
        self.opened_windows["sales"] = Toplevel(self.main_window)
        self.opened_windows["sales"].overrideredirect(True)
        self.attach_window(self.opened_windows["sales"], self.adjust_window_position)
        self.sales_instance = Sales(self.opened_windows["sales"])

    def billing(self):
        self.destroy_all_windows()
        self.opened_windows["billing"] = Toplevel(self.main_window)
        self.opened_windows["billing"].overrideredirect(True)
        # self.attach_window(self.opened_windows["billing"], self.adjust_window_position)
        self.billing_instance = BillClass(self.opened_windows["billing"])
        self.billing_instance.main_window.geometry("1350x700+0+0")

    def dashboard(self) -> None:
        self.destroy_all_windows()

    def logout(self):
        self.main_window.destroy()
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)
        login_path = os.path.join(parent_dir, "authentication/login.py")
        os.system(f"{sys.executable} {login_path}")

    def update_content(self):
        con = sqlite3.connect(database=r"../../db/stockit.db")
        cur = con.cursor()
        try:
            cur.execute("select * from Employee")
            employee = cur.fetchall()
            self.dashboard_menu_labels[0].config(text=f'Total Employee\n[ {str(len(employee))} ]')

            cur.execute("select * from Supplier")
            supplier = cur.fetchall()
            self.dashboard_menu_labels[1].config(text=f'Total Supplier\n[ {str(len(supplier))} ]')

            cur.execute("select * from Category")
            category = cur.fetchall()
            self.dashboard_menu_labels[2].config(text=f'Total Category\n[ {str(len(category))} ]')

            cur.execute("select * from Product")
            product = cur.fetchall()
            self.dashboard_menu_labels[3].config(text=f'Total Product\n[ {str(len(product))} ]')

            bill = len(os.listdir('../../bills'))
            self.dashboard_menu_labels[4].config(text=f'Total Bills\n[{str(bill)}]')

            time_ = time.strftime("%H:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.clock_label.config(text=f'Welcome to stockIT\t\t Date: {str(date_)}\t\t Time: {str(time_)}')
            self.clock_label.after(200, self.update_content)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.main_window)


if __name__ == '__main__':
    app = Tk()
    stock_it_instance = StockIT(app)
    app.mainloop()
