# accounts.py
# read in a 10 character account number and output the account number with only the last 4 digits 
# showing (and the first 6 digits replaced with Xs).
# Author: Faolán Hamilton

#Please enter an 10 digit account number: 1234567890
#XXXXXX7890
#Extra: Modify the program to deal with account numbers of any length (yes that is a vague requirement, 
#comment your assumptions)

#Immeditely lists came to mind for this, with the feature to replace positions in the list e.g. 
#the first 6 numbers to be replaced with X
#I HAVE STILL NOT FIGURED OUT HOW TO ENSURE LIST IF NUMBERS ONLY/MAX Amount
#This slack overflow https://stackoverflow.com/questions/1277914/is-there-a-way-to-output-the-numbers-only-from-a-python-list
#maybe use boolean?


#Python lists on Datacaamp

account = list(input("Please input your 10 digit account number: "))

account [0:6] = 'XXXXXX'


#a mix of stack overflow which had converting strings to list led me to co-pilot for the reverse
#my_list = ['apple', 'banana', 'cherry'] \n result = ', '.join(my_list) \nprint(result)  # Output: apple, banana, cherry


redactded_account = '' .join(account)

if isinstance (account, float): 
    print ("Please only input whole, positive numbers")

#remembered len from lengths, got confirmation from stack overflow (https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths)
elif len(account) > 10 or len(account) < 10: 
    print ("Please input your 10 account numbers")

else:
    print (f"For security purpose, your account number has been redacted to only show the last four digit: {redactded_account}")

#This did not work as intended, printed on a new line each time 
# print (account [1])
# print (account [2])    
# print (account [3])
# print (account [4])
# print (account [5])
# print (account [6])
# print (account [7])
# print (account [8])
# print (account [9])

#For the extra part, this can already handle any number of digits as it is a list, the list range will need to be updated to redact more 
