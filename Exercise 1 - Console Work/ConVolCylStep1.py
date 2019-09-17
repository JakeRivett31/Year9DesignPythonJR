#Input
#What inputs are needed to calculate the volume of a cylinder?
print(input("""Welcome to the Cylinder Volume Calculator!
Press enter to begin"""))

unit = str(input("What is the unit you are using? (Enter abbreviated version) "))
radius = int(input("What is the radius of the cylinder? "))
height = int(input("What is the height of the cylinder? "))

#Process
#What formula is used to calculate the volume of a cylinder?
radiussquared = radius * radius
import math
pi = math.pi
formula = float(pi * radiussquared * height)


#Output
#What is important about the output?
print(str(formula) + str(unit))