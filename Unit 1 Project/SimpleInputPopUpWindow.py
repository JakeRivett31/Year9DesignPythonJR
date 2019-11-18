from tkinter import *
from PIL import Image, ImageTk
from datetime import date
import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import simpledialog

root = tk.Tk()

button = tk.Button(root, text= "ye", command = body)
button.pack()

class MyDialog():

    def body(self, master):

        Label(master, text="First:").grid(row=0)
        Label(master, text="Second:").grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = int(self.e1.get())
        second = int(self.e2.get())
        print ("first", "second") # or something

root.mainloop()

