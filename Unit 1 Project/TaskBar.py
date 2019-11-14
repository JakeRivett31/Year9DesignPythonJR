from tkinter import *
from PIL import Image, ImageTk
from datetime import date
import tkinter as tk
from tkinter import messagebox as tkMessageBox
import sys
from tkinter import simpledialog



print("Start Program")






root = tk.Tk()

root.title("Task Bar")

root.configure(background='#243c6a')


canvas = Canvas(root, bg = "#243c6a", highlightthickness=0, height=100, width=300)
canvas.grid(row=0, column=0)

photoimage = ImageTk.PhotoImage(file="SmallUCCLogo.png")
canvas.create_image(150, 50, image=photoimage)



today = date.today()

d2 = today.strftime("%B %d, %Y")


todaysdateLabel = tk.Label(root, text = d2)
todaysdateLabel.config(bg = "#243c6a", fg = "#6578a0", font =("Franklin Gothic", "30"))
todaysdateLabel.grid(row=0, column=4)



today = date.today()

d2 = today.strftime("%B %d, %Y")


todaysdateLabel = tk.Label(root, text = d2)
todaysdateLabel.config(bg = "#243c6a", fg = "#6578a0", font =("Franklin Gothic", "30"))
todaysdateLabel.grid(row=0, column=4)

TaskBarLabel = tk.Label(root, text="Task Bar")
TaskBarLabel.config(bg = "#243c6a", fg = "#6578a0", font =("Franklin Gothic", "45"))
TaskBarLabel.grid(row=0, column=2)



variable = IntVar(root)
variable.set("30") # default value

FontListBox = OptionMenu(root, variable, "Font Sizes", "11", "12", "etc")
FontListBox.config(fg="#243c6a", width=5, font =("Franklin Gothic", "15"))
FontListBox.grid(row=1, column=0)


EventCanvas1 = Canvas(root, width=800, height=100)
EventCanvas1.config(bd=3, relief="ridge", highlightbackground="#6578a0")
EventCanvas1.grid(row=1, column=1, columnspan=3, pady=10)

DeleteButton1 = tk.Button(root, text = "DELETE", highlightbackground="#8b0000", highlightthickness=20)
DeleteButton1.config(fg="#8b0000")
DeleteButton1.grid(row=1, column=4)

EventLabel = tk.Label(root, text="Event")
EventLabel.config(font =("Franklin Gothic", "30"), fg="#243c6a")
EventLabel.grid(row=1, column=1)

TimeAndDateLabel = tk.Label(root, text="Time and Date")
TimeAndDateLabel.config(font =("Franklin Gothic", "30"), fg="#243c6a")
TimeAndDateLabel.grid(row=1, column=2)

TimeNeededLabel = tk.Label(root, text="Time Needed")
TimeNeededLabel.config(font =("Franklin Gothic", "30"), fg="#243c6a")
TimeNeededLabel.grid(row=1, column=3)

EventCanvas2 = Canvas(root, width=800, height=100)
EventCanvas2.config(bd=3, relief="ridge", highlightbackground="#6578a0")
EventCanvas2.grid(row=2, column=1, columnspan=3, pady=10)

DeleteButton2 = tk.Button(root, text = "DELETE", highlightbackground="#8b0000", highlightthickness=20)
DeleteButton2.config(fg="#8b0000")
DeleteButton2.grid(row=2, column=4)



def PopUpWindow():
   EventNameInput = simpledialog.askstring("Add New Event", "Event Name:")
   DateInput = simpledialog.askstring("Add New Event", "Date (Month, Day, Year):")
   TimeInput = simpledialog.askstring("Add New Event", "Time (Include am or pm):")
   TimeNeededInput = simpledialog.askstring("Add New Event", "Time Needed (In Minutes):", parent = root)

def write_File (text_File):
    file = open("users.txt", "a")



AddNewEventButton = tk.Button(root, text ="Add New Event", command = PopUpWindow, fg = "#243c6a", relief = "groove")
AddNewEventButton.config(width=45, height=2, bd=3, relief="ridge", highlightbackground="#6578a0", font =("Franklin Gothic", "30"))
AddNewEventButton.grid(row=3, column=1, columnspan=3, sticky=W)


root.mainloop()

print("End Program")

