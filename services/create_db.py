import sqlite3


def create_db():
    db_connection = sqlite3.connect(database=r"../db/stockit.db")
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS employee(Employee ID INTEGER PRIMARY KEY AUTOINCREMENT, Name text, "
                   "Email text, Password text, User Type text, Contact text, Birthdate text, Salary text, "
                   "Date of Join text)")
    db_connection.commit()


create_db()
