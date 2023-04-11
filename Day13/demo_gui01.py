from tkinter import *
from tkinter import messagebox as msb
###### CREATING THE WINDOW ######
my_window = Tk()                # create a new window
my_window.title('Hello TK')     # set title of the window

my_window.geometry('300x200')   # set size of the window

###### EVENT HANDLERS ######
def btn_add_click():
    msb.showinfo('Add', 'Add button clicked')

###### CREATING GUI OBJECTS ######
# create a label
lbl_message = Label(my_window, text='Hello, Label') # label parent is my_window
lbl_message.grid(row=1, column=1)                   # position (1, 1) in the grid

# create a button, and set its event handler to btn_add_click function
btn_add = Button(my_window, text='Add', command=btn_add_click) 
btn_add.grid(row=0, column=0)

####### start the main loop, waiting for events #######
my_window.mainloop()