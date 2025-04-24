# week2_bank.py
# Week 2 Assignment: Print the sum of two amounts in euros and cents provided through user input
# Author: Faolán Hamilton

# Prompt the user and read in two money amounts (in cents)
# Read in both amounts separately so they can be added
# The int before input ensures the input is a whole, positive number
amount_1 = int(input ("Please enter the first amount (in cents): "))
amount_2 = int(input ("Please enter the second amount (in cents): "))
# Create a variable called sum, add the two amounts, and divide by 100 to get the amount in euros
sum = ((amount_1 + amount_2) / 100)
# Print the sum, formatted with the € and c and with a context sentence 
print (f"The sum of the two amounts in euros and cents is €{sum}c")

# References

#----------End----------