# week7_txtfile_e.py
# Author: Faolán Hamilton

# Task - read in a txt file and count the number of es

#I learned this method with Datacamp: https://campus.datacamp.com/courses/introduction-to-importing-data-in-python/introduction-and-flat-files-1?ex=2
#The file is read in, and prints
'''
def lorem(*e):
    for l in lorem:
        print
    with open ('loremipsum.txt', mode = 'r') as f:
    print (f.read())


#loremfile = open("loremipsum.txt")
def loremfile ():
    with open ('loremipsum.txt', mode = 'r') as f:
        print (f.read())

print (loremfile)#.find("e"))  
    
#print (loremfile[0].find("e"))
'''

# found a brilliant source for this: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

def loremfile(file_name, letter):
    
    loremfile = open("loremipsum.txt","r")
    text = loremfile.read()
    
    count = 0 

    for char in text:
        if char == letter:
            count += 1
    return count

print (loremfile("loremipsum.txt", "e"))




