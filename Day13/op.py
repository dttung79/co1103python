from tkinter import *
from tkinter import messagebox as msb

###### CREATING THE WINDOW ######
my_window = Tk()                # create a new window
my_window.title('Arithmetic operators')     # set title of the window

my_window.geometry('300x300')   # set size of the window

###### EVENT HANDLERS ######
def calculate(op='+'):
    try:
        a = int(txt_a.get())
        b = int(txt_b.get())
        if   op == '+': c = a + b
        elif op == '-': c = a - b
        elif op == '*': c = a * b
        elif op == '/': c = a / b
        else:           c = 0
        txt_c.delete(0, END) # erase the old content
        txt_c.insert(0, str(c))
    except ZeroDivisionError:
        msb.showerror('Error', 'Cannot divide by zero')
    except ValueError:
        msb.showerror('Error', 'Invalid input, must be integers')
def btn_add_click():
    calculate('+')

def btn_sub_click():
    calculate('-')

def btn_mult_click():
    calculate('*')

def btn_div_click():
    calculate('/')

###### CREATING GUI OBJECTS ######
lbl_a = Label(my_window, text='a = ')
lbl_a.grid(row=0, column=0)

txt_a = Entry(my_window)
txt_a.grid(row=0, column=1, columnspan=4)

lbl_b = Label(my_window, text='b = ')
lbl_b.grid(row=1, column=0)

txt_b = Entry(my_window)
txt_b.grid(row=1, column=1, columnspan=4)

lbl_c = Label(my_window, text='c = ...')
lbl_c.grid(row=2, column=0)

txt_c = Entry(my_window)
txt_c.grid(row=2, column=1, columnspan=4)

btn_add = Button(my_window, text='Add', command=btn_add_click)
btn_add.grid(row=3, column=1)

btn_sub = Button(my_window, text='Sub', command=btn_sub_click)
btn_sub.grid(row=3, column=2)

btn_mult = Button(my_window, text='Mult', command=btn_mult_click)
btn_mult.grid(row=3, column=3)

btn_div = Button(my_window, text='Div', command=btn_div_click)
btn_div.grid(row=3, column=4)
###### start the main loop, waiting for events #######
my_window.mainloop()