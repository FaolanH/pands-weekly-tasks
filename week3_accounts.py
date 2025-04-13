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


#AI Question: how do I replace every digit except the last 4 in a list to 'X' in python?

#AI Answer: numbers = ["1234567890", "9876543210", "5555555555"]
#masked_numbers = ["X" * (len(num) - 4) + num[-4:] for num in numbers]
#print(masked_numbers)

#My output was giving me numbers
#This is my input, I am getting a list with no x's back in my output: ser_input_account = list(input("Please input your 10 digit account number: ")) redacted = '' .join(user_input_account [0:-4]) redacted_account = ["X" * (len(r) - 4) + r[-4:] for r in redacted] print (f"For security purpose, your account number has been redacted to only show the last four digit: {redacted_account}")

#Recommendation AI - user_input_account = input("Please input your 10-digit account number: ")

#redacted_account = "X" * (len(user_input_account) - 4) + user_input_account[-4:]

#print(f"For security purposes, your account number has been redacted: {redacted_account}")



user_input_account = input("Please input your 10 digit account number: ")

redacted_account = '' .join(["X" * (len(user_input_account) - 4) + user_input_account[-4:]])

print (f"For security purpose, your account number has been redacted to only show the last four digit: {redacted_account}")

'''

2345678
#a mix of stack overflow which had converting strings to list led me to co-pilot for the reverse
#my_list = ['apple', 'banana', 'cherry'] \n result = ', '.join(my_list) \nprint(result)  # Output: apple, banana, cherry

if len(account) > 10 or len(account) < 10: 
    print ("Please input your 10 account numbers")

#redactded_account = '' .join(account)

#this part is not working?

if isinstance (account = int):
    print ("Please only input whole, positive numbers")

#remembered len from lengths, got confirmation from stack overflow (https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths)
if len(account) > 10 or len(account) < 10: 
    print ("Please input your 10 account numbers")

else:
    print (f"For security purpose, your account number has been redacted to only show the last four digit: {account}")

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
'''