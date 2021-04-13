from tkinter import *
from tkinter import filedialog
from sys import exit
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from time import sleep

# Opening file explorer
# Make sure the initial dir will be set to C: drive.

         

filename = filedialog.askopenfilename(initialdir= "C:/Users/jacob/Documents/krowpu", 
                                            title="Select a Excel File",
                                            filetypes = (("csv files","*.csv*"),))


#Creating the root root
root = Tk()
# Title
root.title('File Explorer')

label_file_explorer = Label(root, text = "Select File", height = 4,fg = "blue", font='Roboto 15 bold')
label_file_explorer.grid(row = 0, column =1, sticky = W, pady = 5)  

#view_bttn = Button(root, text="Search for file: ", command=viewFiles, width = 10, font='Roboto 15 bold' )
#view_bttn.grid(row=0, column = 1, sticky = E, padx =3,pady = 40)
label_file_explorer.configure(text = "File Opened:\n " + filename)


# Getting the file name from the directory    
filepath = filename
path = Path(filepath)
path_name = path.name

  

# Creating new dataframe 
def createDF(filename):
    df = pd.read_csv(filename,sep=r'\s*,\s*', engine='python',skiprows = 6)
    return df

# Cleaning function the data - removing NA's, creating df, dropping column
def clean_data(df):
    #Removing last column because it has NA values
    df.drop(df.columns[[-1,]], axis=1, inplace=True)
    # To Do: remove NaN's
    df.dropna(inplace=True)
    # Converting 'Date-Time' Col to a datetime object. 
    df['Date-Time'] = pd.to_datetime(df['Date-Time'], format = "%Y/%m/%d %H:%M:%S")
    # Set date-time as index - this is to make it easier to .loc or .iloc
    df = df.set_index(['Date-Time'])
    return df

# creating a df w/ chosen filename
df = createDF(path_name) 

# cleaning dataframe
clean_df = clean_data(df) 

# Graphing function
def graph_data(clean_df,start_date,start_time,end_date,end_time):
    # This is grabbing the rows from selected range of dates and time
    # Have to use sort_index() b/c if not, then it raises an error about future deprecation
    time_chosen_df = clean_df.sort_index().loc[start_date:end_date].between_time(start_time,end_time)

    # Graph attributes
    x_ticks = np.arange(0,151,20)
    plt.xticks(x_ticks)
    plt.title('Shock/Vibe Graph')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Vibrations Shock (G)')
    plt.grid(True)

    # XYVibe
    xyvibe = time_chosen_df['XYVibe'].values
    plt.plot(xyvibe,'bo--', label='XYVibe')

    # Zvib
    zvib = time_chosen_df['ZVib'].values
    plt.plot(zvib,'go--',label='Zvib')

    plt.legend()
    plt.show()


# Start Date
start_date_label = Label(root, text="Start Date: ", font='Roboto 15 bold')
start_date_label.grid(row = 1, column =0,padx = 5 )
end_date_label_ex =  Label(root, text = "Ex. 2021/01/21", font='Roboto 15 bold')
end_date_label_ex.grid(row= 1,column=2,sticky = W)
start_date_entry = Entry(root, bd =3,width = 50, font ='Roboto 15 bold' )
start_date_entry.grid(row=1, column = 1, sticky = W)
start_date_entry.get()
start_date = start_date_entry.get()

# Start Time
start_time_label = Label(root, text="Start Time: ", font='Roboto 15 bold')
start_time_label.grid(row = 2, column = 0, pady = 5)
start_time_label_ex =  Label(root, text = "Ex. 09:00:00", font='Roboto 15 bold')
start_time_label_ex.grid(row= 2,column=2,sticky = W)
start_time_entry = Entry(root, bd =3,width = 50,  font='Roboto 15 bold')
start_time_entry.grid(row= 2, column = 1, sticky = W, pady = 5)
start_time_entry.get()
start_time = start_time_entry.get() 

# End Date
end_date_label = Label(root, text="End Date: ", font='Roboto 15 bold')
end_date_label.grid(row=3, column = 0, pady = 5)
end_date_label_ex =  Label(root, text = "Ex. 2021/01/21", font='Roboto 15 bold')
end_date_label_ex.grid(row= 3,column=2,sticky = W)
end_date_entry = Entry(root, bd =3,width = 50, font='Roboto 15 bold')
end_date_entry.grid(row=3, column = 1, sticky = W, pady = 5)
end_date_entry.get()
end_date = end_date_entry.get() 

# End time
end_time_label = Label(root, text="End Time: ", font='Roboto 15 bold')
end_time_label.grid(row = 4, column = 0, pady = 5)
end_time_label_ex =  Label(root, text = "Ex. 10:30:00", font='Roboto 15 bold')
end_time_label_ex.grid(row= 4,column=2,sticky = W)
end_time_entry = Entry(root, bd =3,width = 50,  font='Roboto 15 bold')
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

root.mainloop()
exit()