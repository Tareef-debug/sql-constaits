import sqlite3

conn = sqlite3.connect('database.sqlite')

conn.execute("DROP TABLE IF EXISTS CLASS_10;")

print("Opened Database successfully")

conn.execute('''CREATE TABLE CLASS_10(SNO INT PRIMARY KEY NOT NULL,Roll_No INT NOT NULL,NAME TEXT NOT NULL,AGE INT DEFAULT (15),GENDER TEXT NOT NULL,Email_ID TEXT NOT NULL,Contact_No Real NOT NULL);''')
print("Table created Successfully")

conn.execute("INSERT INTO CLASS_10(SNO,ROLL_No,NAME,AGE,Gender,Email_ID,Contact_No) VALUES (1, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8080900)");

conn.execute("INSERT INTO CLASS_10(SNO,ROLL_No,NAME,AGE,Gender,Email_ID,Contact_No) VALUES (2, 2, 'Aisha', 14, 'Female', 'aisha@gmail.com', 9080900)");

conn.execute("INSERT INTO CLASS_10(SNO,ROLL_No,NAME,AGE,Gender,Email_ID,Contact_No) VALUES (3, 3, 'Jeff', 15, 'Male', 'jeff@gmail.com', 9900900)");

conn.commit()
print("Records created successfully")

import pandas as pd
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type ='table';""",conn)

tables

class_10d = pd.read_sql("""SELECT * FROM CLASS_10;""",conn)

class_10d.head()

print(tables)
print(class_10d.head)