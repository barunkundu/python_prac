''' it is a cluse- which always execute. '''
# generaly we use it when we write the program into a function

def fun():
    try:
        num = int(input("enter a number: "))
        print(num)
        return 1
    except:
        print("plz enter a integer number.")
        return 0
    finally:
        print("i am alawys execute.")
print(fun())    


