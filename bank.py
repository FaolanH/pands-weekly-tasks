#bank.py
#Prompt the user and read in two money amounts (in cent),Add the two amounts and 
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#Author: Faolán Hamilton

#Prompt the user and read in two money amounts (in cent)
Amount1 = int(input ("Amount1(in cent)"))
Amount2 = int(input ("Amount2(in cent)"))
#Add the two amounts, and divide by 100 to get the amount in euros
Sum = ((Amount1 + Amount2) / 100)
#print the sum, formatted with the € and c and with a context sentence 
print (f"The sum of these two amounts are €{Sum}c")