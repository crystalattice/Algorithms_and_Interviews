import sqlite3

connection = sqlite3.connect("Customers.db")  # The .db extension is optional
cursor = connection.cursor()  # Executes SQL queries

# Alternative DB created only in memory
# mem_conn = sqlite3.connect(":memory:")
# cursor = mem_conn.cursor()

# Create the table to hold entries
cursor.execute("""
CREATE TABLE Customers
	(id INTEGER PRIMARY KEY,
	LName TEXT,
	FName TEXT,
	Address TEXT,
	City TEXT,
	State TEXT)
""")

cursor.execute("""
CREATE TABLE Orders
	(id INTEGER PRIMARY KEY,
	Item_title TEXT,
	Price FLOAT,
	Order_Number INTEGER,
	customer_id INTEGER,
	FOREIGN KEY (customer_id) REFERENCES Customers(id))
""")


def customer_insert(last_name, first_name, address, city, state):
	sql = "INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?)"
	cursor.execute(sql, (None, last_name, first_name, address, city, state))
	return cursor.lastrowid  # Get ID of object


def order_insert(item, price, order_num, customer_id):
	sql = "INSERT INTO Orders VALUES (?, ?, ?, ?, ?)"
	cursor.execute(sql, (None, item, price, order_num, customer_id))
	return cursor.lastrowid


johnson_id = customer_insert("Johnson", "Jack", "123 Easy St.", "Anywhere", "CA")
johnson_order1 = order_insert("Boots", 55.50, 4455, johnson_id)
johnson_order2 = order_insert("Shirt", 16.00, 4455, johnson_id)
johnson_order3 = order_insert("Pants", 33.00, 7690, johnson_id)

smith_id = customer_insert("Smith", "John", "312 Hard St.", "Somewhere", "NY")
smith_order1 = order_insert("Shoes", 23.99, 3490, smith_id)
smith_order2 = order_insert("Shoes", 65.00, 5512, smith_id)

connection.commit()  # Write data to database
cursor.close()  # Close database
