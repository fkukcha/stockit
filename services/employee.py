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
        self.employee_name = StringVar()
        self.employee_date_of_birth = StringVar()
        self.employee_date_of_join = StringVar()
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
        search_button = Button(search_label_frame, text="Search", font=("goudy old style", 15), bg="#4caf50",
                               fg="white", cursor="hand2")
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
        employee_name_label = Label(self.main_window, text="Name", font=("goudy old style", 15), bg="white", fg="black")
        employee_name_label.place(x=750, y=150)


if __name__ == '__main__':
    app = Tk()
    employee_instance = Employee(app)
    app.mainloop()
