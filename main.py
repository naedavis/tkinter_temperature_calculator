#Exercise 2
#Temperature Converter
#Fahrenheit to Celsius and Celsius to Fahrenheit

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("600x400") #window size
window.title("Temperature Converter F to C / C to F")
lblfc_to_f = tk.LabelFrame(window, text = "Celsius to Fahrenheit")
lblfc_to_f.place(x=50, y=60, height=100, width=180)
lblff_to_c = tk.LabelFrame(window, text = "Fahrenheit to Celsius")
lblff_to_c.place(x=300, y=60, height=100, width=180)
e_celsius = tk.Entry(lblfc_to_f, state= "readonly") # saying that on execution of this program the entry is readonly
e_celsius.place(x=40, y=20, width=100)
e_fahrenheit =tk.Entry(lblff_to_c, state= "readonly") # saying that on execution of this program the entry is readonly
e_fahrenheit.place(x=40, y=20, width=100)
conversion = tk.Entry(window, state="readonly")  # saying that on execution of this program the entry is readonly
conversion.place(x=170, y=300, height= 50, width=200)

def convert(): #function defined to be called when convert button is pushed
   if e_celsius['state'] == "normal" : # if state of entry changes to normal then activate the following
       convert1 = int(e_celsius.get())*1.8 + 32 #conversion from celsius to fahrenheit
       conversion.config(state = "normal")# changing conversion entry where output will be displayed into normal state and not readonly
       conversion.insert(INSERT, str(convert1)) # inserting converted value into the output entry
   elif e_fahrenheit['state'] == "normal":
       convert2 = (int(e_fahrenheit.get())- 32) * (5/9)
       conversion.config(state="normal")
       conversion.insert(INSERT, str(convert2))


def activate1(): # function defined to change states of entries when buttons are pushed
    e_celsius.config(state = "normal")
    e_fahrenheit.config(state = "readonly")

btnactivate = tk.Button(window, text="Activate- C to F", command = activate1) # calls function that activates celcius entry
btnactivate.place(x=70, y=180)

def activate2():# function defined to change states of entries when buttons are pushed
    e_fahrenheit.config(state = "normal")
    e_celsius.config(state = "readonly")


btnactivate2 = tk.Button(window, text= "Activate- F to C", command = activate2) # calls function that activates fahrenheit entry
btnactivate2.place(x=320, y=180)



btnConv = tk.Button(window, text = "Calculate Conversion", command = convert)# calls function that converts entries
btnConv.place(x=190, y=250)

def clear(): # defining function for the clear button
    e_fahrenheit.delete(0,tk.END)
    e_celsius.delete(0, tk.END)
    conversion.delete(0,tk.END)

btnclear = tk.Button(window, text= "Clear", command = clear) #clear function being called
btnclear.place(x=470, y=300)
btnexit = tk.Button(window, text= "Exit Program", command= exit)
btnexit.place(x=450, y=350)


window.mainloop()
