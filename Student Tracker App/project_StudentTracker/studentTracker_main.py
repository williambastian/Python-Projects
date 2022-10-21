##Python Version: 3.10.7
##
##Author: William Bastian
##
##Purpose: Demonstrate Tkinter, sqlite3, OOP by creating basic student tracker app
##
##Requirements: Page title is "Student Tracking"
##                Contains form to submit student info
##                    First Name
##                    Last Name
##                    Phone number
##                    Email
##                    Current Course
##                    Submit Button
##                Contains section to display students with all info above
##                Delete button, which deletes selected student

##Tested OS: This code was written and tested on Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# modules created for studentTracker project
import studentTracker_gui
import studentTracker_func

# the class for our primary gui window, which inherits from Tkinter Frame
class TrackerWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # TrackerWindow config
        self.master = master
        self.master.minsize(600, 400) #Height, Width
        self.master.maxsize(600, 400) #Window will not re-size
        # center window on screen
        studentTracker_func.center_window(self, 600, 400)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F3e888")
        # built-in tkinter method .protocol() will catch if
        # user clicks X to close window
        self.master.protocol("WM_DELETE_WINDOW", lambda: studentTracker_func.ask_quit(self))
        arg = self.master

        # load GUI functionality from separate module
        studentTracker_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = TrackerWindow(root)
    root.mainloop()
        
        
