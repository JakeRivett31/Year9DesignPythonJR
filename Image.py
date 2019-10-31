import tkinter as tk
from PIL import ImageTk, Image
import os

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open("SmallCarey.jpg"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "no")
root.geometry("120x100+30+30")
root.mainloop()

