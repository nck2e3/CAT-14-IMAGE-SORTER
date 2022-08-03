import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL.ExifTags import TAGS
import tkinter as tk
from tkinter import ttk
import sv_ttk

def error():
    messagebox.showerror('Error', 'Error: No folder is selected!')

def getPath():
    global path
    path = filedialog.askdirectory()
    browse_button.config(text=path)
    if(path == ""):
        browse_button.config(text="BROWSE")
        error()
        
def rename():
    author = author_entry.get()
    location = dropTwo.get()
    state = dropOne.get()
    files = os.listdir(path)

    if path == "":
        error()
        return None

    i=1
    for file in files:
        if(file == "Thumbs.db"):
            continue
        if(file.lower().endswith(".jpg")):
            date_taken = Image.open(f'{path}//{file}')._getexif()[36867]
            date_taken_string = date_taken.replace(":", "-")
            file_name = date_taken_string
            os.rename(os.path.join(path,file), os.path.join(path, file_name + str(i).zfill(4) + '.jpg'))
            i+=1

    files = os.listdir(path)
    
    i = 1;
    prev_taken = ""
    for file in files:
        if(file == "Thumbs.db"):
            continue
        if(file.lower().endswith(".jpg") or file.lower().endswith(".jpeg") ):
            #Scrape EXIF tag 36867 to find the date the photo was taken
            date_taken = Image.open(f'{path}//{file}')._getexif()[36867]
            #Format string to the desired date format
            date_taken_string = date_taken[:len(date_taken) - 9].replace(":", "-")

            #If previous date is different from current date, reset the count        
            if(date_taken_string != prev_taken):
                i = 1
            else:
                i += 1

            #Reformat photo enumerator to a consistent easily sortable format
            iterator = str(i).zfill(4)

            #Constructing final file name
            #file_name = date_taken_string + " - " + state.lower() + " - " + "loc " + location + " - " +  author + " - " + iterator
            file_name = date_taken_string + " - " + state.lower() + " - " + "ROUTE 24, R5.97, R6.26 AND R6.51" + " - " +  author + " - " + iterator

            #Renaming folder
            os.rename(os.path.join(path,file), os.path.join(path, file_name + '.jpg'))
            
            #Printing modifications to console.
            print(f'\'{file}\' is renamed to \'{file_name}\'')

            prev_taken = date_taken_string

# root window
root = tk.Tk()
sv_ttk.set_theme("light")  # Set light theme
root.geometry("500x215")
root.title('CAT 14 - IMAGE BULK RENAME UTILITY - http://noahking.xyz')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# photo author
author_label = ttk.Label(root, text="IMAGE AUTHOR")
author_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

author_entry = ttk.Entry(root)
author_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

# directory 
directory_label = ttk.Label(root, text="TARGET DIRECTORY")
directory_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

# rename button
browse_button = ttk.Button(root, text= "BROWSE FILES", command= lambda:getPath())
browse_button.config(width=5)
browse_button.grid(column=1, row=1, columnspan=3, sticky=tk.EW, padx=5, pady=5)

# project state
state_label = ttk.Label(root, text="PROJECT STATE")
state_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

dropOne = tk.StringVar(root)
dropOne_entry = ttk.OptionMenu(root, dropOne, "select", "pre-con", "mid-con", "post-con")
dropOne_entry.config(width=40)
dropOne_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

# project format
format_label = ttk.Label(root, text="PROJECT LOCATION")
format_label.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)

dropTwo = tk.StringVar(root)
format_entry = ttk.OptionMenu(root, dropTwo, "select", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
format_entry.config(width=40)
format_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

# rename button
rename_button = ttk.Button(root, text= "RENAME ALL FILES IN DIRECTORY", command= lambda:rename())
rename_button.config(width=40)
rename_button.grid(row=4, columnspan=2, sticky=tk.EW, padx=5, pady=5)

root.mainloop()