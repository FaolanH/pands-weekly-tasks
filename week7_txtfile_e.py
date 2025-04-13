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
def loremfile(*e):
    loremfile = open("loremipsum.txt","rt") as file:
    f.read()

    for letter in e:
        loremfile += loremfile.find("e")
    loremfile.close()
    return loremfile

print (loremfile)




