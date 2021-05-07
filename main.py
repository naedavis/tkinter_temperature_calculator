#Exercise 2
#Temperature Converter
#Fahrenheit to Celsius and Celsius to Fahrenheit
import tkinter as tk
from tkinter import messagebox, INSERT

window = tk.Tk()
window.geometry("580x400") #window size
window.title("Temperature Converter") #window title
window.resizable(width=False, height=False)# user is unable to resize the window
window.config(bg = "white")#background color of the window
lblfc_to_f = tk.LabelFrame(window, text = "Celsius to Fahrenheit") #created a window frame to display the entry in which the user will input a temperature
lblfc_to_f.place(x=50, y=60, height=100, width=180)#size and position of entry
lblff_to_c = tk.LabelFrame(window, text = "Fahrenheit to Celsius")
lblff_to_c.place(x=300, y=60, height=100, width=180)
lblname = tk.Label(window, text="naedavis")# coded inside the program so no one steals my code
lblname.place(x=400, y=400, height=10, width=50)
e_celsius = tk.Entry(lblfc_to_f,bg = "red", fg="white",state= "readonly") # saying that on execution of this program the entry cannot be edited
e_celsius.place(x=40, y=20, width=100)
e_fahrenheit =tk.Entry(lblff_to_c,bg="blue", fg= "white",state= "readonly") # saying that on execution of this program the entry cannot be edited
e_fahrenheit.place(x=40, y=20, width=100)
conversion = tk.Entry(window,state="readonly")  # saying that on execution of this program the entry cannot be edited
conversion.place(x=170, y=300, height= 50, width=200)

#function declared to exit application
def ExitApplication():
    # message box will appear and ask if user is sure about them exiting the application as well as giving the user an option to stay in the program instead
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    #if user clicks on yes then exit the program as requested
    if MsgBox == 'yes':
       window.destroy()
    else:
        #message will pop up telling the user they chose to remain in the application instead of exiting
        tk.messagebox.showinfo('Return','You will now return to the application screen')

#function defined to be called when convert button is pushed
def convert():
   # if state of entry changes to normal then activate the following
   if e_celsius['state'] == "normal" :
      #try except method used to prevent user from inputing an invalid value
      try:
          #clears all other entries
          e_fahrenheit.delete(0,tk.END)
          conversion.delete(0,tk.END)
          #creating a variable that performs conversion from Celsius to Fahrenheit
          convert1 = float(e_celsius.get())*1.8 + 32
          # changing conversion entry where output will be displayed into normal state and not readonly
          conversion.config(state = "normal")
          # inserting converted value into the output entry
          conversion.insert(INSERT, str(round(convert1,1)))
      except ValueError:
          #error message will pop up if values entered is not of float type
          messagebox.showinfo("Error", "Incorrect value entered, Please enter valid input")
          e_celsius.delete(0, tk.END)
   elif e_fahrenheit['state'] == "normal":
       try:
           # clears all other entries
           e_celsius.delete(0, tk.END)
           conversion.delete(0, tk.END)
           # creating a variable that performs conversion from Fahrenheit to Celsius
           convert2 = ((float(e_fahrenheit.get())) - 32) * (5 / 9)
           # changing conversion entry where output will be displayed into normal state and not readonly
           conversion.config(state="normal")
           # inserting converted value into the output entry
           conversion.insert(INSERT, str(round(convert2,1)))
       except ValueError:
           # error message will pop up if values entered is not of float type
          messagebox.showinfo("Error", "Incorrect value entered, Please enter valid input")
          e_fahrenheit.delete(0, tk.END)

# function defined to change states of entries to normal and can now be edited
def activate1():
    e_celsius.config(state = "normal")
    e_fahrenheit.config(state = "readonly")

#button that is clicked that calls activate1 function that allows user to input values
btnactivate = tk.Button(window, text="Activate", font= "Calibri 15",fg = "red", command = activate1)
btnactivate.place(x=70, y=180)

# function defined to change states of entries to normal and can now be edited
def activate2():
    e_fahrenheit.config(state = "normal")
    e_celsius.config(state = "readonly")

#button that is clicked that calls activate1 function that allows user to input values
btnactivate2 = tk.Button(window, text= "Activate", font= "Calibri 15",fg= "blue", command = activate2)
btnactivate2.place(x=320, y=180)

#calls function to allow that converts values inputed by user
btnConv = tk.Button(window, text = "Calculate Conversion", font= "Calibri 15", command = convert)
btnConv.place(x=150, y=250)

#defining a function that will clear whichever entries are in a state of normal
def clear():
    e_fahrenheit.delete(0,tk.END)
    e_celsius.delete(0, tk.END)
    conversion.delete(0,tk.END)

#clear button being called
btnclear = tk.Button(window, text= "Clear",font= "Calibri 15", command = clear)
btnclear.place(x=450, y=300)

#exit application function being called
btnexit = tk.Button(window, text= "Exit Program",font="Calibri 15", bg= "red",command= ExitApplication)
btnexit.place(x=410, y=350)

#running the mainloop
window.mainloop()
