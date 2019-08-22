import sqlite3

connection = sqlite3.connect("Tools.db")  # The .db extension is optional
cursor = connection.cursor()  # Executes SQL queries

# Alternative DB created only in memory
# mem_conn = sqlite3.connect(":memory:")
# cursor = mem_conn.cursor()

# Create the table to hold entries
cursor.execute("""
CREATE TABLE Tools
(id INTEGER PRIMARY KEY,
name TEXT,
size TEXT,
price INTEGER)
""")

# Populate table
for item in (
		(None, "Box Knife", "Small", 15),
		(None, "Drill", "Medium", 35),
		(None, "Axe", "Large", 55),
		(None, "Putty Knife", "Small", 25),
		(None, "Hammer", "Small", 25),
		(None, "Screwdriver", "Small", 10),
		(None, "Crowbar", "Large", 60),
		):
	cursor.execute("INSERT INTO Tools VALUES (?, ?, ?, ?)", item)

connection.commit()  # Write data to database
cursor.close()  # Close database
