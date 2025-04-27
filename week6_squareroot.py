# week6_squareroot.py
# Take in a positive floating-point number and output an approximation of the square root
# Author: Faolán Hamilton

# Initially, I had started with just the user input piece as a float, then went to define the square root
# as a function. I commited my start then when I realised I did not know how to move on! 
# I found several articles on the topic and an AI answer that I wasn't happy with, then came across a 
# Stack overflow article on it which made much more sense to me. 

# Inputting two separate functions that are defined makes more sense to me, other methods only included one
# as the user on stack overflow only included the output and no better descriptions, I asked AI to help 
# describe each step to me (see reference below)
# first step, the function is defined and named (check_value)
def check_value(x, estimate):
	# with the help of the AI explanation, they described this as the absolute difference being returned, 
	# I confirmed this by looking at a W3 schools explanation (referenced below)
	# abs returns the absolute value of estimate*estimate - x if it is less than 0.001
    return (abs(estimate*estimate - x) < 0.001)

# the function called newton 
def newton(x, estimate):
	# this while loop sees if check_value is False (estimate squared is not < 0.001)
    while not check_value(x, estimate):
		# inside the while loop is where the actual method is being applied. 
		# The Newton Raphson method approximates the roots of functions, starting with a guess and refining the result 
        estimate = (estimate + (x/estimate)) / 2.0
    return estimate
# Read in user input, which is a float
estimate = float(input("Please enter a postive number: "))

print (f"The square root of {estimate} is approx. {newton(estimate,1):.4f}") # I also wanted to ensure the answer was only 4 decimal places instead of having 16 decimal place

# References

#A - Kendrick Lamet: https://stackoverflow.com/questions/12850100/finding-the-square-root-using-newtons-method-errors 
#B - Co-pilot answer:
'''
Hello, I would like you to explain each line of code so I understand why it was done that way: def check_value(x, estimate):
 return (abs(estimate*estimate - x) < 0.001)

def newton(x, estimate):
 while not check_value(x, estimate):
 estimate = (estimate + (x/estimate)) / 2.0
 return estimate
# Read in user input
estimate = float(estimate("Please enter a postive number: "))

print (f"The square root of {estimate} is approx. {newton(estimate,1)}")

AI Answer:
Sure, I'd be happy to explain each line of code for you!

Function Definitions
def check_value(x, estimate):

This line defines a function named check_value that takes two arguments: x and estimate.
return (abs(estimate*estimate - x) < 0.001)

This line returns True if the absolute difference between estimate*estimate and x is less than 0.001. Essentially, it checks if estimate squared is close enough to x (within a tolerance of 0.001).
def newton(x, estimate):

This line defines another function named newton that also takes two arguments: x and estimate.
while not check_value(x, estimate):

This line starts a while loop that continues as long as the check_value function returns False. In other words, it keeps looping until estimate squared is close enough to x.
estimate = (estimate + (x/estimate)) / 2.0

Inside the loop, this line updates estimate using the Newton-Raphson method formula for finding square roots. It averages estimate and x/estimate to get a new estimate.
return estimate

Once the loop finishes (when check_value returns True), this line returns the final value of estimate, which is the approximate square root of x.
User Input and Output
estimate = float(input("Please enter a positive number: "))

This line reads a positive number from the user and converts it to a float. The estimate is stored in the variable estimate.
print(f"The square root of {estimate} is approx. {newton(estimate,1)}")

This line prints the approximate square root of the user's estimate number. It calls the newton function with the user's estimate as x and 1 as the initial estimate.
Summary
The check_value function ensures the approximation is close enough.
The newton function iteratively improves the estimate using the Newton-Raphson method.
The user inputs a number, and the program calculates and prints its approximate square root.
Feel free to ask if you have any questions or need further clarification!
'''
#C - W3 Schools, Absolute Value: https://www.w3schools.com/python/ref_func_abs.asp
#D - Netwon Raphson Method: https://www.geeksforgeeks.org/newton-raphson-method/
#E - Aziz Alto: https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places

#----------End----------#