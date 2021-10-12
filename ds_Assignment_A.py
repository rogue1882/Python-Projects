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
# Supplied files listed in a string

    fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt',\
                'data.pdf', 'myPhoto.jpg')
    newfileList= [a for a in fileList if "txt" in a]
    print(newfileList)
   
    

    
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
     

  

conn.close()




   
 
