import sqlite3

#Creates DB File

conn = sqlite3.connect('file.db')

#Connects and Creates table tbl_files with col_filename

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename STRING)")
    conn.commit()
# Closes Connection
conn.close()


conn = sqlite3.connect('file.db')

#Connect to insert items into tbl_files

with conn:
    cur = conn.cursor()
# Supplied files list entered into table

    cur.execute("INSERT INTO tbl_files(col_filename)VALUES (?)",('information.docx',))
    cur.execute("INSERT INTO tbl_files(col_filename)VALUES (?)",('Hello.txt',))
    cur.execute("INSERT INTO tbl_files(col_filename)VALUES (?)",('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_files(col_filename)VALUES (?)",('MyImage.png',))
    cur.execute("INSERT INTO tbl_files(col_filename)VALUES (?)",('World.txt',))
    cur.execute("INSERT INTO tbl_files(col_filename)VALUES (?)",('data.pdf',))
    cur.execute("INSERT INTO tbl_files(col_filename)VALUES (?)",('myPhoto.jpg',))
    
    conn.commit()

conn.close()

   
conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_filename FROM tbl_files WHERE col_filename = '{}.txt' ")
    conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_filename FROM tbl_files WHERE col_filename = '{}.txt' ")
    varTXT = cur.fetchall()
    for item in varTXT:
        msg = "filename {}".format(item[1])
    print(msg) 

  

conn.close()




   
 
