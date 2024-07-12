''' write a program which do not give us error, only the a word quite '''

num = input("enter a value between 4 to 9: ")

if num == "quite": 
    print(num) 
    exit()
elif int(num)<4 or int(num)>9:
    raise ValueError("between 4 to 9")
print(num)