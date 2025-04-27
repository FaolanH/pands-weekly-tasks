# week3_accounts.py
# Week 3 Assignment: Read in a user input account number, replacing all but the last 4 digits with Xs
# Author: Faolán Hamilton

# Immediately lists came to mind for this, with the feature to replace positions in the list e.g. 
# the first 6 numbers are replaced with X, did not figure out how to ensure the input is int only 

# Define the account number using user input
account = list(input("Please input your 10 digit account number: "))

# B - remembered len from lengths, got confirmation from stack overflow
# # I had previously done this with an if loop statement instead of a while loop, and noticed 
# that it restarts the whole run and does not allow user to try input again, so a while loop makes more sense

while len(account) > 10 or len(account) < 10: 
    print ("Please input your 10 account numbers")
    account = list(input("Please input only your 10 digit account number: "))

else:
    account [0:6] = 'XXXXXX'

# C - a mix of stack overflow which had converting strings to list led me to co-pilot for the reverse
# example: my_list = ['apple', 'banana', 'cherry'] \n result = ', '.join(my_list) \nprint(result)  
# Output: apple, banana, cherry

    redacted_account = '' .join(account)
    print (f"For security purposes, your account number has been redacted to only show the last four digits: {redacted_account}")

# If the account number was over 10 digits:
# I asked the Co-Pilot about this, but the structure was different to how I did the rest, so I decided to go with my original way

# AI Question: how do I replace every digit except the last 4 in a list to 'X' in python?

# AI Answer: numbers = ["1234567890", "9876543210", "5555555555"]
# masked_numbers = ["X" * (len(num) - 4) + num[-4:] for num in numbers]
# print(masked_numbers)

# My output was giving me numbers, so I needed to dig deeper
# This is my input, I am getting a list with no x's back in my output: user_input_account = list(input("Please input your 10 digit account number: ")) redacted = '' .join(user_input_account [0:-4]) redacted_account = ["X" * (len(r) - 4) + r[-4:] for r in redacted] print (f"For security purpose, your account number has been redacted to only show the last four digit: {redacted_account}")

# Recommendation AI - user_input_account = input("Please input your 10-digit account number: ")

# redacted_account = "X" * (len(user_input_account) - 4) + user_input_account[-4:]

# print(f"For security purposes, your account number has been redacted: {redacted_account}")

'''
user_input_account = input("Please input your 10 digit account number: ")

redacted_account = '' .join(["X" * (len(user_input_account) - 4) + user_input_account[-4:]])

print (f"For security purposes, your account number has been redacted to only show the last four digit: {redacted_account}")
'''

# References

# A - Python Lists: https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists?ex=10
# B - len: (https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths)
# C - User input List: https://stackoverflow.com/questions/35582959/how-do-i-convert-user-input-into-a-list

#----------End----------#