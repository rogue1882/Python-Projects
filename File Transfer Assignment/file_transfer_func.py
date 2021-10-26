

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


        self.txt_sfile.insert(0, self.sourcepath)

        



def choose_location_destination(self):
        """
        Shows a popup window to select a directory to choose save the lists generated. then sends the path to
        GetDailyFiles Destination."""


        self.destinationpath = fd.askdirectory(title="Choose directory",
                                       initialdir="\home",
                                       mustexist=True)

        self.txt_dfile.insert(0, self.destinationpath)
        
       

def GetDailyFiles( path, type):
    
    #Return a list of filename matching the given path and file type
    
    return glob.glob(path + "*" + type)

    
    



    # Create list of text filenames in Origin folder
    fileList = GetDailyFiles(self.txt_sfile, type)

    for file in fileList:
        # Get last modified date and today's date
        modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        todaysDate = datetime.datetime.today()
        
        filePathList = self.sourcepath
        filename = filePathList # The last element is the filename
        
        # If modified within last 24 hours, then copy to destination folder
        modifyDateLimit = modifyDate + datetime.timedelta(days=1)

        # If the file was edited less then 24 hours ago then move it
        if modifyDateLimit > todaysDate:
            shutil.move(file, self.txt_dfile + filename)

        
        




    


   


if __name__ == "__main__":
    pass
