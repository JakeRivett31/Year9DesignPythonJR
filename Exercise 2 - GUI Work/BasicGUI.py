import tkinter as tk
from PIL import Image, ImageTk


print("Start Program")
root = tk.Tk()

title = tk.Label(root, text = "Carey Price!")
title.config(fg = "red", bg = "blue")
title.pack(fill = tk.BOTH)

path = "https://www.ctvnews.ca/polopoly_fs/1.4184337.1542715604!/httpImage/image.jpg_gen/derivatives/landscape_620/image.jpg"

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")







root = tk.mainloop()

print("End Program")