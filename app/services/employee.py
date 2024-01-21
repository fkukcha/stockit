from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


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
        self.employee_salary = StringVar()
        self.employee_email = StringVar()
        self.employee_password = StringVar()
        self.employee_user_type = StringVar()

        # Title
        self.create_title_label()

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

    def create_title_label(self):
        title = Label(self.main_window, text="Employee Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white")
        title.place(x=50, y=100, width=1050)

    def create_labels(self):
        labels_info = [
            ("EmployeeID", 50, 150), ("Contact", 350, 150), ("Birthdate", 750, 150),
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
            (self.employee_date_of_join, 500, 190, 180), (self.employee_salary, 850, 190, 180),
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
        search_button = Button(frame, text="Search", command=self.search_employee, font=("goudy old style", 15),
                               bg="#4caf50", fg="white", cursor="hand2")
        search_button.place(x=420, y=10, width=150, height=31)

    def create_employee_details_frame(self):
        # Employee frame
        employee_frame = Frame(self.main_window, bd=3, relief=RIDGE, bg="white")
        employee_frame.place(x=0, y=350, relwidth=1, height=150)

        self.create_employee_table(employee_frame)

        # Add, update, delete, clear buttons
        add_button = Button(self.main_window, text="Add", command=self.add_employee, font=("goudy old style", 15),
                            bg="#2196f3", fg="black", cursor="hand2")
        add_button.place(x=500, y=285, width=110, height=31)

        update_button = Button(self.main_window, text="Update", command=self.update_employee,
                               font=("goudy old style", 15), bg="#4caf50", fg="black", cursor="hand2")
        update_button.place(x=620, y=285, width=110, height=31)

        delete_button = Button(self.main_window, text="Delete", command=self.delete_employee, font=("goudy old style", 15), bg="#f44336", fg="black",
                               cursor="hand2")
        delete_button.place(x=740, y=285, width=110, height=31)

        clear_button = Button(self.main_window, text="Clear", command=self.clear_employee_data, font=("goudy old style", 15), bg="#607d8b", fg="black",
                              cursor="hand2")
        clear_button.place(x=860, y=285, width=110, height=31)

    def create_employee_table(self, frame):
        # Employee scrollbar
        employee_scroll_x = Scrollbar(frame, orient=HORIZONTAL)
        employee_scroll_y = Scrollbar(frame, orient=VERTICAL)

        # Employee database columns
        self.employee_table = ttk.Treeview(frame, columns=(
            "EmployeeID", "Name", "Email", "Password", "UserType", "Contact", "Birthdate", "Salary", "DateOfJoin",
            "Address"), yscrollcommand=employee_scroll_y.set, xscrollcommand=employee_scroll_x.set)
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_data)

        employee_scroll_x.pack(side=BOTTOM, fill=X)
        employee_scroll_y.pack(side=RIGHT, fill=Y)
        employee_scroll_x.config(command=self.employee_table.xview)
        employee_scroll_y.config(command=self.employee_table.yview)

        headings = ("EmployeeID", "Name", "Email", "Password", "UserType", "Contact", "Birthdate", "Salary",
                    "DateOfJoin", "Address")

        for heading in headings:
            self.employee_table.heading(heading, text=heading)
            self.employee_table.column(heading, width=100)

        self.employee_table["show"] = "headings"

        # Show employees in the table.
        self.show_employees()

    def create_address_entry(self):
        self.employee_address_text = Text(self.main_window, font=("goudy old style", 15), bg="lightyellow", fg="black")
        self.employee_address_text.place(x=150, y=270, width=300, height=60)

    def add_employee(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.employee_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from Employee where EmployeeID=?", (self.employee_id.get(),))
                row = cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID is already taken", parent=self.main_window)
                else:
                    cursor.execute("Insert into Employee (EmployeeID, Name, Email, Password, UserType, Contact, "
                                   "Birthdate, Salary, DateOfJoin, Address) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
                                   (self.employee_id.get(), self.employee_name.get(), self.employee_email.get(),
                                    self.employee_password.get(), self.employee_user_type.get(),
                                    self.employee_contact.get(), self.employee_birthdate.get(), self.employee_salary.get(),
                                    self.employee_date_of_join.get(), self.employee_address_text.get("1.0", END)))
                    db_connection.commit()
                    messagebox.showinfo("Success", "Employee added successfully.", parent=self.main_window)
                    self.show_employees()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def show_employees(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            cursor.execute("Select * from Employee")
            rows = cursor.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())

            for row in rows:
                self.employee_table.insert('', END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def get_data(self, event):
        focus_employee_table = self.employee_table.focus()
        content = self.employee_table.item(focus_employee_table)
        row = content["values"]

        # Show data of employee once clicked on an employee.
        self.employee_id.set(row[0])
        self.employee_name.set(row[1])
        self.employee_email.set(row[2])
        self.employee_password.set(row[3])
        self.employee_user_type.set(row[4])
        self.employee_contact.set(row[5])
        self.employee_birthdate.set(row[6])
        self.employee_salary.set(row[7])
        self.employee_date_of_join.set(row[8])
        self.employee_address_text.delete("1.0", END)
        self.employee_address_text.insert(END, row[9])

    def update_employee(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.employee_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from Employee where EmployeeID=?", (self.employee_id.get(),))
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID!", parent=self.main_window)
                else:
                    cursor.execute("Update Employee set Name=?, Email=?, Password=?, UserType=?, Contact=?, "
                                   "Birthdate=?, Salary=?, DateOfJoin=?, Address=? where EmployeeID=?",
                                   (self.employee_name.get(), self.employee_email.get(), self.employee_password.get(),
                                    self.employee_user_type.get(), self.employee_contact.get(),
                                    self.employee_birthdate.get(), self.employee_salary.get(),
                                    self.employee_date_of_join.get(), self.employee_address_text.get("1.0", END),
                                    self.employee_id.get()))
                    db_connection.commit()
                    messagebox.showinfo("Success", "Employee updated successfully.", parent=self.main_window)
                    self.show_employees()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def delete_employee(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.employee_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from Employee where EmployeeID=?", (self.employee_id.get(),))
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Employee ID is required!", parent=self.main_window)
                else:
                    cursor.execute("Select * from Employee where EmployeeID=?", (self.employee_id.get(),))
                    row = cursor.fetchone()
                    if row is None:
                        messagebox.showerror("Error", "Invalid Employee ID!", parent=self.main_window)
                    else:
                        confirm = messagebox.askyesno("Confirm", "Do you really want to delete?",
                                                      parent=self.main_window)
                        if confirm:
                            cursor.execute("delete from Employee where EmployeeID=?", (self.employee_id.get(),))
                            db_connection.commit()
                            messagebox.showinfo("Delete", "Employee deleted successfully", parent=self.main_window)
                        self.clear_employee_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def clear_employee_data(self):
        # Show data of employee once clicked on an employee.
        self.employee_id.set("")
        self.employee_name.set("")
        self.employee_email.set("")
        self.employee_password.set("")
        self.employee_user_type.set("Admin")
        self.employee_contact.set("")
        self.employee_birthdate.set("")
        self.employee_salary.set("")
        self.employee_date_of_join.set("")
        self.employee_address_text.delete("1.0", END)
        self.search_text.set("")
        self.search_by.set("Select")

        self.show_employees()

    def search_employee(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.search_by.get() == "Search":
                messagebox.showerror("Error", "Select an option please.", parent=self.main_window)
            elif self.search_text.get() == "":
                messagebox.showerror("Error", "Search input is required!", parent=self.main_window)
            else:
                cursor.execute("Select * from Employee where " + self.search_by.get() + " LIKE '%" +
                               self.search_text.get() + "%'")
                rows = cursor.fetchall()

                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for row in rows:
                        self.employee_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.main_window)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)


if __name__ == '__main__':
    app = Tk()
    employee_instance = Employee(app)
    app.mainloop()
