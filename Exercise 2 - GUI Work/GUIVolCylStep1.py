import math


#

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

print("Start Program")
result = calcVolCylinder(3, 4)
print(result)
print("End Program")



