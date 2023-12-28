from tkinter import *
from tkinter import ttk


class Employee:
    def __init__(self, main_window):
        self.main_window = main_window
        self.initialize_gui()

        # Employee attributes
        self.employee_id = StringVar()
        self.employee_contact = StringVar()
        self.employee_birthdate = StringVar()
        self.employee_name = StringVar()
        self.employee_date_of_join = StringVar()
        self.salary = StringVar()
        self.employee_email = StringVar()
        self.employee_password = StringVar()
        self.employee_user_type = StringVar()

        # Title
        self.create_title_lable()

        # Employee attribute labels
        self.create_labels()

        # Employee attribute entries
        self.create_entries()

        # Employee address entry
        self.create_address_entry()

    def initialize_gui(self):
        self.setup_main_window()
        self.create_search_frame()
        self.create_employee_details_frame()

    def setup_main_window(self):
        self.main_window.geometry("1148x548+200+155")
        self.main_window.title("Employee")
        self.main_window.config(bg="white")
        self.main_window.focus_force()

    def create_title_lable(self):
        title = Label(self.main_window, text="Employee Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white")
        title.place(x=50, y=100, width=1050)

    def create_labels(self):
        labels_info = [
            ("Employee ID", 50, 150), ("Contact", 350, 150), ("Birthdate", 750, 150),
            ("Name", 50, 190), ("Date of Join", 350, 190), ("Salary", 750, 190),
            ("Email", 50, 230), ("Password", 350, 230), ("User Type", 750, 230),
            ("Address", 50, 270)
        ]

        for text, x, y in labels_info:
            label = Label(self.main_window, text=text, font=("goudy old style", 15), bg="white", fg="black")
            label.place(x=x, y=y)

    def create_entries(self):
        entries_info = [
            (self.employee_id, 150, 150, 180), (self.employee_contact, 500, 150, 180),
            (self.employee_birthdate, 850, 150, 180), (self.employee_name, 150, 190, 180),
            (self.employee_date_of_join, 500, 190, 180), (self.salary, 850, 190, 180),
            (self.employee_email, 150, 230, 180), (self.employee_password, 500, 230, 180)
        ]

        for variable, x, y, width in entries_info:
            entry = Entry(self.main_window, textvariable=variable, font=("goudy old style", 15), bg="lightyellow",
                          fg="black")
            entry.place(x=x, y=y, width=width)

        combo_box_user_type = ttk.Combobox(self.main_window, textvariable=self.employee_user_type,
                                           values=("Admin", "Employee"), state="readonly", justify=CENTER,
                                           font=("goudy old style", 15))
        combo_box_user_type.place(x=850, y=230, width=180)
        combo_box_user_type.current(0)

    def create_search_frame(self):
        search_label_frame = LabelFrame(self.main_window, text="Search Employee", font=("goudy old style", 12, "bold"),
                                        bd=2, relief=RIDGE, bg="white", fg="black")
        search_label_frame.place(x=250, y=20, width=600, height=70)

        self.setup_search_widgets(search_label_frame)

    def setup_search_widgets(self, frame):
        # Search attributes
        self.search_by = StringVar()
        self.search_text = StringVar()

        # Options
        combo_box_search = ttk.Combobox(frame, textvariable=self.search_by,
                                        values=("Select", "Name", "Email", "Contact"), state="readonly", justify=CENTER,
                                        font=("goudy old style", 15))
        combo_box_search.place(x=10, y=10, width=180)
        combo_box_search.current(0)

        # Search text
        search_text = Entry(frame, textvariable=self.search_text, font=("goudy old style", 15),
                            bg="lightyellow", fg="black")
        search_text.place(x=200, y=10)

        # Search button
        """search_button = Button(search_label_frame, text="Search", font=("goudy old style", 15), bg="#4caf50",
                               fg="white", cursor="hand2")
        search_button.place(x=420, y=10, width=150, height=31)"""

        style = ttk.Style()
        style.configure("Search.TButton", background="green", foreground="white")
        search_button = ttk.Button(frame, text="Search", style="Search.TButton", cursor="hand2")
        search_button.place(x=420, y=10, width=150, height=31)

    def create_employee_details_frame(self):
        # Employee frame
        employee_frame = Frame(self.main_window, bd=3, relief=RIDGE, bg="white")
        employee_frame.place(x=0, y=350, relwidth=1, height=150)

        self.create_employee_table(employee_frame)

        # Add, update, delete, clear buttons
        add_button = Button(self.main_window, text="Add", font=("goudy old style", 15), bg="#2196f3", fg="black",
                            cursor="hand2")
        add_button.place(x=500, y=285, width=110, height=31)

        update_button = Button(self.main_window, text="Update", font=("goudy old style", 15), bg="#4caf50", fg="black",
                               cursor="hand2")
        update_button.place(x=620, y=285, width=110, height=31)

        delete_button = Button(self.main_window, text="Delete", font=("goudy old style", 15), bg="#f44336", fg="black",
                               cursor="hand2")
        delete_button.place(x=740, y=285, width=110, height=31)

        clear_button = Button(self.main_window, text="Clear", font=("goudy old style", 15), bg="#607d8b", fg="black",
                              cursor="hand2")
        clear_button.place(x=860, y=285, width=110, height=31)

    def create_employee_table(self, frame):
        # Employee scrollbar
        employee_scroll_x = Scrollbar(frame, orient=HORIZONTAL)
        employee_scroll_y = Scrollbar(frame, orient=VERTICAL)

        # Employee database columns
        self.employee_table = ttk.Treeview(frame, columns=(
            "Employee ID", "Name", "Email", "Password", "User Type", "Contact", "Birthdate", "Salary", "Date of Join"),
                                           yscrollcommand=employee_scroll_y.set, xscrollcommand=employee_scroll_x.set
                                           )
        self.employee_table.pack(fill=BOTH, expand=1)

        employee_scroll_x.pack(side=BOTTOM, fill=X)
        employee_scroll_y.pack(side=RIGHT, fill=Y)
        employee_scroll_x.config(command=self.employee_table.xview)
        employee_scroll_y.config(command=self.employee_table.yview)

        headings = ("Employee ID", "Name", "Email", "Password", "User Type", "Contact", "Birthdate", "Salary",
                    "Date of Join")

        for heading in headings:
            self.employee_table.heading(heading, text=heading)
            self.employee_table.column(heading, width=100)

        self.employee_table["show"] = "headings"

    def create_address_entry(self):
        self.employee_address_text = Text(self.main_window, font=("goudy old style", 15), bg="lightyellow", fg="black")
        self.employee_address_text.place(x=150, y=270, width=300, height=60)


if __name__ == '__main__':
    app = Tk()
    employee_instance = Employee(app)
    app.mainloop()
