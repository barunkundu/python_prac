""" like: downlode a file using this link and save that file in a name (which we provide)"""

""" the below code only save picture which naem we are provide """

# import argparse
# import requests

# # make instanse
# parser = argparse.ArgumentParser()

# # copy from net
# def download_file(url, local_filename):
#     # local_filename = url.split('/')[-1]
#     # NOTE the stream=True parameter below
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 # If you have chunk encoded response uncomment if
#                 # and set chunk_size parameter to None.
#                 #if chunk: 
#                 f.write(chunk)
#     return local_filename

# # add command line argument
# parser.add_argument("url", help="use the url to downlode the file ")
# parser.add_argument("output", help="by which name you want to save")
# # parser.add_argument("-o", "--output", help=None)

# args = parser.parse_args() # above argument are parser

# print(args.url)
# print(args.output)
# download_file(args.url, args.output)

""" use the above code for downlode the picture if you save the picture setting your name"""
"""python 85_comand_line_utility.py https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg 
    kundu.jpg"""





""" this bellow code save file if we don't give any name"""

import argparse
import requests

# make instanse
parser = argparse.ArgumentParser()

# copy from net
def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

# add command line argument
parser.add_argument("url", help="use the url to downlode the file ")
# parser.add_argument("output", help="by which name you want to save")
parser.add_argument("-o", "--output", help=None)

args = parser.parse_args() # above argument are parser

print(args.url)
print(args.output)
download_file(args.url, args.output)

""" use the above code for downlode the picture if you don't set any name then it save it's on name
    and if you give the name the this code save your picture in your name"""
"""python 85_comand_line_utility.py https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg 
   -o kundu.jpg"""