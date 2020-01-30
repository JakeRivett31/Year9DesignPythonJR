data = open("randomDataRAW.txt","r")

datastring = data.read()

datalist = datastring.split("\n")

for i in range(0, len(datalist),1):
    datalist[i] = datalist[i].replace(",","")
    datalist[i] = float(datalist[i])

print(datalist)

