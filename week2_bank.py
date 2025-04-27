# week2_bank.py
# Week 2 Assignment: Print the sum of two amounts in euros and cents provided through user input
# Author: Faolán Hamilton

# Prompt the user and read in two money amounts (in cents)
# Read in both amounts separately so they can be added
# A - The int before input ensures the input is a whole, positive number
amount_1 = int(input ("Please enter the first amount (in cents): "))
amount_2 = int(input ("Please enter the second amount (in cents): "))
# Create a variable called sum, add the two amounts, and divide by 100 to get the amount in euros
# B - I had initially struggled with how to get the amounts in cents on the first go, got the idea for this
# on a week 4 lab called average.py
sum = ((amount_1 + amount_2) / 100)
# Print the sum, formatted with the € and c and with a context sentence 
print (f"The sum of the two amounts in euros and cents is €{sum}c")

# References

#A - Pands 2.4 first programs, Andrew Beatty: https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fandrew%5Fbeatty%5Fatu%5Fie%2FDocuments%2Fpands%202025%20%28private%29%2Fvideos%2Fpands%202%2E4%20first%20programs%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ed2d84c52%2D4219%2D4106%2Db73f%2D1aa2c636a254
#B - Lab 4.2 Loops, Andrew Beatty: https://vlegalwaymayo.atu.ie/pluginfile.php/1496536/mod_label/intro/Lab%204.2%20loops.pdf?time=1676413047731

#----------End----------#