# marks = [23,45,67,89,76,54]
# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("good barun")
#     index += 1

""" Enumerate function - in the same time it gives us
    the index number of a variable (set, tuple, list) """
# marks = [23,45,67,89,76,54]
# for index, mark in enumerate(marks):
#     print(index,mark)
#     if index==3:
#         print("good barun")


# # string type
# mylist = ['bananna', 'apple', 'naspati', 'rahim', 'karim']
# for index, list in enumerate(mylist):
#     print(index, list)
#     if index == 3:
#         break

# # if we use continue option then
# mylist = ['bananna', 'apple', 'naspati', 'rahim', 'karim']
# for index, list in enumerate(mylist):

#     if index == 3:
#         continue
#     print(index, list)

'''if we like to strat the indmx number in one or something  use'''
# "strat = " syntex
mylist = ['bananna', 'apple', 'naspati', 'rahim', 'karim']
for index, list in enumerate(mylist, start=1):

    if index == 3:
        continue
    print(index, list)
