import time
import os
#Time including year, month, day, hour, minute, 
#and second

generaltime = time.localtime()

#Just the hour
hour = generaltime.tm_hour

#Greeting based on time of day
if  6 < hour < 12:
	print("Good Morning!")
	os.system("say Good Morning!")

elif 12 < hour < 17:
	print("Good Afternoon!")

elif 17 < hour < 22:
	print("Good Evening!")

elif 22 < hour < 24:
	print("Good Night!")

elif 0 < hour < 6:
	print("Why are you up so early?")

#Gets a number that is the day of the week
dayofweek = generaltime.tm_wday

#Greeting based on time of week

if dayofweek == 0:
	print("How has your Monday been so far?")

elif dayofweek == 1:
	print("How has your Tuesday been so far?")

elif dayofweek == 2:
	print("How has your Wednesday been so far?")

elif dayofweek == 3:
	print("How has your Thursday been so far?")

elif dayofweek == 4:
	print("How has your Friday been so far?")

elif dayofweek == 5:
	print("How has your Saturday been so far?")

elif dayofweek == 6:
	print("How has your Sunday been so far?")

#Gets number for how day is going
scale = float(input("On a scale from 1 to 10. "))

#Generates response based on how day is going
if scale <= 2:
	print("I'm sorry that your day hasn't been great.")

elif 2 < scale <=4:
	print("Don't worry, it'll get better.")

elif 5 < scale <=7:
	print("That's pretty good!")

elif 7 < scale <=9:
	print("I wish my day would be that great, all I do is get my buttons pushed. It gets me realllllly annoyed.")

elif scale == 10:
	print("A perfect 10! You must be having a record-breaking day!")

else:
	print("I didn't know a day could be better than a perfect 10!")

#Input
print("Anyways, would you like to add an event to your calendar or ")



