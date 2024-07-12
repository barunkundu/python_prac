''' this is a statement, generally used when we need to call a function 
    that into in other file . very much used in math problem.we can  build a 
    functon and we can used buidin fuction which stored in "math" '''

""" 1st we see which function are stored in the math function"""
# import math
# print(dir(math))

"""find spure root of a value"""
# # num = int(input("enter a value in 1-10: "))
# import math

# # import math as m  ## another process to defime math
# # value = m.sqrt(9)

# valu = math.sqrt(9)
# print(valu)

""" derectly call which problem solved we need -- here we need to used "from math import ..." """
# from math import sqrt
# value = sqrt(9)

# # from math import sqrt as s
# # value = s(9)

# print(value)


''' now in this time we write a function in another file and used it in this program'''
from main import *
# here * means we call the all function variable etc which 
# write in the main.py file
# barun()
# print(kundu)

nice()
print(rong)
