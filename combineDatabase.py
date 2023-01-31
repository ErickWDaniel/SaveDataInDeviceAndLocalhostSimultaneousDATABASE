import sqlite3 as sc
import mysql.connector as mc
#Written by Erick Wilfred
ConnectDeviceDB = sc.connect("erickDbDevice.db")
our_cursor_readerDevice = ConnectDeviceDB.cursor()
our_cursor_readerDevice.execute('CREATE TABLE IF NOT EXISTS users(ID INTEGER PRIMARYKEY AUTO INCREMENT,NAME TEXT,AGE INTEGER)')
our_cursor_readerDevice.execute('INSERT INTO users(NAME,AGE) VALUES("Erick Wilfred",38)')
our_cursor_readerDevice.execute('INSERT INTO users(NAME,AGE) VALUES("Mbise Kilakoi",53)')
our_cursor_readerDevice.execute('INSERT INTO users(NAME,AGE) VALUES("Lulu Ally",85)')
ConnectDeviceDB.commit()
our_cursor_readerDevice.execute("SELECT * FROM users")
rows = our_cursor_readerDevice.fetchall()

ConnectLocalhostDB = mc.connect(
    host="localhost",
    user="root",
    database="erickDb"  #this database is stored in localhost
)
our_cursor_readerLocalhost = ConnectLocalhostDB.cursor()

for row in rows:
    id, name, age = row
    our_cursor_readerLocalhost.execute("INSERT INTO users (ID, NAME, AGE) VALUES (%s, %s, %s)", (id, name, age))

ConnectLocalhostDB.commit()
ConnectDeviceDB.close()
ConnectLocalhostDB.close()
