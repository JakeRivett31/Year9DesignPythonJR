from tkinter import *
from PIL import Image, ImageTk
from datetime import date
import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import simpledialog, filedialog

'''
Mr. Miskew is cheating a bit. Really the better way to do
this is to use Object Oriented Design.  

The effect is that you need to store all variables as lists
'''

#VaRIaBLES
root = tk.Tk()

data = ["","","",""] #Creates an empty list

photocanvas = Canvas(root, bg = "#243c6a", highlightthickness=0, height=100, width=300)

photoimage = ImageTk.PhotoImage(file="SmallUCCLogo.png")

today = date.today()

d2 = today.strftime("%B %d, %Y")

todaysdatelabel = tk.Label(root, text = d2)

taskbarlabel = tk.Label(root, text="Task Bar")

eventcanvas1 = Canvas(root, width=800, height=100)

deletebutton1 = tk.Button(root, text = "DELETE", highlightbackground="#8b0000", highlightthickness=20)

eventlabel1 = tk.Label(root, text="Event")

timeanddatelabel1 = tk.Label(root, text="Time and Date")

timeneededlabel1 = tk.Label(root, text="Time Needed")

addneweventbutton = tk.Button(root, text ="Add New Event", fg = "#243c6a", relief = "groove")

file = open("EventDetails.txt","a")


#FUNCTIONS
#creates 4 separate 
def popupwindow():
  #There is a nice opportunity for some while loops to error check
  #You can check the type of a variable using the type command
  data[0] = simpledialog.askstring("Add New Event", "Event Name:")    
  data[1] = simpledialog.askstring("Add New Event", "Date (Month, Day, Year):")
  data[2] = simpledialog.askstring("Add New Event", "Time (Include am or pm):")
  data[3] = simpledialog.askstring("Add New Event", "Time Needed (In Minutes):")
  
  file.write(str(data))

  eventcanvas = Canvas(root, width=800, height=100)
  eventcanvas.config(bd=3, relief="ridge", highlightbackground="#6578a0")
  eventcanvas.grid(row=2, column=1, columnspan=3, pady=10)

  deletebutton = tk.Button(root, text = "DELETE", highlightbackground="#8b0000", highlightthickness=20)
  deletebutton.config(fg="#8b0000", command = deletetext)
  deletebutton.grid(row=2, column=4)

  eventlabel = tk.Label(root, text=data[0])
  eventlabel.config(font =("Franklin Gothic", "30"), fg="#243c6a")
  eventlabel.grid(row=2, column=1)

  timeanddatelabel = tk.Label(root, text=data[1]+"     "+data[2])
  timeanddatelabel.config(font =("Franklin Gothic", "26"), fg="#243c6a")
  timeanddatelabel.grid(row=2, column=2)
  
  timeneededlabel = tk.Label(root, text=data[3])
  timeneededlabel.config(font =("Franklin Gothic", "30"), fg="#243c6a")
  timeneededlabel.grid(row=2, column=3)


def deletetext():
  eventlabel.destroy()
  timeanddatelabel.destroy()
  timeneededlabel.destroy()
  eventcanvas.destroy()
  deletebutton.destroy()

#deletes whole event bar
def deletetext1():
    eventlabel1.destroy()
    timeanddatelabel1.destroy()
    timeneededlabel1.destroy()
    eventcanvas1.destroy()
    deletebutton1.destroy()



#WINDOW CONSTRUCTION
print("Start Program")



root.title("Task Bar")

root.configure(background='#243c6a')

photocanvas.grid(row=0, column=0)

photocanvas.create_image(150, 50, image=photoimage)



todaysdatelabel.config(bg = "#243c6a", fg = "#6578a0", font =("Franklin Gothic", "30"))
todaysdatelabel.grid(row=0, column=4)



taskbarlabel.config(bg = "#243c6a", fg = "#6578a0", font =("Franklin Gothic", "45"))
taskbarlabel.grid(row=0, column=2)



eventcanvas1.config(bd=3, relief="ridge", highlightbackground="#6578a0")
eventcanvas1.grid(row=1, column=1, columnspan=3, pady=10)


deletebutton1.config(fg="#8b0000", command = deletetext1)
deletebutton1.grid(row=1, column=4)


eventlabel1.config(font =("Franklin Gothic", "30"), fg="#243c6a")
eventlabel1.grid(row=1, column=1)


timeanddatelabel1.config(font =("Franklin Gothic", "30"), fg="#243c6a")
timeanddatelabel1.grid(row=1, column=2)


timeneededlabel1.config(font =("Franklin Gothic", "30"), fg="#243c6a")
timeneededlabel1.grid(row=1, column=3)


addneweventbutton.config(width=45, height=2, bd=3, relief="ridge", highlightbackground="#6578a0", font =("Franklin Gothic", "30"), command = popupwindow)
addneweventbutton.grid(row=10, column=1, columnspan=3, sticky=W)


root.mainloop()

print("End Program")

