import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import *


root = tk.Tk()


listbox = Listbox(root)
listbox.pack()

listbox.insert(END, "A list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)



lb = Listbox(root)

b = Button(root, text="Delete",
           command=lambda lb=lb: lb.delete(ANCHOR))











root.geometry("300x200+250+250")
root.mainloop()