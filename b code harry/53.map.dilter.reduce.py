''' find square in a list'''
# list = [2,4,5,6,4,5,3]
# def square(x):
#     return x*x

# new_list = []
# for i in list:
#     squa = square(i)
#     new_list.append(squa)

# print(new_list)

'''now using (map) function and short the program '''
# list1 = [2,4,5,6,4,5,3]
# def square(x):
#     return x*x

# # new_list = map(square, list) # its returan a map object now make this object as a list

# new_list = list(map(square, list1))# 1st- what we do, 2nd- which variable are use
# print(new_list)


''' now using (filter) function to filter something
1st we write the condition (as a function) and input this function
'''
# list1= [2,4,5,6,4,5,3]
# def filter_func(x):
#     return x<5

# new_list = list(filter(filter_func, list1))
# print(new_list)

''' need to understand this function
if we need to sum of a list then we use reduce function
    1st need to input the reduce function from functools '''

list1= [2,4,5,6,4,5,3]
from functools import reduce
# import functools
# print(dir(functools)) # check which are include in the functools
def red(x , y):
    return x+y
sum = reduce(red, list1) # sum the list value one by one
print(sum)