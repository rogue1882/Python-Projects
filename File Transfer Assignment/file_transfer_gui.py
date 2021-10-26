


from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd

# Be sure to import our other modules 
# so we can have access to them
import File_Transfer_Main
import file_transfer_func



def load_gui(self):
   
    self.btn_sfile = tk.Button(self.master,text='Source Folder Name:',command=lambda: file_transfer_func.choose_location_source(self))
    self.btn_sfile.grid(row=0,column=0,padx=(27,0),pady=(10,10),sticky=N+W)
    self.btn_dfile = tk.Button(self.master,text='Destination Folder Name:',command=lambda: file_transfer_func.choose_location_destination(self))
    self.btn_dfile.grid(row=2,column=0,padx=(27,0),pady=(10,10),sticky=N+W)


    self.txt_sfile = tk.Entry(self.master,text= '')
    self.txt_sfile.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_dfile = tk.Entry(self.master,text='')
    self.txt_dfile.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
  

    

    
    self.btn_filelist = tk.Button(self.master,width=12,height=2,text='File Transfer',command=lambda: file_transfer_func.GetDailyFiles)
    self.btn_filelist.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: file_transfer_func.ask_quit(self))
    self.btn_close.grid(row=8,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

   

    



if __name__ == "__main__":
    pass
