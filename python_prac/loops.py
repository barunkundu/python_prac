"""sometime we need repeat a set of statements in our program, in this time we use loops

    - while loop
    - for loop """

'''while loop we use some statement
    -brake
    -continoue
    -else
'''

# a = 0
# while a < 1000:
#     print(a)
#     a += 1

'''break'''
# while a < 100:
#     print(a)
#     a += 1

#     if a == 77:
#         break


'''continoue'''

# while a<10:
#     a += 1
#     if a ==4:   # skepe this value and continue the series
#         continue
#     print(a)

'''else'''

# while a < 10:
#     print(a)
#     a += 1
# else:
#     print("run when condition is no longeris true")



"""   for    """

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
'''break'''
# two times we use this break statement after and befor print
b = ['fruits', 'akmol', 'kihoiche ', 'fata', 'sala']
# for x in b:
#     print(x)
#     if x == "fata":
#         break


# for x in b:
#     if x == "fata":
#         break
#     print(x)

'''continue same as previous'''


'''range - used to generate a sequence of number. 
    we can also specify the strat stop and step size'''
# range(strat, stop, step size)

# for x in range(1,30,2): # or strat it takes by defalt 0
#     print(x)