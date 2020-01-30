import math

speed = float(input("How fast was your recorded speed?"))
limit = float(input("What was the speed limit of the road you were on?"))
fine = 0

overspeedlimit = speed - limit

if overspeedlimit <= 20:
	fine = 100

if 20 < overspeedlimit <= 30:
	fine = 270

if overspeedlimit > 30:
	fine = 500

if speed > limit:
	print("You are speeding and your fine is "+str(fine)+".")

if speed < limit:
	print("Congratulations, you are within the speed limit!")






