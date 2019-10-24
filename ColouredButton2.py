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





root.title("Task Bar")
root.configure(bg = "#0015B3")

root.geometry("300x200+250+250")
root.mainloop()


def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")



B = tk.Button(root, text ="Hello", command = helloCallBack, foreground = "blue", relief = "groove")





B.pack()
