import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta
import time


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")
        # Create button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # Position button using tkinter grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        # Create entry for source directory selection
        self.source_dir = Entry(width=75)
        # Position entry using tkinter grid, align with button
        self.source_dir.grid(row=0, column = 1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Create and position button to select file destination
        self.destDir_btn = Button(text="Select Destination", width = 20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Create and position entry field for file destination
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #Create button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #position transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Create exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #position exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

        


#function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content in the Entry widget.
        # This allows the path to be entered into the Entry widget properly.
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir directory
        self.source_dir.insert(0, selectSourceDir)


#function to select destination
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)
        
#function to transfer files from source to destination
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination
        destination = self.destination_dir.get()
        #gets list of files in the source directory
        source_files = os.listdir(source)
        #set current time in seconds since epoch
        currentTime = time.time()
        oneDaySeconds = timedelta(days=1).total_seconds()
        
        # iterates through each file in source directory
        for i in source_files:
            ##Functionality to only move files modified in previous 24 hours:
            
            ## os.path.getmtime returns time in seconds from epoch when
            ## file was last modified.
            
            ## os.path.getmtime requires full file path, so concatenate
            ## "source" variable, which is the directory path, with i,
            ## the name of any given file in the directory.
            
            ## Then, to determine if changes occurred within last 24 hours,
            ## subtract modTime from currentTime, which returns the
            ## number of seconds between now and the most recent modification.

            ## The oneDaySeconds value uses timedelta().total_seconds() to represent 24 hours
            ## in seconds.
            ## If the difference between the currentTime and the modTime is
            ## less than oneDaySeconds, it is newer than 24 hours, and should
            ## be transferred. If less, do not transfer.
            


            ## Print confirmation of transfer to console, or, print confirmation
            ## of file not transferred.
            
            modTime = os.path.getmtime(source + '/' + i)
            
            if ((currentTime - modTime) < oneDaySeconds):
                #moves each file from source to destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')
            else:
                print(i +  ' not moved: no recent changes.')

#function to exit program
    def exit_program(self):
        #root is the main GUI window. the .destroy method tells python
        # to terminate root.mainloop and all widgets in the GUI window
        root.destroy()









if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
