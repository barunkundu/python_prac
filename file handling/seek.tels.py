''' seek() & tell() this two option are used to work with file objects and their 
    position with in a file
    
    seek() -  it tell the program where the program strat to read
    tell() - it said us where we seek the file that means which position the program strat to 
            read the file or show us the file current position'''


# with open("D:/unacademy/files/kundu.txt", 'r') as file:
#     # print(type(file))
#     # print(file.read())
#     file.seek(45)
#     print(file.tell())
#     # print(file.read())


''' ".truncate" it used when we need to limited our file'''

with open("D:/unacademy/files/truncate.txt", 'w')  as file: #here autometically create a file and intport the sms
    file.write("my name is barun.")
    file.truncate(10) # we need 1st 10 char that's why we use it
with open("D:/unacademy/files/truncate.txt", 'r') as file:
    print(file.read())