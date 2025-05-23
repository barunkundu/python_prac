"""Write a program to organize files within a specified folder on the computer. 
    The program should use the os module to:

    Rename all .png image files in the folder sequentially, 
    starting from 1.png up to n.png, where n is the total number of .png files.
    Perform the same renaming process for other file formats present in the folder. 
    This implies identifying different file extensions and renaming files with the same extension sequentially."""

import os
folders = os.listdir("data")
i = 1
for folder in folders:
    if folder.endswith(".png"):
        print(folder)
        os.rename(f"data/{folder}", f"data/{i}.png")
        i = i+1
    print(folder)
    








# import os 
# # remove folder
# # os.rmdir("data")

# # folders = os.listdir("data")


# # used to remove all folder into the data folder
# import shutil

# for item in folders:
#     item_path = os.path.join("data", item)
    
#     # Check if it is a folder
#     if os.path.isdir(item_path):
#         shutil.rmtree(item_path)
    

