fishfinder1 = int(input("First Fish Reading: "))
fishfinder2 = int(input("Second Fish Reading: "))
fishfinder3 = int(input("Third Fish Reading: "))
fishfinder4 = int(input("Four Fish Reading: "))

if fishfinder1 < fishfinder2 < fishfinder3 < fishfinder4:
	print("Fish Rising")

if fishfinder1 > fishfinder2 > fishfinder3 > fishfinder4:
	print("Fish Diving")

if fishfinder1 == fishfinder2 == fishfinder3 == fishfinder4:
	print("Constant Depth")

else:
	print("No Fish.")