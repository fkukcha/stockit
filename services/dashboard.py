import os
from tkinter import *
from PIL import Image, ImageTk


class StockIT:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.geometry("1350x700+0+0")
        self.main_window.title("StockIt")
        self.main_window.config(bg="white")

        # Get the current directory of the script
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # Title
        title_image_path = self.get_image_path(current_dir, 'logo1.png')
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

        # Menu frame
        menu_frame = Frame(self.main_window, bd=2, relief=RIDGE, bg="white")
        menu_frame.place(x=0, y=102, width=200, height=485)

        # Menu image
        menu_image_path = self.get_image_path(current_dir, 'menu_im.png')
        menu_image = Image.open(menu_image_path)
        resized_menu_image = menu_image.resize((200, 200), Image.LANCZOS)
        self.menu_image_photo = ImageTk.PhotoImage(resized_menu_image)

        menu_image_label = Label(menu_frame, image=self.menu_image_photo)
        menu_image_label.pack(side=TOP, fill=X)

        # Menu label
        menu_label = Label(menu_frame, text="Menu", font=("times new roman", 20), bg="#009688")
        menu_label.pack(side=TOP, fill=X)

        # Menu options' image
        side_image_path = self.get_image_path(current_dir, 'side.png')
        self.icon_side = PhotoImage(file=side_image_path)

        # Menu options
        menu_options = ["Employee", "Supplier", "Category", "Product", "Sales", "Exit"]
        for option in menu_options:
            employee_button = Button(
                menu_frame, text=option, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2"
            )
            employee_button.pack(side=TOP, fill=X)

        # Dashboard content
        dashboard_icons_positions = [(300, 120), (650, 120), (1000, 120), (300, 300), (650, 300)]
        dashboard_icons_colors = ["#33bbf9", "#ff5722", "#009688", "#607d8b", "#ffc107"]
        dashboard_icons_labels = ["Total Employees\n[ 0 ]", "Total Suppliers\n[ 0 ]", "Total Categories\n[ 0 ]",
                                  "Total Products\n[ 0 ]", "Total Sales\n[ 0 ]"]
        for i in range(5):
            label = Label(self.main_window, text=dashboard_icons_labels[i], bd=5, relief=RIDGE,
                          bg=dashboard_icons_colors[i], fg="white", font=("goody old style", 20, "bold"))
            label.place(x=dashboard_icons_positions[i][0], y=dashboard_icons_positions[i][1], height=150, width=300)

        # Footer
        footer_label = Label(self.main_window, text="StockIT", font=("times new roman", 12), bg="#4d636d", fg="white")
        footer_label.pack(side=BOTTOM, fill=X)

    @staticmethod
    def get_image_path(current_dir, image_name):
        parent_dir = os.path.dirname(current_dir)
        return os.path.join(parent_dir, 'images', image_name)


app = Tk()
stock_it_instance = StockIT(app)
app.mainloop()