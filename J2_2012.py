fishfinder1 = int(input(""))
fishfinder2 = int(input(""))
fishfinder3 = int(input(""))
fishfinder4 = int(input(""))

if fishfinder1 < fishfinder2 < fishfinder3 < fishfinder4:
	print("Fish Rising")
	

if fishfinder1 > fishfinder2 > fishfinder3 > fishfinder4:
	print("Fish Diving")
	

if fishfinder1 == fishfinder2 == fishfinder3 == fishfinder4:
	print("Constant Depth")

else:
	print("No Fish.")