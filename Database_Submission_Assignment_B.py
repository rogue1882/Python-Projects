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
# Supplied files listed in a string

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt',\
                'data.pdf', 'myPhoto.jpg')

#Loops through finding files with .txt to add
for x in fileList:
       if x.endswith('.txt'):
           with conn:
               cur = conn.cursor()
               # inserts the defind files to db

               cur.execute("INSERT INTO tbl_files(col_filename) VALUES (?)", (x,))
               print(x)
   
    

    

conn.close()

   


   
 
