

import shutil
import os

#set where the source of the files are
source = '/Users/rogue/OneDrive/Desktop/Python-Projects/File Transfer Assignment/Folder A'

#ser the destination path to folder B
destination = '/Users/rogue/OneDrive/Desktop/Python-Projects/File Transfer Assignment/Folder B'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

    

























