## Goals of script:
## 1) Create new db using sqlite3 module

## 2) Create table in new db with two fields: an auto-increment ID primary key,
##      and a text field for qualifying file names from a given tuple.

## 3) Read from given tuple, enter values with .txt file extension into table,
##      and then print the qualifying file names to the console.
##


## First step, import sqlite3 module
import sqlite3


##Use sqlite3.connect to create new db
conn = sqlite3.connect('db_fileList.db')


## use .cursor() method to create cur as a cursor object
## using cur as a cursor object, SQL commands can be executed with
##  .execute() method
## SQL commands create table, the primary key column, and the fileName column
## the .commit() method commits the current transaction to the new database
## the .close() method closes the database connection to prevent memory leaks


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        FILE_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()

## reconnect to new database
conn = sqlite3.connect('db_fileList.db')


## declare fileList as the given tuple of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


## this for loop iterates through each value in the tuple,
##  and if a value ends with .txt, uses the cur cursor object to execute a
##  SQL INSERT command, only if the file extension qualifies

##  "VALUES(?)", (x,))" is a series of characters that specifies x, or any
##  qualifying value in the tuple, will be placed into the EXECUTE command, where
##  "?" is a placeholder for qualifying values of x

##  the print() statement also uses a placeholder "{}" for any qualifying values of x


for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_Files (col_fileName) VALUES(?)", (x,))
            print("File Name: {}".format(x))
conn.close()
## close db connection again after all commands are complete
