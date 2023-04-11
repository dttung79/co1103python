from tkinter import *
from tkinter import messagebox as msb
###### CREATING THE WINDOW ######
my_window = Tk()                # create a new window
my_window.title('Demo Text fields')     # set title of the window

my_window.geometry('300x200')   # set size of the window


####### EVENT HANDLERS ######
def btn_hello_click():
    msg = 'Hello ' + txt_name.get()
    msb.showinfo('Hello', msg)

####### CREATING GUI OBJECTS ######
# create text field
txt_name = Entry(my_window)
txt_name.grid(row=0, column=0)

# create a button
btn_hello = Button(my_window, text='Say hi', command=btn_hello_click)
btn_hello.grid(row=0, column=1)


####### start the main loop, waiting for events #######
my_window.mainloop()