

import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import glob
import datetime
import shutil




# Be sure to import our other modules 
# so we can have access to them
import File_Transfer_Main
import file_transfer_gui



def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
  



def choose_location_source(self):
        """
        Shows a popup window to select a directory to choose save the lists generated. then sends the path to
        GetDailtFiles Origin."""


        self.sourcepath = fd.askdirectory(title="Choose directory",
                                       initialdir="\home",
                                       mustexist=True)

        #add path to text box
        self.txt_sfile.insert(0, self.sourcepath)

        



def choose_location_destination(self):
        """
        Shows a popup window to select a directory to choose save the lists generated. then sends the path to
        GetDailyFiles Destination."""


        self.destinationpath = fd.askdirectory(title="Choose directory",
                                       initialdir="\home",
                                       mustexist=True)
        #add path to text box
        self.txt_dfile.insert(0, self.destinationpath)
        
       

def GetDailyFiles(self):
    #gets the path to source folder 
    source = self.txt_sfile.get()
    
    #gets the path to destination folder
    destination = self.txt_dfile.get()

    # Create list of text filenames in source folder
    fileList = os.listdir(source)

    #iterates through the list of files
    for file in fileList:

        """ Joins the source folder and file name
        to get absolute path"""
        source_file = os.path.join(source, file)

        # Get last modified date and time
        modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(source_file))
        # gets the current date and time
        todaysDate = datetime.datetime.now()
        # gets the current date and tiem 24 hours ago
        twentyfour = todaysDate - datetime.timedelta(hours=24)
 
        # If the file was edited less then 24 hours ago then move it
        if modifyDate > twentyfour:
            shutil.move(source_file, destination)

        
        




    


   


if __name__ == "__main__":
    pass
