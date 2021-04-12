from tkinter import *
from tkinter import filedialog
from sys import exit
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cleaning_data import clean_data,graph_data
import os
from pathlib import Path



#Creating the root root
root = Tk()

# Opening file explorer
# Make sure the initial dir will be set to C: drive.

# To do: adjust file for cleaning_data b/c it's only on 1_22_21
# To do: Issue w/ df only reading 1-22-21 from cleaning_data. 
# Might just put all the classes in one file to reduce issues.  


    
filename = filedialog.askopenfilename(initialdir= "C:/Users/jacob/Documents/krowpu", 
                                        title="Select a Excel File",
                                        filetypes = (("csv files","*.csv*"), ))
    
filepath = filename
path = Path(filepath)
path_name = path.name
#Change label contents 
label_file_explorer = Label(root, text = "Select File",width = 70, height = 4,fg = "Red")
label_file_explorer.pack()
label_file_explorer.configure(text = "File Opened:\n " + path_name)
    

# Creating new dataframe 
def createDF(filename):
    df = pd.read_csv(filename,sep=r'\s*,\s*', engine='python',skiprows = 6)
    return df

# cleaning the dataframe using clean_data()
def newCleanDF(df):
    df = clean_data(df)
    return df

df = createDF(path_name)
clean_df = newCleanDF(df)


root.geometry("500x500")
# Set root title
root.title('File Explorer')

# Create a File Explorer label

# Browse files button
#button_explore = Button(root,text = "Browse Files",command = viewFiles)
#button_explore.pack()

# Input Box - Examples
#e = Entry(root, width = 50)
#e.pack()
#e.insert(0, "Enter your start date: ")
#e.get() # Gets the value of the written thing

# Start Date
start_date_label = Label(root, text="Start Date: ")
start_date_label.pack()
start_date_entry = Entry(root, bd =5,width = 50)
start_date_entry.insert(0, "ex. 2021/01/21")
start_date_entry.pack()
start_date_entry.get()
start_date = start_date_entry.get()


# Start Time
start_time_label = Label(root, text="Start time: ")
start_time_label.pack()
start_time_entry = Entry(root, bd =5,width = 50)
start_time_entry.insert(0, "ex. 09:00:00")
start_time_entry.pack()
start_time_entry.get()
start_time = start_time_entry.get() 

# End Date
end_date_label = Label(root, text="End Date: ")
end_date_label.pack()
end_date_entry = Entry(root, bd =5,width = 50)
end_date_entry.insert(0, "ex. 2021/01/21")
end_date_entry.pack()
end_date_entry.get()
end_date = end_date_entry.get() 

# End time
end_time_label = Label(root, text="End time: ")
end_time_label.pack()
end_time_entry = Entry(root, bd =5,width = 50)
end_time_entry.insert(0, "ex. 10:30:00")
end_time_entry.pack()
end_time_entry.get()
end_time = end_time_entry.get()

# Example click
def myClick():
    start_date = start_date_entry.get()
    start_time = start_time_entry.get() 
    end_date = end_date_entry.get() 
    end_time = end_time_entry.get()
    graph_data(clean_df,start_date,start_time,end_date,end_time)
# Calculate Button
calculate_bttn = Button(root, text="Calculate", command=myClick)
calculate_bttn.pack()


# Restart the program
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

restart_bttn = Button(root, text = "Restart", command = restart_program)
restart_bttn.pack()

# Exit button
button_exit = Button(root, text = "Exit", command = exit)
button_exit.pack()

root.mainloop()
exit()