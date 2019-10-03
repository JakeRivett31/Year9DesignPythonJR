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

btnrun = tk.Button(root, text = "CALCULATE", highlightbackground='#3E4149')
btnrun.config(fg="blue")
btnrun.pack(fill = tk.BOTH)

output = tk.Text(root)
output.config(width = 50, height = 10, state = "disabled", borderwidth = 2, relief = "groove")
output.pack()

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)
#Building widgets goes before mainloop.
root.mainloop()

print("End Program")	




