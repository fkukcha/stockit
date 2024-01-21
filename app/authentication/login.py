from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import sys


class Login:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("User Authentication")
        self.main_window.geometry("1350x700+0+0")
        self.main_window.config(bg="#fafafa")

        # Phone image
        self.phone_image = ImageTk.PhotoImage(file="../../images/phone.png")
        self.phone_image_label = Label(self.main_window, image=self.phone_image, bd=0)
        self.phone_image_label.place(x=200, y=50)

        # Login frame
        login_frame = Frame(self.main_window, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        # Title
        title = Label(login_frame, text="Login to StockIT", font=("Elephant", 30, "bold"), bg="white")
        title.place(x=0, y=30, relwidth=1)

        # Username
        self.employee_id = StringVar()
        user_label = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171")
        user_label.place(x=50, y=100)
        username_text = Entry(login_frame, textvariable=self.employee_id, font=("times new roman", 15), bg="#ECECEC")
        username_text.place(x=50, y=140, width=250)

        # Password
        self.password = StringVar()
        password_label = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171")
        password_label.place(x=50, y=200)
        password_text = Entry(
            login_frame, textvariable=self.password, show="*", font=("times new roman", 15), bg="#ECECEC")
        password_text.place(x=50, y=240, width=250)

        # Login button
        login_button = Button(
            login_frame, command=self.login, text="Login", font=("Arial Rounded MT Bold", 15), bg="#00B0F0",
            activebackground="#00B0F0", fg="white", activeforeground="white", cursor="hand2")
        login_button.place(x=50, y=300, width=250, height=35)

        # Horizontal line
        horizontal_line = Label(login_frame, bg="lightgray")
        horizontal_line.place(x=50, y=370, width=250, height=2)

        # OR horizontal_line
        or_horizontal_line = Label(login_frame, text="OR", bg="white", fg="lightgray",
                                   font=("times new roman", 15, "bold"))
        or_horizontal_line.place(x=150, y=355)

        # Forget password button
        forget_password_button = Button(
            login_frame, text="Forgot Password?", command=self.forget_password_form, font=("times new roman", 13),
            bg="white", fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E")
        forget_password_button.place(x=100, y=390)

        # Register frame
        register_frame = Frame(self.main_window, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=650, y=570, width=350, height=60)

        # Register label
        register_label = Label(
            register_frame, text="SUBSCRIBE | LIKE | SHARE", font=("times new roman", 13), bg="white")
        register_label.place(x=0, y=20, relwidth=1)

        # Login images animation
        self.image_1 = ImageTk.PhotoImage(file="../../images/im1.png")
        self.image_2 = ImageTk.PhotoImage(file="../../images/im2.png")
        self.image_3 = ImageTk.PhotoImage(file="../../images/im3.png")

        self.animation_image_label = Label(self.main_window, bg="white")
        self.animation_image_label.place(x=367, y=153, width=240, height=428)

        # Animate images
        self.animate()

    def animate(self):
        self.animate_image = self.image_1
        self.image_1 = self.image_2
        self.image_2 = self.image_3
        self.image_3 = self.animate_image

        self.animation_image_label.config(image=self.animate_image)
        self.animation_image_label.after(2000, self.animate)

    def login(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()

        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required!", parent=self.main_window)
            else:
                cursor.execute("select UserType from Employee where EmployeeID=? AND Password=?",
                               (self.employee_id.get(), self.password.get()))
                user = cursor.fetchone()
                if user is None:
                    messagebox.showerror("Error", "Invalid Employee ID or Password", parent=self.main_window)
                else:
                    if user[0] == "Admin":
                        print(user)
                        self.main_window.destroy()
                        current_dir = os.path.dirname(os.path.realpath(__file__))
                        parent_dir = os.path.dirname(current_dir)
                        dashboard_path = os.path.join(parent_dir, "services/dashboard.py")
                        os.system(f"{sys.executable} {dashboard_path}")
                    else:
                        self.main_window.destroy()
                        current_dir = os.path.dirname(os.path.realpath(__file__))
                        parent_dir = os.path.dirname(current_dir)
                        dashboard_path = os.path.join(parent_dir, "services/billing.py")
                        os.system(f"{sys.executable} {dashboard_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)

    def forget_password_form(self):
        db_connection = sqlite3.connect(database=r"../../db/stockit.db")
        cursor = db_connection.cursor()
        try:
            if self.employee_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=self.main_window)
            else:
                cursor.execute("select Email from Employee where EmployeeID=?", (self.employee_id.get(),))
                email = cursor.fetchone()

                if email is None:
                    messagebox.showerror("Error", "Invalid Employee ID, please try again", parent=self.main_window)
                else:
                    self.reset_password = StringVar()
                    self.new_password = StringVar()
                    self.confirm_password = StringVar()

                    self.forget_password_window = Toplevel(self.main_window)
                    self.forget_password_window.title("RESET PASSWORD")
                    self.forget_password_window.geometry("400x350+500+100")
                    self.forget_password_window.focus_force()

                    title = Label(
                        self.forget_password_window, text="Reset Password", font=("goudy old style", 15, "bold"),
                        bg="#3f51b5", fg="white")
                    title.pack(side=TOP, fill=X)

                    reset_label = Label(
                        self.forget_password_window, text="Password reset email sent.", font=("times new roman", 15),
                        bg="#3f51b5", fg="white"
                    )
                    reset_label.place(x=20, y=60)

                    reset_text = Entry(
                        self.forget_password_window, textvariable=self.reset_password, font=("times new roman", 15),
                        bg="lightyellow"
                    )
                    reset_text.place(x=20, y=100, width=250, height=30)

                    self.reset_button = Button(
                        self.forget_password_window, text="SUBMIT", font=("times new roman", 15), bg="lightblue")
                    self.reset_button.place(x=280, y=100, width=100, height=30)

                    new_pwd = Label(
                        self.forget_password_window, text="New Password", font=("times new roman", 15), bg="#3f51b5",
                        fg="white"
                    )
                    new_pwd.place(x=20, y=160)

                    new_pwd_text = Entry(
                        self.forget_password_window, textvariable=self.new_password, font=("times new roman", 15),
                        bg="lightyellow"
                    )
                    new_pwd_text.place(x=20, y=190, width=250, height=30)

                    confirm_pwd = Label(
                        self.forget_password_window, text="Confirm Password", font=("times new roman", 15),
                        bg="#3f51b5", fg="white"
                    )
                    confirm_pwd.place(x=20, y=225)

                    confirm_pwd_text = Entry(
                        self.forget_password_window, textvariable=self.confirm_password, font=("times new roman", 15),
                        bg="lightyellow"
                    )
                    confirm_pwd_text.place(x=20, y=255, width=250, height=30)

                    self.update_button = Button(
                        self.forget_password_window, text="Update", state=DISABLED, font=("times new roman", 15),
                        bg="lightblue"
                    )
                    self.update_button.place(x=150, y=300, width=100, height=30)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.main_window)


if __name__ == '__main__':
    app = Tk()
    login_instance = Login(app)
    app.mainloop()
