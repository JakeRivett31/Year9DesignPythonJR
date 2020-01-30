data = open("randomDataExtract2.txt","r")

datastring = data.read()

datalist = datastring.split("\n")

for i in range(0, len(datalist),1):
    datalist[i] = datalist[i].replace(",","")
    datalist[i] = float(datalist[i])

smallest = datalist[0]

for i in range(0, len(datalist),1):
	if smallest > datalist[i]:
		smallest = datalist[i]


print("Smallest number is: "+str(smallest))


largest = datalist[0]

for i in range(0, len(datalist),1):
	if largest < datalist[i]:
		largest = datalist[i]

print("Largest number is: "+str(largest))

value = input("What number do you want to set as upper limit?")
value = float(value)

datalist = sorted(datalist)

for i in range(0, len(datalist),1):
	if datalist[i] > value:
		for num in range(int(value), len(datalist),1):
			datalist.remove(num)
			
	print("You have set your upper limit to: "+str(value))


print(datalist)

	