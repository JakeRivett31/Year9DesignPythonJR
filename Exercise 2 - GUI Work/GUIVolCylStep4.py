import math
import tkinter as tk


#Function that multiplies radius and height.
def calcVolCylinder(radius, height):

	if radius >= 0 and height >= 0:
		radiussquared = radius * radius
		import math
		pi = math.pi
		formula = float(pi * radiussquared * height)
		formula = round(formula,2)
		return formula

	else:
		return -1

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

  output.config(state = "normal")
  output.delete("1.0",tk.END)
  result = "\n\n\tr\t= "+str(r)+" units\n\th\t= "+str(h)+" units\n\tvolume\t= "+str(volume)+" units\u00B3"
  output.insert(tk.END, result)
  output.config(state = "disabled")



def checkSelect():
  print(var.get())
  
#Main Code:
root = tk.Tk()
#Construction
title = tk.Label(root, text = "Cylinder Volume Calculator")
#Configuration
title.config(fg = "red", bg = "black")
#Add it to root window. 
title.pack(fill = tk.BOTH)

radiusLabel = tk.Label(root, text = "Radius:")
radiusLabel.config(anchor = "w")
radiusLabel.pack(fill = tk.BOTH)

radiusEntry = tk.Entry(root)
radiusEntry.config()
radiusEntry.pack(fill = tk.BOTH)

heightLabel = tk.Label(root, text = "Height:")
heightLabel.config(anchor = tk.W)
heightLabel.pack(fill = tk.BOTH)

heightEntry = tk.Entry(root)
heightEntry.config()
heightEntry.pack(fill = tk.BOTH)

btnrun = tk.Button(root, text = "CALCULATE", highlightbackground='#3E4149', command = runMe)
btnrun.config(fg="blue", command = runMe)
btnrun.pack(fill = tk.BOTH)

output = tk.Text(root)
output.config(width = 50, height = 10, state = "disabled", borderwidth = 2, relief = "groove")
output.pack()


var = tk.IntVar()

check = tk.Checkbutton(root, text = "High Contrast", variable = var, command = checkSelect)
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)


root.bind("<Return>",runMe)
#Building widgets goes before mainloop.
root.mainloop()

print("End Program")	




