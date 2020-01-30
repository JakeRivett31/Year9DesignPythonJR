import math

limit = float(input("Enter the speed limit: "))
speed = float(input("Enter the recorded speed of the car: "))
fine = 0

overspeedlimit = speed - limit

if 0 < overspeedlimit <= 20:
	fine = 100

if 20 < overspeedlimit <= 30:
	fine = 270

if overspeedlimit > 30:
	fine = 500

if speed > limit:
	print("You are speeding and your fine is $"+str(fine)+".")

if speed <= limit:
	print("Congratulations, you are within the speed limit!")






