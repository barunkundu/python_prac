# try:
#     write your code
# except:
#     print(comment)

''' when we like to run our code, we think it may be gives us some error
    this time we use this statement. we write our program into this loop
    and provide a sms then it dose not stop the programs another statement.
    other statement are run.   '''

# num = input("enter a number: ")

# ''' if user not inter the number input a charecter. 
#     program is stop in the 'print' statement which into the for loop.
#     it do not run after any statement, in this time we like
#     to run our another code we use "try......eccept statement" '''
# try:
#     for i in range(1,11):
#         print(f"{int(num)}x{i} = {int(num)*i}")
# except:
#     print("plz input the numeric value.")

# print("yes, i run this code")
# print("namota tui mara kha, ami run hoilam")


''' another some think related to the error, 
    use this statement we solved the specific error'''
# in one line may be rise 5 types of error


# try:
#     num = int(input("enter a number: "))
#     a = [3,4,6,5,2,5,7]
#     print(a[num]) #indexing the number which comes from the variable a
# except ValueError: 
#     print("plz enter a value.") # if we not input the numeric value
# except IndexError: 
#     print("plz write the right index.") # if we not input the right index
