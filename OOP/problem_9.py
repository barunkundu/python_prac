# import pyttsx3

# # Initialize the engine
# engin = pyttsx3.init()
# text = "hi barun. how are you."

# # Make Python speak
# engin.say(text)

# # Wait and let it finish speaking
# engin.runAndWait()



"""Input: The program will receive a Python list containing one or more names (strings). 
    An example list l = ["Rahul", "Nishant", "Harry"] is given.

    Processing: For each name in the input list, the program needs to utilize the text-to-speech functionality 
    available through the win32 API. This API provides access to features of the Windows operating system. 
    The program should construct a specific phrase that includes the current name from the list.

    Output: The program should audibly pronounce these constructed phrases. The example shows that for each name, the program should say something like "Shoutout to [Name]". So, for the given list, it should pronounce:

    "Shoutout to Rahul"
    "Shoutout to Nishant"
    "Shoutout to Harry" """

import pyttsx3
engin = pyttsx3.init()

names = ["barun", "priya", "kundu"]
for name in names:
    engin.say(f"hello {name}")
    engin.runAndWait()







    




