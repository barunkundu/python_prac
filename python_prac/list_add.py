""" adding items in a variable, generally we used
    .apend(...)- add items end of the items 
    .insert(...)- need 2 arug. 1st where we like to add the variable & 
                2nd is which new variable we like to insert.
    .extend(... )- use when we add a list in another list """

mylist = ['bananna', 'apple', 'naspati', 'rahim', 'karim']
newlist = ['fruits', 'akmol', 'kihoiche ', 'fata', 'sala']

mylist.append('orange')
print(mylist)


mylist.insert(1, 'orange')
print(mylist)


mylist.extend(newlist)
print(mylist)

