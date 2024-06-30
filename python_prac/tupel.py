"""Tuple - is a collection which is ordered and unchangeable. Allows duplicate members 
    - that is written round braket"""

mylist = ('fruits', 'akmol', 'kihoiche ', 'fata', 'sala')
# print(type(mylist))
# items calling or access same as previous

# if "fata" in mylist:
#     print("yea")

"""update or remove or change item in a tuple

    we cannot update items in a tuple. 1st we convert the tuple in list
    and update or remove or change item and again make it tuple"""

y = list(mylist)
# print(type(y))
# y.append("oooooooooo")
# or
y[1] = "oooooooo"
mylist = tuple(y)
print(type(mylist))
print(y)