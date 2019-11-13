from tkinter import *
from PIL import Image, ImageTk
from datetime import date
import tkinter as tk



print("Start Program")

class FullScreenApp(object):

    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{0}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom




root = tk.Tk()

root.title("Task Bar")

root.configure(background='#243c6a')


canvas = Canvas(root, bg = "#243c6a", highlightthickness=0, height=100, width=300)
canvas.grid(row=0, column=0)

photoimage = ImageTk.PhotoImage(file="SmallUCCLogo.png")
canvas.create_image(150, 50, image=photoimage)

variable = IntVar(root)
variable.set("30") # default value

FontListBox = OptionMenu(root, variable, "Font Sizes", "11", "12", "etc")
FontListBox.config(fg="#243c6a", width=5, font =("Franklin Gothic", "15"))
FontListBox.grid(row=1, column=0)


today = date.today()

d2 = today.strftime("%B %d, %Y")


todaysdateLabel = tk.Label(root, text = d2)
todaysdateLabel.config(bg = "#243c6a", fg = "#6578a0", font =("Franklin Gothic", "30"))
todaysdateLabel.grid(row=0, column=4)

EventCanvas = Canvas(root, width=800, height=100)
EventCanvas.grid(row=1, column=1, columnspan=3)

btnrun = tk.Button(root, text = "DELETE", highlightbackground="#8b0000", highlightthickness=20)
btnrun.config(fg="#8b0000")
btnrun.grid(row=1, column=4)

EventLabel = tk.Label(root, text="Event")
EventLabel.config(font =("Franklin Gothic", "30"), fg="#243c6a")
EventLabel.grid(row=1, column=1)

TimeAndDateLabel = tk.Label(root, text="Time and Date")
TimeAndDateLabel.config(font =("Franklin Gothic", "30"), fg="#243c6a")
TimeAndDateLabel.grid(row=1, column=2)

TimeNeededLabel = tk.Label(root, text="Time Needed")
TimeNeededLabel.config(font =("Franklin Gothic", "30"), fg="#243c6a")
TimeNeededLabel.grid(row=1, column=3)


app = FullScreenApp(root)

root.mainloop()

print("End Program")

