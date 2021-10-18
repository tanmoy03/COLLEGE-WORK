# Script Name: time.py
# Author: Tanmoy Debnath 121324683

# get number of minutes spent watching tv
minutes = int(input("How many minutes do you spend watching TV: "))


# save as hours 
hours = minutes // 60
# save the remaining minutes
minutes = minutes % 60

print("You spend" , hours, "hours and", minutes, "minutes watching TV.")