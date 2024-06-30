'''this is block of ocde only eturns when it is called
    "def" using this keyword we define function
    '''

# def my_function():
#     print("hey barun")
# # calling
# my_function()

'''information can be passed into function as argument
    '''
# def function(argument):
#     print(argument + " kundu")
# function("barun")
# function("finding")
# function("loading")

'''number of argument
    - if we have two argument in a function,  note that
      when we call the function this time need to the two
      argument'''

# def num_argu(name, ser_name):
#     print(name, ser_name)
# num_argu("barun", "kundu")

'''if we do not know how many argument are passed in 
     the function this thime we use befor the parameter
     name "*"
     this time it make tuple
     and we call the arugument write position [0,1,2,3....] '''

# def arb_args(*name):
#     print("my name is", name[1])
# arb_args("barun", "rahim")

'''keyword argument
    we write the keys in the "function(..)"
    and call and specified their name in the calling option '''

# def key_word(worker1, worker2):
#     print("worker name is", worker1)
# key_word(worker1="rahim", worker2="karim")
'''when we do not how many keys are need in our function '''

# def keys(**name):
#     print("the children name is ", name["child1"])
# keys(child1 = "rahim", child2 = "karim")

''' use a default parameter'''
# def default(religion = "sanatan"):
#     print("the religion is", religion)
# default()
# default("muslim")
# default("cristan")
# default("bodho")

'''using loop in function -- passing a list as an argument '''

# def passing(animal):
#     for x in animal:
#         print(x)
# birds = ["tiger", "dog", "hen"]
# passing(birds)

'''using "return" function to return a value'''

# def math(x):
#     return x*5
# print(math(6))
# print(math(9))
# print(math(7))

'''using "pass" statement
    - function definition can't empty. when we have a function
        but we have no content of this function, this time we
        need to avoid this error and this time we use this pass 
        statement'''

# def barun():
#     pass

# def my_function(x):
#   print(x)

# my_function(x=3)


"""recurtion"""
# we like to find the factorial of a number


def recurtion(n):
    if n < 0:
        print("not for negative numbers")
        return None
    elif n == 1:
        print(" factorial ois one: 1")
recurtion(0)
