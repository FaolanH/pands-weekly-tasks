# week7_txtfile.py
# Week 7 Assignment - read in a txt file and count the number of 'e'
# Author: Faolán Hamilton

# I found a brilliant source for this (reference B) and

# Define the function, include the file name, and letter to reference later
def loremfile(file_name, letter):
    # A - bring in the text file, including the letter 'r' means it will read in the file as we don't need to edit it
    loremfile = open("week7_loremipsum.txt","r")
    # This step actually reads the file 
    text = loremfile.read()
    
    # Setting the count to 0 to begin with, will show how many 'e' there are
    count = 0 
    
    # char represents character
    for char in text:
        if char == letter:
            # This adds 1 every time an e is found
            count += 1
    return count

print (loremfile("week7_loremipsum.txt", "e"))

# References

# A - Reading in a file: https://campus.datacamp.com/courses/introduction-to-importing-data-in-python/introduction-and-flat-files-1?ex=2
# B - Main source for finding how many time a letter appears: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# C - dummy text source: https://www.lipsum.com/feed/html

#----------End----------#