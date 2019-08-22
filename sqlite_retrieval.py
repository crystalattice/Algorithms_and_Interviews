import sqlite3
import pprint

connection = sqlite3.connect("Tools.db")
cursor = connection.cursor()

# cursor.execute("SELECT name, size, price FROM Tools")
# toolsTuple = cursor.fetchall()
# for entry in toolsTuple:
#     name, size, price = entry  # Unpack the tuples
#     item = ("{}, {}, {}".format(name, size, price))
#     print(item)
cursor.execute("SELECT * FROM Tools")
for row in cursor:
    print ("-" * 10)
    print ("ID:", row[0])
    print ("Name:", row[1])
    print ("Size:", row[2])
    print ("Price:", row[3])
    print ("-" * 10)