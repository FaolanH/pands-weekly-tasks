#week6_squareroot.py

#Author: Faolán Hamilton

#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#You should create a function called <tt>sqrt</tt> that does this.
#I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
#I suggest that you look at the newton method at estimating square roots. 

#I found an article discussing this, and re-formulated it as my own! This code is contributed by AnkitRai01
#source: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

'''
#----------------My_start----------------------
positive_number = float(input("Please enter a postive number: "))
square_root = 1

#print (f"The square root of {positive_number} is approx. {square_root}")
def square_root(<tt>sqrt</tt>):

print (square_root(<tt>sqrt</tt>))

#-------------------article answer----------------------
# Function to return the square root of a number using Newtons method 
def square_root(n, l) :

	# Assuming the sqrt of n as n only 
	x = n 

	# To count the number of iterations 
	count = 0

	while (1) :
		count += 1

		# Calculate more closed x 
		root = 0.5 * (x + (n / x)) 

		# Check for closeness 
		if (abs(root - x) < l) :
			break

		# Update root 
		x = root

	return root 

# Driver code 
if __name__ == "__main__" : 

	n = float(input("Please enter a postive number: "))
	l = 0.00001


print (f"The square root of {n} is approx. {square_root(n, l)}")
'''

#---------------------AI----------------------------
def sqrt_newton_raphson(s, tolerance=1e-10):
    x = s
    while True:
        root = 0.5 * (x + s / x)
        if abs(root - x) < tolerance:
            return root
        x = root

# Example usage:
s = float(input("Please enter a postive number: "))
print (f"The square root of {s} is approx. {sqrt_newton_raphson(s)}")


#Both have a similar answer, but the AI's formula is shorter.