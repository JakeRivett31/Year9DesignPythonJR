#This is a comment
#Comments are initiated with a #

#This program will take two integers 
#and multiply them

#Input
#The input function returns the string 
#the user entered
#All inputs start as strings
#To change the type you need to cast it
name = input("Please input your name: ")
a = input("Please input first number: ")
a = int(a)
b = input("Please input second number: ")
b = int(b)
#Process

product = a * b 

#Output

print("Hi, " + name)
print("The product of "+str(a)+" and "+str(b)+" is "+str(product)+".")