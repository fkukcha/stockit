import sqlite3


def create_db():
    db_connection = sqlite3.connect(database=r"../../db/stockit.db")
    cursor = db_connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Employee(EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT, Name text, "
                   "Email text, Password text, UserType text, Contact text, Birthdate text, Salary text, "
                   "DateOfJoin text, Address text)")
    db_connection.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS Supplier(SupplierInvoiceNum INTEGER PRIMARY KEY AUTOINCREMENT, Name text, "
                   "Contact text, Description text)")
    db_connection.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS Product(PID INTEGER PRIMARY KEY AUTOINCREMENT, Category text, "
                   "Supplier text, Name text, Price text, Qty text, Status text)")
    db_connection.commit()


create_db()
