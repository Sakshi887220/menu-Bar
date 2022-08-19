# importing only  those functions  
# which are needed 

from tkinter import * 
from tkinter.ttk import * 

# creating tkinter window 
root = Tk() 
root.title('Menu Demonstration') 
root.geometry("500x500")

# Creating Menubar 
 
def newfile():
    a = Label(root , text = "You clicked on new file!").pack()

  
  
# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='New File', command = newfile) 
file.add_command(label ='Open...', command = openfile) 
file.add_command(label ='Save', command = savefile) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 
  
# Adding Edit Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = cutfile) 
edit.add_command(label ='Copy', command = copyfile) 
edit.add_command(label ='Paste', command = pastefile) 
edit.add_command(label ='Select All', command = None) 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None) 
  
# Adding Help Menu 

  
# display Menu 

mainloop() 
