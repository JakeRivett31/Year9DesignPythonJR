#allows user to do basic operations
#with two digits

def main():

#input
#The numbers that will be added, multiplied, etc.

	num1 = int(input("What is number 1? "))
	num2 = int(input("What is number 2? "))
	operation = int(input("""What do you want to do? 1. Add, 2. Subtract, 3. Multiply, 4. Divide. 
Enter number: """))

	#Process

	#Addition
	if (operation == 1):
		print("Adding....")
		print(num1 + num2)
	#Subtraction
	elif (operation == 2):
		print("Subtracting....")
		print(num1 - num2)
	#Multiplication
	elif (operation == 3):
		print("Multiplying....")
		print(num1 * num2)
	#Division
	elif (operation == 4):
		print("Dividing....")
		print(num1 // num2)
	#Other
	else:
		print("I don't understand.")

main()

