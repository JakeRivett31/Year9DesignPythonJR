from tkinter import *
from PIL import Image, ImageTk
from datetime import date
import tkinter as tk



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
todaysdateLabel.grid(row=0, column=2)

canvas2 = Canvas(root, width=800, height=100)
canvas2.grid(row=1, column=1)

canvas2.create_rectangle(0, 0, 0, 0,
    outline="#6578a0", fill="#243c6a", width=0)

btnrun = tk.Button(root, text = "DELETE", highlightbackground="#8b0000", highlightthickness=10)
btnrun.config(fg="#8b0000")
btnrun.grid(row=1, column=2)

EventLabel = tk.Label(root, text="Event")
EventLabel.grid(row=1, column=1)




root.mainloop()

print("End Program")

