''' lambda is a anonymouse(নাম বিহীন) function. that is used to comprese our function
    this make function as a variable but work as function, but take data as a function medule 
    function is: lambda argument : expression'''

# def sum(x):
#     return x*3
# print(sum(2))

# sum = lambda x : x*3
# print(sum(2))

""" we can also used a lambda in a functions argument. now see this"""
sum = lambda x : x+3

def barun(func, x):
    return 7 + func(x)
# sum(2)
print(barun(sum, 2)) # here we used sum as a function argument
                     # also we ca derectly used "lambda argument : expression" in the place of here
## print(barun(lambda x : x+3, 2))