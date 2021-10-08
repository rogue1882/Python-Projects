import sqlite3

conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_filename FROM tbl_files WHERE col_filename = '{}.txt' ")
    varTXT = cur.fetchall()
    for item in varTXT:
        msg = "FILE: {}".format(item[0], item[1])
    print(msg) 
