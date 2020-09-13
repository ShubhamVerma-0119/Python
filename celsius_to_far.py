# -*- coding: utf-8 -*-
"""
celsius to farhenite converter

@author: Shubham Verma
"""


from tkinter import *

root = Tk()

root.title('Converter')

#size

root.minsize(150, 150)
root.maxsize(150, 150)

#frames

cframe = Frame(root)
cframe.pack(side= TOP)

fframe = Frame(root)
fframe.pack(side = BOTTOM)



# display screens

cdisplay = Entry(cframe)
cdisplay.grid(row= 4, columnspan =6)

fdisplay = Entry(fframe)
fdisplay.grid(row= 4, columnspan =6)

# label

clabel = Label(cframe, text="Celsius")
clabel.grid()

flabel = Label(fframe, text="farhenite")
flabel.grid()

#functions

def converter():
    celsius = cdisplay.get()
    c_num = int(celsius)
    f_num = 0
    fdisplay.delete(0, END)
    f_num = ((c_num * 9 / 5) +32)
    fdisplay.insert(0, f_num)
    
#button
    
Button(cframe, text="convert", bg="Orange", command= lambda: converter()).grid(row=5, column=4)


root.mainloop()
