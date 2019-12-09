import tkinter as tk

def callback(event):
    print(event.widget['text'])

main = tk.Tk()

switcher = tk.Button(main, text="click here")
switcher.grid()
switcher.bind("<Button-1>", callback)
main.mainloop();