"""Python does not have a character data type, a single character is simply a string with a length of 1.

    Square brackets can be used to access elements of the string."""

## strat in 0,1,2,3,..................


x = "fruit, bananna"
print(x[1])
# find length
print(len(x))

## check string

# To check if a certain phrase or character is present in a string, we can use the keyword 'in'.

text = """The worn inscription on the tombstone, 
    weathered by time, offered only a name and a date. 
    But beneath the surface, a life story awaited to be unearthed."""

print(len(text))

print("name " in text)

print("barun" not in text)

# using if statement 

if "and" in text:
    print("yes")

if "kundu" not in text:
    print("yes")
