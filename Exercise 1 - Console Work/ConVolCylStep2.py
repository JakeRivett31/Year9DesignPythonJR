#Input
#What inputs are needed to calculate the volume of a cylinder?
print(input("""\nWelcome to the Cylinder Volume Calculator!
Press enter to begin"""))
height = 1
radius = 1
name = str(input("What is your name? "))
unit = str(input("\nWhat is the unit you are using? (Enter abbreviated version) "))
radius = int(input("\nWhat is the radius of the cylinder? "))
height = int(input("\nWhat is the height of the cylinder? "))

#Process
#What formula is used to calculate the volume of a cylinder?
radiussquared = radius * radius
import math
pi = math.pi
formula = float(pi * radiussquared * height)
formula = round(formula,2)

#Output
#What is important about the output?
print("\nHere is your volume " + name + " I hope you enjoyed!")
print(str(formula) + str(unit) + "\u00b23")