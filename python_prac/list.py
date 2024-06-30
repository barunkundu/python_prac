""" there are 4 build in data types in python

    1.List - is a collection which is ordered and changeable. Allows duplicate members.
    2.Tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
    3.Set - is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    4.Dictionary - is a collection which is ordered** and changeable. No duplicate members.

       """
## List is a collection which is ordered and changeable. Allows duplicate members.
## list are used to multiple data in a single variable
'''used squre braket to idicate list'''

list = ["apple", "bananna", "naspati"]
print(list)

#indicates the list item 
print(list[0])  

# add new item plased end in the list
# list is changeable
# allow duplicates [same value allow]
# list cantain any data type and also contain different data type
list1 = ["barun", 'kundu', 5, True]
print(list1)

list2 = ["apple", "bananna", "naspati", "apple", "bananna", "naspati"]
print(list2)
print(type(list2))

#and we also used "list((.....))" statement to write a list
mylist3  =  list(('rahim', 'karim'))
print(mylist3)
# in this file we use many times the list word thats why list is not work in this file 
