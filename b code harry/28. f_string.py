''' string formationg er jonno bebohar kora hoy '''
# # in previois we face some problem in string formating that is:
# post = "my name is {}. i read in class {}"
# name = "rahim"
# edu = "10"
# print(post.format(name , edu))
''' problem is if we change the variable place then it get ans but that ans is rong'''


""" f_string"""
# here we derectly use the variable name into the 'f"   " ' 

# country = "bangladesh"
# village = "nageswari"
# print(f" my village name is {village}. i live in {country}") 
# # need not to indicate the variable place 



""" docstring - ফাংশনকে সঠিকভাবে বোঝার জন্য বিস্তারিত সাথে দিয়ে দেয় """

def my_function(n):
    '''take a number & square of this number. '''
    print(n**2)
    # if we write the comment here. we don't call it is a doc.
    # all time it write into the below of the function
    
# calling
my_function(2)
# print the comment that we call docstring
print(my_function.__doc__)

''' in termina write 'python' then 'import this'
    it give us a poime thai is the zen of pthon '''