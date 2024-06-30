mylist = ['bananna', 'apple', 'naspati', 'rahim']
print(len(mylist))

# same as string  scaling 

print(mylist[1])

# mind it-  it all time gives us less one value
# The search will start at index 2 (included) and end at index 4 (not included).
print(mylist[2:4])

print(mylist[:2])

print(mylist[1:])



## change list items

mylist[0:1]= ['fruits']
print(mylist)

mylist1 = ['bananna', 'apple', 'naspati', 'rahim', 'karim']
mylist1[1:4] = ['fruits1']
print(mylist1)
