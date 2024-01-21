import sqlite3

# create a table called simple db and connect to it
connection = sqlite3.connect('sample.db')

# create a table
table = 'CREATE TABLE people ( id integer primary key, name TEXT, surname TEXT )'
cursor = connection.cursor()
cursor.execute(table)
connection.commit()
