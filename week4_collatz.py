#week4_collatz.py

# ask user to input a positive integer and output successive value calculations 
#At each step calculate the next value by taking the current value and, if it is even, 
#divide it by two, but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.

#Author: Faolán Hamilton

user_input = int(input("Please enter a positive integer (whole number): "))

#even_number = ({user_input} % 2)
#odd_number = ({user_input} *3 % 1)

while (user_input % 2) == 0:
    even = (user_input % 2)
    print (even)


    
if (user_input % 2) != 0:
    print ("odd number")
