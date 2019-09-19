import math
def calcVolCylinder():
	#Input
	#What inputs are needed to calculate the volume of a cylinder?
	
	height = 1

	radius = 1

			

	

	unit = str(input("\nWhat is the unit you are using? (Enter abbreviated version) "))


		
		

	

	#Process
	#What formula is used to calculate the volume of a cylinder?
	radiussquared = radius * radius

	pi = math.pi
	formula = float(pi * radiussquared * height)
	formula = round(formula,2)

	#Output
	#What is important about the output?
	if radius >= 0 and height >= 0:
		
		print(str(formula) + str(unit) + "\u00B3")
	else: 
		print("\nPlease do not use negative numbers.")

	if radius == 0 or height == 0:
		print("\nThank you for using the Calculator!")

#MAIN CODE
print("Start Program")
calcVolCylinder()
print("End Program")