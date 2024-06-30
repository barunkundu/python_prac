""" remove remove items , we generaly used 
    .remove(...)- remove the specific item in that list &
                if that list contain two or more same item but this method remove only similar 1st item 
    .pop(..)- pop method remove the specific item in the list &
            if we do not specify the index it's remove the last item in the list
    del var [index]- delete the specific item 
    or
    del var - it delete the complete list
    
    .clear(..)- delete the list item but the list stil remain
      """

newlist = ['fruits', 'akmol', 'kihoiche ', 'fata', 'sala']
# newlist.remove("fata")
# print(newlist)

# newlist.pop(1)
# print(newlist)

# newlist.pop()
# print(newlist)

# del newlist[0]
# print(newlist)

# del newlist[1]
# print(newlist)

# del newlist

newlist.clear()
print(newlist)
newlist.append("barun")
print(newlist)