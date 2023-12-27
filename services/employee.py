from tkinter import *
from tkinter import ttk


class Employee:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.geometry("1148x548+200+155")
        self.main_window.title("Employee")
        self.main_window.config(bg="white")
        self.main_window.focus_force()

        # Search attributes
        self.search_by = StringVar()
        self.search_text = StringVar()

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

        # Search frame
        search_label_frame = LabelFrame(self.main_window, text="Search Employee", font=("goudy old style", 12, "bold"),
                                        bd=2, relief=RIDGE, bg="white", fg="black")
        search_label_frame.place(x=250, y=20, width=600, height=70)

        # Options
        combo_box_search = ttk.Combobox(search_label_frame, textvariable=self.search_by,
                                        values=("Select", "Name", "Email", "Contact"), state="readonly", justify=CENTER,
                                        font=("goudy old style", 15))
        combo_box_search.place(x=10, y=10, width=180)
        combo_box_search.current(0)

        # Search text
        search_text = Entry(search_label_frame, textvariable=self.search_text, font=("goudy old style", 15),
                            bg="lightyellow", fg="black")
        search_text.place(x=200, y=10)

        # Search button
        """search_button = Button(search_label_frame, text="Search", font=("goudy old style", 15), bg="#4caf50",
                               fg="white", cursor="hand2")
        search_button.place(x=420, y=10, width=150, height=31)"""

        style = ttk.Style()
        style.configure("Search.TButton", background="green", foreground="white")
        search_button = ttk.Button(search_label_frame, text="Search", style="Search.TButton", cursor="hand2")
        search_button.place(x=420, y=10, width=150, height=31)

        # Title
        title = Label(self.main_window, text="Employee Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white")
        title.place(x=50, y=100, width=1050)

        # Employee attribute labels
        employee_id_label = Label(self.main_window, text="Employee ID", font=("goudy old style", 15), bg="white",
                                  fg="black")
        employee_id_label.place(x=50, y=150)

        employee_contact_label = Label(self.main_window, text="Contact", font=("goudy old style", 15), bg="white",
                                       fg="black")
        employee_contact_label.place(x=350, y=150)

        employee_birthdate_label = Label(self.main_window, text="Birthdate", font=("goudy old style", 15), bg="white",
                                         fg="black")
        employee_birthdate_label.place(x=750, y=150)

        employee_name_label = Label(self.main_window, text="Name", font=("goudy old style", 15), bg="white", fg="black")
        employee_name_label.place(x=50, y=190)

        employee_date_of_join_label = Label(self.main_window, text="Date of Join", font=("goudy old style", 15),
                                            bg="white", fg="black")
        employee_date_of_join_label.place(x=350, y=190)

        employee_salary_label = Label(self.main_window, text="Salary", font=("goudy old style", 15), bg="white",
                                      fg="black")
        employee_salary_label.place(x=750, y=190)

        employee_email_label = Label(self.main_window, text="Email", font=("goudy old style", 15), bg="white",
                                     fg="black")
        employee_email_label.place(x=50, y=230)

        employee_password_label = Label(self.main_window, text="Password", font=("goudy old style", 15), bg="white",
                                        fg="black")
        employee_password_label.place(x=350, y=230)

        employee_user_type_label = Label(self.main_window, text="User Type", font=("goudy old style", 15), bg="white",
                                         fg="black")
        employee_user_type_label.place(x=750, y=230)

        employee_address_label = Label(self.main_window, text="Address", font=("goudy old style", 15), bg="white",
                                       fg="black")
        employee_address_label.place(x=50, y=270)

        # Employee attribute entries
        employee_id_entry = Entry(self.main_window, textvariable=self.employee_id, font=("goudy old style", 15),
                                  bg="lightyellow", fg="black")
        employee_id_entry.place(x=150, y=150, width=180)

        employee_contact_entry = Entry(self.main_window, textvariable=self.employee_contact,
                                       font=("goudy old style", 15), bg="lightyellow", fg="black")
        employee_contact_entry.place(x=500, y=150, width=180)

        employee_birthdate_entry = Entry(self.main_window, textvariable=self.employee_birthdate,
                                         font=("goudy old style", 15), bg="lightyellow", fg="black")
        employee_birthdate_entry.place(x=850, y=150, width=180)

        employee_name_entry = Entry(self.main_window, textvariable=self.employee_name, font=("goudy old style", 15),
                                    bg="lightyellow", fg="black")
        employee_name_entry.place(x=150, y=190, width=180)

        employee_date_of_join_entry = Entry(self.main_window, textvariable=self.employee_date_of_join,
                                            font=("goudy old style", 15), bg="lightyellow", fg="black")
        employee_date_of_join_entry.place(x=500, y=190, width=180)

        employee_salary_entry = Entry(self.main_window, textvariable=self.salary, font=("goudy old style", 15),
                                      bg="lightyellow", fg="black")
        employee_salary_entry.place(x=850, y=190, width=180)

        employee_email_entry = Entry(self.main_window, textvariable=self.employee_email, font=("goudy old style", 15),
                                     bg="lightyellow", fg="black")
        employee_email_entry.place(x=150, y=230, width=180)

        employee_password_entry = Entry(self.main_window, textvariable=self.employee_password,
                                        font=("goudy old style", 15), bg="lightyellow", fg="black")
        employee_password_entry.place(x=500, y=230, width=180)

        combo_box_user_type = ttk.Combobox(self.main_window, textvariable=self.employee_user_type,
                                           values=("Admin", "Employee"), state="readonly", justify=CENTER,
                                           font=("goudy old style", 15))
        combo_box_user_type.place(x=850, y=230, width=180)
        combo_box_user_type.current(0)

        self.employee_address_text = Text(self.main_window, font=("goudy old style", 15), bg="lightyellow", fg="black")
        self.employee_address_text.place(x=150, y=270, width=300, height=60)

        # Add, delete buttons
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

        # Employee frame
        employee_frame = Frame(self.main_window, bd=3, relief=RIDGE, bg="white")
        employee_frame.place(x=0, y=350, relwidth=1, height=150)

        # Employee scrollbar
        employee_scroll_x = Scrollbar(employee_frame, orient=HORIZONTAL)
        employee_scroll_y = Scrollbar(employee_frame, orient=VERTICAL)

        # Employee database columns
        self.employee_table = ttk.Treeview(employee_frame, columns=(
            "Employee ID", "Name", "Email", "Password", "User Type", "Contact", "Birthdate", "Salary", "Date of Join"),
                                           yscrollcommand=employee_scroll_y.set, xscrollcommand=employee_scroll_x.set
                                           )
        self.employee_table.pack(fill=BOTH, expand=1)

        employee_scroll_x.pack(side=BOTTOM, fill=X)
        employee_scroll_y.pack(side=RIGHT, fill=Y)
        employee_scroll_x.config(command=self.employee_table.xview)
        employee_scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("Employee ID", text="Employee ID")
        self.employee_table.heading("Name", text="Name")
        self.employee_table.heading("Email", text="Email")
        self.employee_table.heading("Password", text="Password")
        self.employee_table.heading("User Type", text="User Type")
        self.employee_table.heading("Contact", text="Contact")
        self.employee_table.heading("Birthdate", text="Birthdate")
        self.employee_table.heading("Salary", text="Salary")
        self.employee_table.heading("Date of Join", text="Date of Join")
        self.employee_table["show"] = "headings"

        self.employee_table.column("Employee ID", width=90)
        self.employee_table.column("Name", width=100)
        self.employee_table.column("Email", width=100)
        self.employee_table.column("Password", width=100)
        self.employee_table.column("User Type", width=100)
        self.employee_table.column("Contact", width=100)
        self.employee_table.column("Birthdate", width=100)
        self.employee_table.column("Salary", width=100)
        self.employee_table.column("Date of Join", width=100)


if __name__ == '__main__':
    app = Tk()
    employee_instance = Employee(app)
    app.mainloop()
