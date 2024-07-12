""" kun banega karor pati"""
questions = [["1.what is  the capital of bangladesh", "dhaka", "rajshahi", "rangpur", "kurigram",1],
             ["2.what is  the capital of india", "dhaka", "rajshahi", "rangpur", "kurigram",2],
             ["3.what is  the capital of china", "dhaka", "rajshahi", "rangpur", "kurigram",3],
             ["4.what is  the capital of japan", "dhaka", "rajshahi", "rangpur", "kurigram",4],
             ["5.what is  the capital of vutan", "dhaka", "rajshahi", "rangpur", "kurigram",1],
             ["6.what is  the capital of bangladesh", "dhaka", "rajshahi", "rangpur", "kurigram",2],
             ["7.what is  the capital of kolombia", "dhaka", "rajshahi", "rangpur", "kurigram",3],
             ["8.what is  the capital of bangladesh", "dhaka", "rajshahi", "rangpur", "kurigram",4],
             ["5.what is  the capital of kurigram", "dhaka", "rajshahi", "rangpur", "kurigram",1]
             ]

levels = [1000, 2000, 3000, 4000,5000,6000,7000,8000,9000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"{question[0]}")
    print(f"question for tk. {levels[i]} ")
    print(f"a. {question[1]}       b. {question[2]} ")
    print(f"c. {question[3]}       d. {question[4]}\n ")
    reply = int(input("wite your ans 1-4 or quter for 0 : "))

    if reply == 0:
        print("i quite the game.\n")
        money = levels[i-1]
        break
    elif reply == question[-1]:
        print("correct ans.")
        print(f"you win {levels[i]}\n")

        if i==2:
            money = 3000
        elif i==5:
            money = 6000
        elif i==8:
            money = 9000         

    else:
        print("rong ans.")
        break
print("your take home money is", money)