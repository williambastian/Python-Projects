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

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

import studentTracker_main
import studentTracker_gui


def center_window(self, w, h): #pass in tkinter frame class, width, height
    # get screen dimensions from user
    screenWidth = self.master.winfo_screenwidth()
    screenHeight = self.master.winfo_screenheight()
    # locate window at center of user screen
    x = int((screenWidth/2) - (w/2))
    y = int((screenHeight/2) - (h/2))
    centerGUI = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGUI

# double check if user wants to close window
def ask_quit(self):
    if messagebox.askokcancel("Exit Student Tracker", "Okay to exit Student Tracker?"):
        self.master.destroy()
        os._exit(0)

# database functionality
def createDB(self):
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?,?,?,?,?,?)""", ('John', 'Placeholder', 'John Placeholder', '000-000-0000','placeholder@mail.com','Python Course'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur, count

#select entry from list window
def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email, col_course FROM tbl_students WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # a tuple is returned, which can then be sliced using data[]
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def addEntry(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize data
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname, var_lname))
    print("var_fullname: {}".format(var_fullname)) 
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip().title()

    if not "@" or not "." in var_email:
        print("Please enter a valid email address")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('db_studentTracker.db')
        with conn:
            cursor = conn.cursor()
            # check db for existence of fullname. If it already exists, alert user and disregard request.
            # upgrade to functionality: generate a check against more robust combination of fields (full name, address, phone number)
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if chkName is 0 then the fullname does not exist; new data can be added
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?,?,?,?,?,?)""", (var_fname, var_lname, var_fullname, var_phone, var_email, var_course))
                self.lstList1.insert(END, var_fullname) #update list window with new fullname
                onClear(self) #call function to clear all text fields
            else:
                messagebox.showerror("Error: ", "'{}' already exists in the database. Please choose a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Error: ", "Please complete all required fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #Value selected in list window
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cur = conn.cursor()
        # check count to make sure this is not last record in db.
        # trying to delete final record will cause error
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Confirm: Delete Record", "All information associated with ({}) \nwill be permanently deleted from the database. \n\nDelete this record permanently?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_studentTracker.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) #this function clears all text fields, refreshes list window
                conn.commit()
            else:
                confirm = messagebox.showerror("Error: Last Record Deletion Attempt", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
        conn.close()

def onDeleted(self):
    #clear text in entry fields
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear text in these fields
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

def onRefresh(self):
    # populate list window
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("""SELECT col_fullname FROM tbl_students""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.lstList1.insert(0,str(item))
                    i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] #index of list selection
        var_value = self.lstList1.get(var_select) # list selection text value
    except:
        messagebox.showinfo("Missing Selection","No name was selected from the list. \nCancelling request to update.")
        return
    # The user will only be allowed to update changes for phone, email, and current course
    # Name changes will require deleting and remaking entire record
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0): #ensure data is present in fields
        conn = sqlite3.connect('db_studentTracker.db')
        with conn:
            cur = conn.cursor()
            # count records to see if user's changes are already in db, meaning no updates needed
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_students WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_students WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            cur.execute("""SELECT COUNT(col_course) FROM tbl_students WHERE col_course = '{}'""".format(var_course))
            count3 = cur.fetchone()[0]
            print(count3)
            if count == 0 or count2 == 0 or count3 ==0: #if proposed changes not already in db, proceed
                response = messagebox.askokcancel("Update Request","The following changes, ({}) ({}) ({}), will be implemented for ({}). \n\nProceed with the update request?".format(var_phone, var_email, var_course, var_value))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_students SET col_phone = '{0}',col_email = '{1}',col_course = '{2}' WHERE col_fullname = '{3}'""".format(var_phone,var_email,var_course,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected.","({}), ({}), and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone,var_email, var_course))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone, email, or course information.")
    onClear(self)



if __name__ == "__main__":
    pass

    
        
    
