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


canvas = Canvas(root, bg = "#243c6a", highlightthickness=1, height=220, width=300)
canvas.grid(row=0, column=0)

photoimage = ImageTk.PhotoImage(file="SmallUCCLogo.png")
canvas.create_image(150, 150, image=photoimage)

today = date.today()

d2 = today.strftime("%B %d, %Y")


todaysdateLabel = tk.Label(root, text = d2)
todaysdateLabel.config(bg = "#243c6a", fg = "#6578a0", font =("Franklin Gothic", "30"))
todaysdateLabel.grid(row=0, column=1)


app=FullScreenApp(root)

root.mainloop()

print("End Program")

