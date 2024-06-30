# that means adding numeric and char type variable 
# in this case we use F -  formate method


a = 5 
text = f" i am {a} years old"
print(text)


## string methods w3 school 
#capitalize()	Converts the first character to upper case
text1 = """statistics is the field that deals with data: 
        how to collect it, analyze it, interpret it, and present it. 
        It's like a toolbox with methods to make sense of all the information we collect in the world. 
        Statistics helps us understand patterns, trends, and uncertainties in data.  
        Imagine you have a giant bag of colored candies. 
        Statistics gives you a way to figure out how many of each color there are,  
        the most common colors, and how unusual it is to find a specific color."""

text2 = text1.capitalize()
print(text2)

#casefold()	Converts string into lower case
text3 = text1.casefold()
print(text3)

#count()	Returns the number of times a specified value occurs in a string
# mind it python is a case sencitive program 
text4 = text1.count("statistics")
print(text4)

#find()	Searches the string for a specified value and returns the position of where it was found
text5 = text1.find("Statistics")
print(text5)

#index()	Searches the string for a specified value and returns the position of where it was found
# same as find statement 

#join()	Joins the elements of an iterable to the end of the string
a = ("bananna", "fruits", "naspati")
b = '$'.join(a)
print(b)

#upper()	Converts a string into upper case 
print(text1.upper())