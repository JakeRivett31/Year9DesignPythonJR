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
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


root = Tk()

root.title("Task Bar")

root.configure(background='#243c6a')


today = date.today()

photo = PhotoImage(file="SmallUCCLogo.png")

w = Label(root, image=photo)

w.grid(row=0, column=0, padx = 20, pady = 20)

d2 = today.strftime("%B %d, %Y")


todaysdate = tk.Label(root, text = d2)
todaysdate.config(bg = "#243c6a", fg = "#6578a0", font =("Franklin Gothic", "30"))
todaysdate.grid(row=0, column=1 )


app=FullScreenApp(root)

root.mainloop()

print("End Program")