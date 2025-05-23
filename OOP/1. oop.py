''' there are three foure pillers in oop. this are:

    1. abtruction: hiding the implimantation details of the class.
                    only show the essentiol reasult. (example: hide the unnessecary details )

    2. encapsulation: data, methods attribuites সব মিলায় আমরা যে কোডটি করলাম একেই একটা
                     ক্যাপসুল কাকারে দেখতে পারি। 


    3. inheritance
    4. polymorphisom'''


##                      del attribuites                         ##

''' use this attribuites to delet any objects into the program. now see the exampel '''

# class workers():
#     def __init__(self, name, age):
#         self.name =  name
#         self.age = age

# worker1 = workers("barun", 28)
# print("worker name is", worker1.name," and age is", worker1.age)

# # now delet the worker name
# del worker1.name
# print("worker name is", worker1.name," and age is", worker1.age) # this line show an error because we delet the workers name





##                          private objects & methods                               ##

''' in fornt of methods or objects , take double underscore make praivate methods or object "__".
    we give those methods or objects access inside the class. write a another function into the class and give those access.
    but we don't have access outside of the class.

    now see the example: '''

# class person():
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age     ## make the object private

# man = person("barun", 28)
# print(man.name)   
# print(man.name, man.__age)  ## it gives an error. because age is hidden 

''' now see another example to access the hidden variable'''

# class person():
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age     ## make the object private

#     def info(self):
#         print(self.__age)

# man = person("barun", 28)

# print(man.name)   
# print(man.info())

''' now see another example hidden methods'''

# class person():
#     def __init__(self, name):
#         self.name = name

#     def __hello(self):
#         print("hi barun")

#     def welcome(self):
#         self.__hello()  ## call the hidden method


# man = person("barun")
# print(man.name)   
# man.welcome()
# # man.__hello()   ## this gives us an error 


""" **"Create Account class with 2 attributes - balance & account no.

Create methods for debit, credit & printing the balance."** """

# class account():
#     def __init__(self, account_no, balance):
#         self.account_no = account_no
#         self.balance = balance

#     def debit(self, amount):
#         # input("enter your debit ammount: ")
#         self.balance -= amount
#         print(f"your debit amount is: {amount}")
#         print(f"your current bal is: {self.current_amount()}")

#     def credit(self, amount):
#         # input("enter your credit ammount: ")
#         self.balance += amount
#         print(f"your credit amount is: {amount}")
#         print(f"your current bal is: {self.current_amount()}")

#     def current_amount(self):
#         return self.balance

#     # def all(self):
#     #     print(f"your account_no is: {self.account_no} \n balance is: {self.balance()}\n now your current bal is: {self.current_amount()}")


# a1 = account(23, 200)
# a1.debit(100)
# a1.credit(200)



class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def debit(self):
        amount = float(input("Enter amount to debit: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Debited: {amount}")
            print(f"Current Balance: {self.current_amount()}")

    def credit(self):
        amount = float(input("Enter amount to credit: "))
        self.balance += amount
        print(f"Credited: {amount}")
        print(f"Current Balance: {self.current_amount()}")

    def current_amount(self):
        return self.balance


# Create an account
a1 = Account(account_no=12345, balance=500)

# Ask user whether to debit or credit
while True:
    print("\nChoose an action:")
    print("1. Debit")
    print("2. Credit")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        a1.debit()
    elif choice == "2":
        a1.credit()
    elif choice == "3":
        print(f"Current Balance: {a1.current_amount()}")
    elif choice == "4":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
