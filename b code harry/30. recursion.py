''' if we call a function which into in the same function
    (recursion is the process of defining something in terms of itself)
(ফাংশনের মধ্যে যদি আমরা ওই ফাংশনকেই কল করি তাহলে তাকে recursion বলে)'''

# # find the factorial of a number
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))



''' fibonacci series'''
# where f0=0 and f1=1
# fn = f(n-1) + f(n-2)

# f1 = 1
# f0 = 0
# def func(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return func(n-1)+ func(n-2)
# print(func(6))
