# -*- coding: utf-8 -*-
"""
GUI Employee SQL entry with Python

@author: Shubham Verma
"""
# import libraries

from tkinter import *
import tkinter as tk
import psycopg2



# Start tkinter

root = Tk()

# Title of UI app
root.title("employee")


# canvas
canvas = Canvas(root, height=480, width=900)
canvas.pack()

#Frame
frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

frame2 = Frame()
frame2.pack(side=BOTTOM)




#Labels
label = Label(frame, text="Add data")
label.grid(row=0, column=2)


id_label = Label(frame, text="emp ID: ")
id_label.grid(row=1, column=0)

name_label = Label(frame, text="Name: ")
name_label.grid(row=2, column=0)

emailid_label = Label(frame, text="Email ID: ")
emailid_label.grid(row=3, column=0)

age_label = Label(frame, text="Age: ")
age_label.grid(row=4, column=0)

gender_label = Label(frame, text="Gender: ")
gender_label.grid(row=5, column=0)

dept_label = Label(frame, text= "Department: ")
dept_label.grid(row=6, column=0)

desig_label = Label(frame, text= "Designation: ")
desig_label.grid(row=7, column=0)

address_label = Label(frame, text= "Address: ")
address_label.grid(row=1, column=3)

pcode_label = Label(frame, text= "Pin code: ")
pcode_label.grid(row=2, column=3)

city_label = Label(frame, text= "city: ")
city_label.grid(row=3, column=3)

state_label = Label(frame, text= "state: ")
state_label.grid(row=4, column=3)

country_label = Label(frame, text= "country: ")
country_label.grid(row=5, column=3)





#Entry values
entry_id= Entry(frame)
entry_id.grid(row=1, column=1)

entry_name= Entry(frame)
entry_name.grid(row=2, column=1)

entry_email= Entry(frame)
entry_email.grid(row=3, column=1)

entry_age= Entry(frame)
entry_age.grid(row=4, column=1)

entry_gender= Entry(frame)
entry_gender.grid(row=5, column=1)

entry_dept= Entry(frame)
entry_dept.grid(row=6, column=1)

entry_desig= Entry(frame)
entry_desig.grid(row=7, column=1)

entry_address= Entry(frame)
entry_address.grid(row=1, column=4)

entry_pcode= Entry(frame)
entry_pcode.grid(row=2, column=4)

entry_city= Entry(frame)
entry_city.grid(row=3, column=4)

entry_state= Entry(frame)
entry_state.grid(row=4, column=4)

entry_country= Entry(frame)
entry_country.grid(row=5, column=4)


#clear_all()

def clear_all():
    entry_id.delete(0, END)
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    entry_age.delete(0, END)
    entry_gender.delete(0, END)
    entry_desig.delete(0, END)
    entry_dept.delete(0, END)
    entry_address.delete(0, END)
    entry_pcode.delete(0, END)
    entry_city.delete(0, END)
    entry_state.delete(0, END)
    entry_country.delete(0, END)


#get_data()

def get_data():

        conn = psycopg2.connect(dbname="postgres", user="postgres", 
                                password="********", host="localhost", 
                                port="5432")
        cur = conn.cursor()
        id = entry_id.get()
        name = entry_name.get()
        email = entry_email.get()
        age = entry_age.get()
        gender = entry_gender.get()
        desig = entry_desig.get()
        dept = entry_dept.get()
        address = entry_address.get()
        pcode = entry_pcode.get()
        city = entry_city.get()
        state = entry_state.get()
        country = entry_country.get()

        
        query ='''insert into employee (emp_id, name, email_id, age, gender, department, designation, address, pincode, city, State, country) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s );'''
        
        cur.execute(query, (id, name, email, age, gender, dept, desig, address, pcode, city, state, country))
        
        
        conn.commit()
        
        conn.close()
        clear_all()
        messagebox.showinfo("Data saved","Congratulations! Student's Data Saved")  


# show all values
def all_values():
        conn = psycopg2.connect(dbname="postgres", user="postgres", 
                                password="********", host="localhost", 
                                port="5432")
        cur = conn.cursor()
        query = '''select * from employee; '''
        cur.execute(query)
        row=cur.fetchall()
        
        listbox = Listbox(frame2, width=120, height=5)
        listbox.grid(row=9, column=1)
        for x in row:
            listbox.insert(END,x)
        conn.commit()
        
        conn.close()
 


#Buttons
Button(frame, text="Save",width=6, command= lambda : get_data()).grid(row=8, column=1)
Button(frame, text="Clear All",width=6, command= lambda : clear_all()).grid(row=8, column=2)
Button(frame, text="View all",width=6, command= lambda : all_values()).grid(row=8, column=3)






    
root.mainloop()

