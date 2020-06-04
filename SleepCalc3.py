from tkinter import *
import tkinter as tk

root = tk.Tk()

root.title("Sleep Calculator")

frame1 = tk.Frame(root, bg="#001245")



frame2 = tk.Frame(root, bg="#001245")

sleepCalcTitle = tk.Label(frame1, text="Sleep Calculator", font = ('Avenir',35), bg="#001245", fg="#0068f0")

sleepCalcTitle.grid(row=0, columnspan=2, padx=(75,0))

nameQuestion = tk.Label(frame1, text="What is your name?", font = ('Avenir',15), bg="#001245", fg="#0068f0").grid(row=1, padx=(80, 50))

e1 = Entry(frame1)
e1.grid(row=1, column=1)

def getName ():  
    name = e1.get()
    print(name)

nameSubmit = tk.Button(frame1, text="Submit", highlightbackground="#0068f0", highlightthickness=3, relief="groove", command=getName)
nameSubmit.grid(row=1,column=2)

age = tk.Label(frame1, text="How old are you?", font = ('Avenir',15), bg="#001245", fg="#0068f0").grid(row=2, pady=10, padx=(80, 50))

agevariable = IntVar(frame1)
agevariable.set("8") # default value

ageDropdown = OptionMenu(frame1, agevariable, "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18")
ageDropdown.grid(row=2, column=1)


def getAge ():  
    age = agevariable.get()
    print(age)

ageSubmit = tk.Button(frame1, text="Submit", relief="groove", highlightbackground="#0068f0", highlightthickness=3, command=getAge)
ageSubmit.grid(row=2,column=2)

wakeUp = tk.Label(frame1, text="What time do you wake up at on weekdays?", font = ('Avenir',15), bg="#001245", fg="#0068f0").grid(row=3, pady=10, padx=(80, 50))

wakeUpVariable = StringVar(frame1)
wakeUpVariable.set("6:00am") # default value

ageDropdown = OptionMenu(frame1, wakeUpVariable, "6:00am", "6:30am", "7:00am", "7:30am", "8:00am", "8:30am", "9:00am", "9:30am", "10:00am", "10:30am", "11:00am")
ageDropdown.grid(row=3, column=1)


def getWakeUp ():  
    wakeUp = wakeUpVariable.get()
    print(wakeUp)

wakeUpSubmit = tk.Button(frame1, text="Submit", relief="groove", highlightbackground="#0068f0", highlightthickness=3, command=getWakeUp)
wakeUpSubmit.grid(row=3,column=2)

def showWakeUp ():
    if wakeUpVariable.get() == "6:00am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="8:00pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
            print("hi")
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="9:00pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "6:30am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="8:30pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="9:30pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "7:00am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="9:00pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="10:00pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "7:30am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="9:30pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="10:30pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "8:00am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="10:00pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="11:00pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "8:30am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="10:30pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="11:30pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "9:00am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="11:00pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="12:00am", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "9:30am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="11:30pm", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="12:30am", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "10:00am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="12:00am", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="1:00am", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "10:30am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="12:30am", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="1:30am", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
    if wakeUpVariable.get() == "11:00am":
        if agevariable.get() <= 12: 
            bedtimeLabel = tk.Label(frame2, text="1:00am", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)
        if agevariable.get() >= 13: 
            bedtimeLabel = tk.Label(frame2, text="2:00am", font = ('Avenir',15), bg="#001245", fg="#0068f0")
            bedtimeLabel.grid(row=3, column=1)

def cont ():
    frame1.pack_forget()
    frame2.pack()
    name = e1.get()
    nameTitle = tk.Label(frame2, text=name+"'s Sleep Calculator", font = ('Avenir',35), bg="#001245", fg="#0068f0")
    nameTitle.grid(row=0, column=0, columnspan=2)
    bedtimeQ = tk.Label(frame2, text="What is the latest reasonable bedtime for me during weekdays?", font = ('Avenir',15), bg="#001245", fg="#0068f0")
    bedtimeQ.grid(row=3, column=0)
    bedtimeBtn = tk.Button(frame2, text="Show", relief="groove", highlightbackground="#0068f0", highlightthickness=3, command=showWakeUp)
    bedtimeBtn.grid(row=3, column=2)
    yourWakeUp = tk.Label(frame2, text="My weekday wake up time: "+str(wakeUpVariable.get()), font = ('Avenir',15), bg="#001245", fg="#0068f0")
    yourWakeUp.grid(row=1, column=0)
    yourAge = tk.Label(frame2, text="My age: "+str(agevariable.get()), font = ('Avenir',15), bg="#001245", fg="#0068f0")
    yourAge.grid(row=2, column=0)
    
continueButton = tk.Button(frame1, text="Continue", highlightbackground="#0068f0", highlightthickness=3, relief="raised", command=cont)
continueButton.grid(row=4, column=1)




frame1.pack()
    

root.mainloop()