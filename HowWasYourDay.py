#Gathering preliminary info

import time

#Time including year, month, day, hour, minute, 
#and second

generaltime = time.localtime()

#Just the hour
hour = generaltime.tm_hour

#Greeting based on time of day
if  6 < hour < 12:
	print("Good Morning!")

elif 12 < hour < 17:
	print("Good Afternoon!")

elif 17 < hour < 22:
	print("Good Evening!")

elif 22 < hour < 24:
	print("Good Night!")

elif 0 < hour < 6:
	print("Why are you up so early?")

#A number from 0 to 6, based on what day it is.
dayofweek = generaltime.tm_wday

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


#input for 1-10 on how day has been.

scale = int(input("On a scale from 1 to 10. "))









