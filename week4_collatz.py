# week4_collatz.py
# Week 4 Assignment: User input an int, and depending on if it's odd or even have the program output collatz, ending in 1
# Author: Faolán Hamilton 

# Initially, all I had was a while loop for even and odd numbers, as well as the user input. 
# A Stack Overview forum (listed as 'A' in references below) built on this method to output the desired collatz 
# I tweaked it in a way that made sense to me, using the initial post to be refined and the last answer 
# not including the 'seen', 'set()', 'try' and 'ValueError' and using only what I understood

#defining the collatz_input function
def collatz_input(num):
    while num != 1: # ensuring that if it is equal to 1, the loop will end
        if num % 2: # any even number will be divisible by two 
            num = 3 * num + 1 # any odd number if multiplied by three + 1 will be an even number, which can then be divided by 2 resulting in an int
        else:
            num //= 2 # divides the user input by 2
        print(num, end=" ") # end=" " creates a better looking output, with all numbers on the same line with a space between them
    return num # the forum had suggested a return == 1, but this seems redundant considering the initial exclusion

# Now that the function has been defined, the number can be decided by the user!
# Using int at least confirms the type of input
num = int(input("Please enter a positive integer (whole number) greater than 1: "))

#adding this if statement in lessens the chance for user error 
if num <= 0:
    print("Try again - please only enter a positive integer (whole number): ")
# this is the final piece - now that everything is added/correct the function can be printed under the right conditions
else:
    collatz_input(num) 

# References

# A: Collatz structure - https://stackoverflow.com/questions/75745136/collatz-sequence-in-python-any-improvements
# B: formatting output using end=" " - https://stackoverflow.com/questions/18424899/print-range-of-numbers-on-same-line

#----------End----------#

