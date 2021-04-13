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
from time import sleep



#Creating the root root
root = Tk()

# Opening file explorer
# Make sure the initial dir will be set to C: drive.

# To do: adjust file for cleaning_data b/c it's only on 1_22_21
# To do: Issue w/ df only reading 1-22-21 from cleaning_data. 
# Might just put all the classes in one file to reduce issues.  


    
filename = filedialog.askopenfilename(
                                        title="Select a Excel File",
                                        filetypes = (("csv files","*.csv"), ("all files","*.*"),))


# Getting the file name from the directory    
filepath = filename
path = Path(filepath)
path_name = path.name
#Change label contents 
label_file_explorer = Label(root, text = "Select File", height = 4,fg = "blue", font='Roboto 15 bold')
#label_file_explorer.pack()
label_file_explorer.configure(text = "File Opened:\n " + path_name)
label_file_explorer.grid(row = 0, column =1, sticky = W, pady = 5)    

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


root.title('File Explorer')

# Create a File Explorer label

# Browse files button
#button_explore = Button(root,text = "Browse Files",command = viewFiles)
#button_explore.pack()


# Start Date
start_date_label = Label(root, text="Start Date: ", font='Roboto 15 bold')
start_date_label.grid(row = 1, column =0,padx = 5 )
end_date_label_ex =  Label(root, text = "Ex. 2021/01/21", font='Roboto 15 bold')
end_date_label_ex.grid(row= 1,column=2,sticky = W)
start_date_entry = Entry(root, bd =3,width = 40, font ='Roboto 15 bold' )
start_date_entry.grid(row=1, column = 1, sticky = W)
start_date_entry.get()
start_date = start_date_entry.get()


# Start Time
start_time_label = Label(root, text="Start Time: ", font='Roboto 15 bold')
start_time_label.grid(row = 2, column = 0, pady = 5)
start_time_label_ex =  Label(root, text = "Ex. 09:00:00", font='Roboto 15 bold')
start_time_label_ex.grid(row= 2,column=2,sticky = W)
start_time_entry = Entry(root, bd =3,width = 40,  font='Roboto 15 bold')
start_time_entry.grid(row= 2, column = 1, sticky = W, pady = 5)
start_time_entry.get()
start_time = start_time_entry.get() 

# End Date
end_date_label = Label(root, text="End Date: ", font='Roboto 15 bold')
end_date_label.grid(row=3, column = 0, pady = 5)
end_date_label_ex =  Label(root, text = "Ex. 2021/01/21", font='Roboto 15 bold')
end_date_label_ex.grid(row= 3,column=2,sticky = W)
end_date_entry = Entry(root, bd =3,width = 40, font='Roboto 15 bold')
end_date_entry.grid(row=3, column = 1, sticky = W, pady = 5)
end_date_entry.get()
end_date = end_date_entry.get() 

# End time
end_time_label = Label(root, text="End Time: ", font='Roboto 15 bold')
end_time_label.grid(row = 4, column = 0, pady = 5)
end_time_label_ex =  Label(root, text = "Ex. 10:30:00", font='Roboto 15 bold')
end_time_label_ex.grid(row= 4,column=2,sticky = W)
end_time_entry = Entry(root, bd =3,width = 40,  font='Roboto 15 bold')
end_time_entry.grid(row=4, column = 1, sticky = W, pady = 5)
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
calculate_bttn = Button(root, text="Graph", command=myClick, width = 10, font='Roboto 15 bold' )
calculate_bttn.grid(row=5, column = 2, sticky = E, padx =3,pady = 40)


# Restart the program
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Restart Button
restart_bttn = Button(root, text = "Restart", command = restart_program, width = 10, font='Roboto 15 bold')
restart_bttn.grid(row=6,column = 2, sticky = E, padx =3,pady = 2)

# Exit button
button_exit = Button(root, text = "Exit", command = exit, width = 10, font='Roboto 15 bold')
button_exit.grid(row = 7, column = 2, sticky = E, padx =3, pady = 2)
#button_exit.pack()

root.mainloop()
exit()