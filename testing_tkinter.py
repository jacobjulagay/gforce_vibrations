from tkinter import *
from tkinter import filedialog
from sys import exit

#Creating the root root
root = Tk()

# Opening file explorer
# Make sure the initial dir will be set to C: drive.
def viewFiles():
    filename = filedialog.askopenfilename(initialdir= "C:/Users/jacob/Documents/krowpu", 
                                        title="Select a Excel File",
                                        filetypes = (("csv files","*.csv*"),("all files",
                                                        "*.*"), ))
    #Change label contents 
    label_file_explorer.configure(text = "File Opened: " + filename)


root.geometry("500x500")
# Set root title
root.title('File Explorer')

# Set root background color
root.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(root, text = "Select report",width = 70, height = 4,fg = "blue")
label_file_explorer.pack()

# Input Box
e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter your start date: ")
e.get() # Gets the value of the written thing

# Browse files button
button_explore = Button(root,text = "Browse Files",command = viewFiles)
button_explore.pack()
# Exit button
button_exit = Button(root, text = "Exit", command = exit)
button_exit.pack()

root.mainloop()
exit()