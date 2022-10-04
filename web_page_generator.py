#import the necessary modules for tkinter gui and webbrowser functionality
import tkinter as tk
from tkinter import *
import webbrowser


#define the parent window / gui frame
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #Window title
        self.master.title("Web Page Generator")
        #Label and configuration for text entry field
        self.labelEntry = tk.Label(self.master, text = "Enter custom text or click the Default HTML page button")
        self.labelEntry.grid(row = 0, column = 0, padx=(30, 10), pady=(30, 0))
        self.textEntry = Entry(width = 120)
        self.textEntry.grid(row = 1, column = 0, columnspan=4, padx=(10, 10), pady=(30, 0))
        #Configure and position the buttons for default HTML, and custom text
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row = 2, column = 1, pady=(10,10))
        self.btnCustom = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customText)
        self.btnCustom.grid(row = 2, column = 2, padx=(10,40), pady=(10,10))

#define behavior for default HTML button
    def defaultHTML(self):
        #text to be placed within HTML element
        htmlText = "Stay tuned for our amazing summer sale!"
        #opens file for writing: "index.html" will be file name, "w" specifies file will be written to
        htmlFile = open("index.html", "w")
        #tag formatting, and concatenation of htmlText
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        #htmlFile.write() writes the content in parentheses, htmlContent, to the file designated in htmlFile, "index.html"
        htmlFile.write(htmlContent)
        #closes htmlFile
        htmlFile.close()
        #opens index.html in new tab, using default browser
        webbrowser.open_new_tab("index.html")

#behavior for customText is mostly the same, except for cusText
    def customText(self):
        # self.textEntry is the field for text entry created in the GUI window
        # the .get() method gets any text entered into that field
        # this is stored in the cusText variable
        cusText = self.textEntry.get()
        cusFile = open("index.html", "w")
        #This time we use cusText, which is any user-entered text in the entry field
        cusContent = "<html>\n<body>\n<h1>" + cusText + "</h1>\n</body>\n</html>"
        cusFile.write(cusContent)
        cusFile.close()
        webbrowser.open_new_tab("index.html")
        





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
