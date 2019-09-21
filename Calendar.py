import time
import os

searchfile = open("CalendarData.txt","a")
#Time including year, month, day, hour, minute, 
#and second

generaltime = time.localtime()

#Just the hour
hour = generaltime.tm_hour

#Greeting based on time of day
if  6 < hour < 12:
	print("Good Morning!")
	os.system("say Good Morning!")

elif 12 <= hour < 17:
	print("Good Afternoon!")
	os.system("say Good Afternoon!")

elif 17 <= hour < 22:
	print("Good Evening!")
	os.system("say Good Evening!")


elif 22 <= hour < 24:
	print("Bon Soir!")
	os.system("say Bon Soir!")


elif 0 <= hour < 6:
	print("Why are you up so early?")
	os.system("say Why are you up so early?")


#Gets a number that is the day of the week
dayofweek = generaltime.tm_wday

#Greeting based on time of week

if dayofweek == 0:
	print("How has your Monday been so far?")
	os.system("say How has your Monday been so far?")

elif dayofweek == 1:
	print("How has your Tuesday been so far?")
	os.system("say How has your Tuesday been so far?")

elif dayofweek == 2:
	print("How has your Wednesday been so far?")
	os.system("say How has your Wednesday been so far?")

elif dayofweek == 3:
	print("How has your Thursday been so far?")
	os.system("say How has your Thursday been so far?")

elif dayofweek == 4:
	print("How has your Friday been so far?")
	os.system("say How has your Friday been so far?")

elif dayofweek == 5:
	print("How has your Saturday been so far?")
	os.system("say How has your Saturday been so far?")

elif dayofweek == 6:
	print("How has your Sunday been so far?")
	os.system("say How has your Sunday been so far?")

#Gets number for how day is going
scale = float(input("On a scale from 1 to 10. "))

#Generates response based on how day is going
if scale <= 2:
	print("I'm sorry that your day hasn't been great.")

elif 2 < scale <=4:
	print("Don't worry, it'll get better.")

elif 5 <= scale <=7:
	print("That's pretty good!")

elif 7 <= scale <=9:
	print("That's awesome!")

elif scale == 10:
	print("A perfect 10! You must be having a record-breaking day!")

else:
	print("I didn't know a day could be better than a perfect 10!")

#Input
print("Anyways, would you like to add an event or check your tasks?")

addorcheck = input("Add or Check? ")

if addorcheck == ("Add"):
	#The input for the date
	date = input("What is the date of your event? ")
	searchfile.write(str(date)+"\n")
	#The input for the time of day
	timeofday = input("What is the time of your event? ")
	searchfile.write(str(timeofday)+"\n")
	#The input for what the event actually is
	event = input("What is the name of the event? ")
	searchfile.write(str(event)+"\n")

elif addorcheck == ("Check"):
	#Input for the date that you want to check the calendar for.
	checkdate = 0
	
	checkdate = input("What is the date you are looking for? ")
	
	#Defines the variable, gives it a value to build off of.
	count=0
searchfile = open("CalendarData.txt", "r")
#Checks the file for text
numofdate = searchfile.readlines()
for line in numofdate:
    #If the the date is in the text
    if checkdate in line:
        #The count of how many times the date appears.
        count = count+1

#If there is only one event on the date, it will print event instead of events.
if count > 1:
	numofevents = (" events")

else:
	numofevents = (" event")

#Prints a staement saying how many events are on the date.
print("You have " + str(count) + numofevents + " on this day.")

#Option to see the events.
viewevents = input("Would you like to see your events on this day? Yes or no. ")



searchfile.close()


