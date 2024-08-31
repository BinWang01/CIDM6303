# Bin Wang
import csv
import sqlite3

with open("customers.csv", encoding="ISO-8859-1") as file:
    reader = csv.reader(file)
    data = list(reader)

db_name = "chinook.db"
with sqlite3.connect(db_name) as conn:
    sql_command = "INSERT INTO Customers (Company,FirstName,LastName,Address,City,PostalCode,Country,Email) VALUES (?,?,?,?,?,?,?,?)"
    for customer in data:
        customer_values = tuple(customer)
        conn.execute(sql_command, customer_values)
    conn.commit()
