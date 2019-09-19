
import math
#Open function takes 2 parameters.  Both are String
# parameter 1 is the name of the file. 
# parameter 2 is what should be done with the file. 
#	"w" - is the parameter for write.  Delete content and start with a new file. 
#	"a" - is the parameter for append. Take the file and just add more onto it
#	"r" - is read.  This is used if you need to readto file. 

file = open("data.txt","w")
#Input
#What inputs are needed to calculate the volume of a cylinder?
print(input("""\nWelcome to the Cylinder Volume Calculator!
Press enter to begin"""))

height = 1

radius = 1

		

name = str(input("What is your name? "))


unit = str(input("\nWhat is the unit you are using? (Enter abbreviated version) "))


while radius != 0 or height != 0:
	
	try:
		radius = int(input("\nWhat is the radius of the cylinder? "))
		height = int(input("\nWhat is the height of the cylinder? "))

	except:
		print("\n\t\tNumeric Input Required")
		break

	#Process
	#What formula is used to calculate the volume of a cylinder?
	radiussquared = radius * radius
	
	pi = math.pi
	formula = float(pi * radiussquared * height)
	formula = round(formula,2)
	finalanswer = str(formula) + str(unit) + "\u00B3"
	file.write(str(finalanswer)+"\n")

#Output
#What is important about the output?
	if radius == 0 or height == 0:
		print("\nThank you for using the Calculator!")
		break
		
	if radius >= 0 and height >= 0:
		print("\nHere is your volume " + name + " I hope you enjoyed!")
		print(str(formula) + str(unit) + "\u00B3")
	else: 
		print("\nPlease do not use negative numbers.")


file.close()

