# Python with SQL database
def takeInput():
    arr = []
    arr.append(input("Enter name: "))
    arr.append(input("Enter phone number: "))
    arr.append(input("Enter address: "))
    return arr

import sqlite3

# create a datbase object, if doesnt exist, else access it
db = sqlite3.connect("DB1.sqlite")

# create a table
try:
    db.execute("create table student (name text, phone text, address text)")
except:
    pass

# insert rows
db.execute("insert into student values('sam', '998877', 'delhi')")
db.execute("insert into student values('john', '786453', 'pune')")

# list1 = takeInput()
# db.execute("insert into student values (?,?,?)",list1)

db.commit() # -> saves data

# extract data from database
cursor = db.cursor()
cursor.execute("select * from student")

# name = input("Whose data do you want to get: ")
# cursor.execute("select * from student where name = ?", [name])
print(cursor.fetchall())

cursor.close()
db.close()