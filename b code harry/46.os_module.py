""" "os" this module is a build in module. use of this module if we like to delete 
    ,add any file or any folder in our coumputer we can easyly used this module
    and make complete our work  """

''' now we make a folder (barun) and also make another some folder into this barun folder'''

# import os
# # os.mkdir("data") == used when main file are not exits, it makes a folder 
# if (os.path.exists("data")): # when folder is exits
#     # os.mkdir("data")
#     for i in range(0,100):
#             os.mkdir(f"data/day{i+1}")


''' now we like to rename our folders '''
# import os
# if (os.path.exists("data")):
#     for i in range(0,100):
#         os.rename(f"data/day{i+1}", f"data/rahim {i+1}")

''' now we like to now how many folder in a folder'''
# import os 
# folders = os.listdir("data")
# # print(folders) # it gives the folders as a list
# # print(len(folders))

# for folder in folders:
#     print(folder)     # it gives us the folders one by one


'''now we like to know how many file into the "f"data/{folder} '''
# import os
# folders = os.listdir("data")
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))  # ফোলডারের মধ্যে কি কি ফাইল আছে তা দিয়ে দেবে


""" need to read in details of os method visit this two link
    (https://www.w3schools.com/python/module_os.asp)
    (https://docs.python.org/3/library/os.html)"""