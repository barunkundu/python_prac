def game():
    return 9999

score = game()
# print(score)
# print(type(score))

# with open('D:/unacademy/example/9 example/highscore.txt') as f:
#     hi_scor_str = f.read()
# if hi_scor_str == '8888':
#     with open('D:/unacademy/example/9 example/highscore.txt','w') as f:
#         print(f.write(str(score)))
        
# elif int(hi_scor_str) < score:
#     with open('D:/unacademy/example/9 example/highscore.txt','w') as f:
#         print(f.write(str(score)))


file = open('D:/unacademy/example/9 example/highscore.txt')
prev_high_score = file.read()
# print(type(prev_high_score))

if int(prev_high_score) < score:
    file = open('D:/unacademy/example/9 example/highscore.txt', 'w')
    file.write(str(score))
    file = open('D:/unacademy/example/9 example/highscore.txt') 
    print(file.read())
elif int(prev_high_score) == score:
    print("previous score and present score is same ")
else:
    print("pevious high score higher then the present score")