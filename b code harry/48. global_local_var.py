''' global variable -- means which we used any where in function or without function
    local variables -- which we write into a function and it only used in this function
                        we do not use it out of he function '''


# x = 4  # this is call global variable
# print(x, "- i am a global variable")

# def func():
#     y = 5
#     print(y, "- i am local variable")

# func()
# print(x)

''' now need to change the global variable '''
# here we used the "global" statement

x = 5
print(x)

def fun():
    global x  # now we change the global variable
    x = 9
    y = 7
    print(y)

fun()
print(x)
