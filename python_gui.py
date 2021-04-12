from tkinter import *
from tkinter import filedialog
from sys import exit
from cleaning_data import clean_data, graph_data


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
    label_file_explorer.configure(text = "File Opened:\n " + filename)


root.geometry("500x500")
# Set root title
root.title('File Explorer')

# Set root background color
#root.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(root, text = "Select File",width = 70, height = 4,fg = "Red")
label_file_explorer.pack()

# Browse files button
button_explore = Button(root,text = "Browse Files",command = viewFiles)
button_explore.pack()


# Input Box - Examples
#e = Entry(root, width = 50)
#e.pack()
#e.insert(0, "Enter your start date: ")
#e.get() # Gets the value of the written thing

# Start Date
start_date_label = Label(root, text="Start Date: ")
start_date_label.pack()
start_date_entry = Entry(root, bd =5)
start_date_entry.pack()
start_date_entry.get()

# Start Time
start_time_label = Label(root, text="Start time: ")
start_time_label.pack()
start_time_entry = Entry(root, bd =5)
start_time_entry.pack()
start_time_entry.get()

# End Date
end_date_label = Label(root, text="End Date: ")
end_date_label.pack()
end_date_entry = Entry(root, bd =5)
end_date_entry.pack()
end_date_entry.get()

# End time
end_time_label = Label(root, text="End time: ")
end_time_label.pack()
end_time_entry = Entry(root, bd =5)
end_time_entry.pack()
end_time_entry.get()

def input():
    start_date = start_date_entry.get()
    start_time = start_time_entry.get() 
    end_date = end_date_entry.get() 
    end_time = end_time_entry.get()
    print(start_date, start_time, end_date,end_time)
# Calculate Button
calculate_bttn = Button(root, text="Calculate", command=input)
calculate_bttn.pack()
# Exit button
#button_exit = Button(root, text = "Exit", command = exit)
#button_exit.pack()

root.mainloop()
exit()