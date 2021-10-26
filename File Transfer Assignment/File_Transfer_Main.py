
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog


import shutil
import os
import glob
import datetime

import file_transfer_gui
import file_transfer_func

#set where the source of the files are
source = '/Users/rogue/OneDrive/Desktop/Python-Projects/File Transfer Assignment/Folder A/'

#set the destination path to folder B
destination = '/Users/rogue/OneDrive/Desktop/Python-Projects/File Transfer Assignment/Folder B/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

    

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        file_transfer_func.center_window(self,500,300)
        self.master.title("Daily File Transfer")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_transfer_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        file_transfer_gui.load_gui(self)
      

        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
























