""" time.time() this function return us the time take the code for exciquite 

    time.time() 
    time.sleep() - how many time python take to run the next code or output
    time.strftime() - formate a time value as a string, based on a specific formate.Thats means it show us the local 
    time. 
    time.localtime() - this said us the local time

"""

import time

# def usingwhile():
#     i = 0 
#     while i<20000:
#         print(i)
#         i = i+1

# def usingfor():
#     for i in range(20000):
#         print(i)

# init = time.time()
# usingwhile()
# t1 = time.time() - init

# init = time.time()
# usingfor()
# t2 = time.time() - init

# print(t1)
# print(t2)
# # print(time.time)


"""     time.sleep()            """

# print("hi barun")
# time.sleep(4)
# print("now i am print after 4 sec.")

"""     time.strftime()     """

t = time.localtime()
formated_time = time.strftime("%Y- %m-%d  %H:%M:%S", t)
print(formated_time)