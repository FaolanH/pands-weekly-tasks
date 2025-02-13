# accounts.py
# read in a 10 character account number and output the account number with only the last 4 digits 
# showing (and the first 6 digits replaced with Xs).
# Author: Faolán Hamilton

#Please enter an 10 digit account number: 1234567890
#XXXXXX7890
#Extra: Modify the program to deal with account numbers of any length (yes that is a vague requirement, 
#comment your assumptions)

#Python lists on Datacaamp
account_number = list(input("Please input your 10 digit account number: "))
account_number [0:5] = 'XXXXXX'
#a mix of stack overflow which had converting strings to list led me to co-pilot for the reverse
#my_list = ['apple', 'banana', 'cherry'] \n result = ', '.join(my_list) \nprint(result)  # Output: apple, banana, cherry

redactded_account_number = '' .join(account_number)
print (f"For security purpose, your account number has been redacted to only show the last four digit: {redactded_account_number}")

#This did not work as intended, printed on a new line each time 
# print (account_number [1])
# print (account_number [2])    
# print (account_number [3])
# print (account_number [4])
# print (account_number [5])
# print (account_number [6])
# print (account_number [7])
# print (account_number [8])
# print (account_number [9])

#For the extra part, this can already handle any number of digits as it is a list, the list range will need to be updated to redact more 
