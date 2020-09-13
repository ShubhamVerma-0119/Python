"""
Created on Sun Sep 13 17:47:02 2020

@author: Shubham Verma
"""




# importing libraries : tkinter and parser

from tkinter import *
import parser




root = Tk()


# Title
root.title('Calculator')


root.maxsize(300,200)

#get user-input in the text Field
i=0                                            
def get_variable(num):
    global i
    display.insert(i,num)                       
    i+=1
    
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        
def factorial():
    x = display.get()
    y = int(x)
    z = 1
    try:    
        while (y > 1):
            z = z * y
            y-=1
        clear_all()
        display.insert(0, z)
    
    except Exception:
        clear_all()
        display.insert(0,"Error")

        
    
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length

def clear_all():
    display.delete(0,  END)

def undo():
    entire_string = display.get()
    new_string = entire_string[:-1]
    display.delete(0, END)
    display.insert(0, new_string)
    

    


# display screen
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)





# Add Buttons (0 to 9)
Button(root, text=1, width=6, command= lambda : get_variable(1)).grid(row=2, column=0)
Button(root, text=2, width=6, command= lambda : get_variable(2)).grid(row=2, column=1)
Button(root, text=3, width=6, command= lambda : get_variable(3)).grid(row=2, column=2)


Button(root, text=4, width=6, command= lambda : get_variable(4)).grid(row=3, column=0)
Button(root, text=5, width=6, command= lambda : get_variable(5)).grid(row=3, column=1)
Button(root, text=6, width=6, command= lambda : get_variable(6)).grid(row=3, column=2)

Button(root, text=7, width=6, command= lambda : get_variable(7)).grid(row=4, column=0)
Button(root, text=8, width=6, command= lambda : get_variable(8)).grid(row=4, column=1)
Button(root, text=9, width=6, command= lambda : get_variable(9)).grid(row=4, column=2)

Button(root, text=0, width=6, command= lambda : get_variable(0)).grid(row=5, column=1)


# Add Other Buttons

Button(root, text="AC", width=6, bg="red", command= lambda: clear_all()).grid(row=5, column=0)
Button(root, text="=", width=6, bg="Green", command= lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", width=6, command= lambda : get_operation("+")).grid(row=2, column=3)
Button(root, text="-", width=6, command= lambda : get_operation("-")).grid(row=3, column=3)
Button(root, text="*", width=6, command= lambda : get_operation("*")).grid(row=4, column=3)
Button(root, text="/", width=6, command= lambda : get_operation("/")).grid(row=5, column=3)

Button(root, text="PI",width=6, bg="Orange", command= lambda : get_operation("3.14")).grid(row=2, column=4)
Button(root, text="%", width=6, bg="Orange", command= lambda : get_operation("%")).grid(row=3, column=4)
Button(root, text="(", width=6, bg="Orange", command= lambda : get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", width=6, bg="Orange", command= lambda : get_operation("**")).grid(row=5, column=4)

Button(root, text="<-",width=6, bg="Orange", command= lambda: undo()).grid(row=2, column=5)
Button(root, text="x!", width=6, bg="Orange", command= lambda: factorial()).grid(row=3, column=5)
Button(root, text=")", width=6, bg="Orange", command= lambda : get_operation(")")).grid(row=4, column=5)
Button(root, text="^2", width=6, bg="Orange", command= lambda : get_operation("**2")).grid(row=5, column=5)

label = Label(text="created by Shubham Verma", bg="Orange")
label.grid(row=6, columnspan=6)

root.mainloop()