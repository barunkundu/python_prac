''' now write a secrate code
and decode the code'''

coding = input("what you like coding(for 1) or decoding(for 0): ")
if coding == "1":
    coding = True
    print("you choose coding.\n")
else:
    coding = False
    print("you choose decoding.\n")

# coding = True if(coding == "1") else False
# print(coding)

# coding = False
code = input("enter your code: \n")
code_sp = code.split()
# coding = False   
if(coding):
    new_wowrd = []
    for word in code_sp:
        if len(word) >= 3:
            r1 = "DDD"
            r2= 'RRR'
            newcod = r1 + word[1:] + word[0] + r2
            new_wowrd.append(newcod)
            # print(newcod)
        else:
            newcod = word[::-1]
            new_wowrd.append(newcod)
            # print(newcod)
    print( " ".join(new_wowrd))
else:
    new_wowrd = []
    for word in code_sp:
        if len(word) >= 3:
            newcod = word[3:-3]
            # print(newcod)
            newcod =newcod[-1] +newcod[:-1] 
            new_wowrd.append(newcod)
            # print(newcod)
        else:
            newcod = word[::-1]
            new_wowrd.append(newcod)
    #         # print(newcod)
    print( " ".join(new_wowrd))
