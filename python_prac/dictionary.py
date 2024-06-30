"""Dictionary - is a collection which is ordered** and changeable. No duplicate members.
    
    -Dictionaries are used to store data values in key:value pairs.
    - Dictionary items are presented in key:value pairs, and can be referred to by using the key name."""

identy = {
    "name": "barun",
    "titel": "kundu",
    "uni": "IU",
    "dept":"stat",
    "roll": 182034
}
# print(identy)

# print(len(identy))

'''access items '''

# print(identy["name"])

# x = identy.get("uni")
# print(x)

# print(identy.keys())

'''change or add items'''

# identy["name"] = "karim" # change the keys
# print(identy)

# identy.update({"plase": "kustia", "gram":"sekhpara"}) # used to update the or add item in dictiomary
# print(identy)

'''remove item'''

# identy.popitem()
# print(identy)


# identy.pop("name")
# print(identy)

## also we use dict.clear() it clear the dict data but dict. exists