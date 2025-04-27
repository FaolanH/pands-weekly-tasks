# week5_weekday.py
# Week 5 Assignment: Output what day of the week it is
# Author: Faolán Hamilton

# I learned how to do this through DataCamp, 'Working with Dates and Time in Python'

# Import date from datetime
import datetime 

# Initially I set the date, AI told me I could let the computer set today's date! 
# Create a date object - this would have to be changed according to the day it is 
# Today = date(2025, 3, 8, they do give the exact time to the second as well)
today = datetime.datetime.now()

# This step formats today's date as a weekday day (aka a number between 0-6 incl. 6)
day_of_week = today.weekday()

# Which day of the week is the date? The days start from 0 (Monday) and go up to 3 (Thursday)
if day_of_week <4:
    print (f"Yes, unfortunately {today.strftime('%A (%B %d)')} is a weekday")

# Well if it's a Friday, I think there should be a bit of celebration!
elif day_of_week == 4:
    print (f"Yay, finally it's {today.strftime('%A (%B %d)')}, still a weekday but nearly the weekend!")
    
# For a weekend, it is a 5 or a 6, but this can be called else as there is no other option
else:
    print (f"Today is {today.strftime('%A (%B %d)')} aka. the weekend, yay!")

#with a mixture of my DataCamp and AI to let me know which letter to use (A), we can see what day it is today

# References
#A - https://app.datacamp.com/learn/courses/working-with-dates-and-times-in-python
#B - #AI Question:
# python datetime .weekday print as day of week
# AI_Answer
# import datetime
# Get the current date
# current_date = datetime.datetime.now()
# Get the day of the week as a string
# day_of_week = current_date.strftime("%A")
# Print the day of the week
# print("Today is:", day_of_week)

#----------End----------#