''' {open()} this function is use to opne file in 
   python. 
    - this function takes 2 parameter: file name & mode
    - in python have 4 methods to open file
     ["r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists
    ] '''
# set the location to read the txt file
# f = open("D:/unacademy/files/kundu.txt", 'r') 

# ''' f = open("D:\\unacademy\files\kundu.txt", 'r')

#      f = open("kundu.txt")'''

# print(f.read())
# f.close()

'''if we need to read some specific lines
    ".readline()" this statement read the 1st lien'''
# print(f.readline())
# print(f.readline())

''' using loop to print a text'''

# f = open("D:/unacademy/kundu.txt", 'r') 
# for x in f:
#     print(x)
"""this is a importent thing when we used "with" statement to open a file this
    time we do not used to close a file because this statement autometically closed
    the file when its work is done
 """
with open("D:/unacademy/files/kundu.txt", 'r') as file:
    print(file.read())
