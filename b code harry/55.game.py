# import random
# item = ["s", "w", "g"]
# print(item)



# for i in range(10):

#     player = input("choose a option into the list: ")
#     compu = random.choice(item)
#     print(compu)
    

#     if player == compu:
#         print("you draw")
#     elif (player == item[0] and compu == item[2]):
#         print("you loos")
#     elif (player == item[1] and compu == item[0]):
#         print("you loos")
#     elif (player == item[2] and compu == item[0]):
#         print("you loss")
#     else:
#         print("you win")

#     x = input("play again write g: ")
#     if x=="g":
#         continue
#     else:
#         break


####### another solution ########
import random
item = ["s", "w", "g"]
print(item)
player_point= 0
comp_point= 0

for i in range(4):
    # player_point= 0
    # comp_point= 0
    def game(comp, user):
        if comp == user:
            return 0
        elif (player == item[0] and comp == item[2]):
            return -1
        elif (player == item[1] and comp == item[0]):
            return -1
        elif (player == item[2] and comp == item[1]):
            return -1
        else:
            return 1

    player = input("take a word in the item list: ")
    print("you choose", player)
    comp = random.choice(item)
    print("computer choose",comp)

    score = game(comp, player)

    if score == 0:
        print("draw")
    elif score == -1:
        print("you loos")
        comp_point = comp_point+1
    else:
        print("you win")
        player_point = player_point +1



    x = input("play again write g: ")
    if x=="g":
        continue
    else:
        break

if player_point > comp_point:
    print("you win", player_point)
else:
    print("computer win", comp_point)
