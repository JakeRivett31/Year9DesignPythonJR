import math
import tkinter as tk

btnrun = tk.Button(root, text = "CALCULATE", highlightbackground='#3E4149', command = runMe)
btnrun.config(fg="blue", command = runMe)
btnrun.pack(fill = tk.BOTH)





def runMe(*args):
  print("Runnning")
  r = radiusEntry.get() #gets value and stores in r
  try:
    r = float(r) #casts r to float
  except:
    r = -1

    radiusEntry.delete(0,tk.END) #deltes content of entry tk.END gets last char
    
  h = heightEntry.get() #gets value and stores in h
  try:
    h = float(h) #casts h to float
  except:
    h = -1
    
    heightEntry.delete(0,tk.END) #deltes content of entry tk.END gets last char
    
  volume = calcVolCylinder(r,h)
  print(volume)

  if volume != -1:
    output.config(state = "normal")
    output.delete("1.0",tk.END)
    result = "\n\n\tr\t= "+str(r)+" units\n\th\t= "+str(h)+" units\n\tvolume\t= "+str(volume)+" units\u00B3"
    output.insert(tk.END, result)
    output.config(state = "disabled")

    file.write(str(r)+"\n")
    file.write(str(h)+"\n")
    file.write(str(volume)+"\n")
  else:
    output.config(state = "normal")
    output.delete("1.0",tk.END)
    output.insert(tk.END, "BAD INPUT  ")
    output.config(state = "disabled")


