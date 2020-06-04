from tkinter import *
import tkinter as tk

root = tk.Tk()

root.title("Sleep Calculator")

root.geometry("600x450")

root.configure(bg="#001245")


nameQuestion = tk.Label(root, text="What is your name?", font = ('Avenir',15), bg="#001245", fg="#0068f0").grid(row=0, padx=(80, 50))

e1 = Entry(root)
e1.grid(row=0, column=1)

def getName ():  
    name = e1.get()
    print(name)

button1 = tk.Button(text="Submit", command=getName)
button1.grid(row=0,column=2)
    




age = tk.Label(root, text="How old are you?", font = ('Avenir',15), bg="#001245", fg="#0068f0").grid(row=1, pady=10, padx=(80, 50))

agevariable = StringVar(root)
agevariable.set("8") # default value

ageDropdown = OptionMenu(root, agevariable, "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18")
ageDropdown.grid(row=1, column=1)


def getAge ():  
    age = agevariable.get()
    print(age)

button2 = tk.Button(text="Submit", command=getAge)
button2.grid(row=1,column=2)






root.mainloop()