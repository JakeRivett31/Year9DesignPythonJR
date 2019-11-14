import tkinter as tk
from tkinter import *
import sys

root = Tk()

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Add New Event")
        self.l.grid()
        self.e=Entry(top)
        self.e.grid()
        self.b=Button(top,text='Add',command=lambda: sys.stdout.write(self.cleanup()+'\n'))
        self.b.grid()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
        return self.value

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=Button(master,text="click me!",command=self.popup)
        self.b.grid()
        

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"


        

if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)

root.mainloop()
