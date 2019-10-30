import tkinter as tk

file = open("GuiCalc.txt","a")

file.write(str(r)+"\n")
file.write(str(h)+"\n")
file.write(str(volume)+"\n")

file.close()