## some problems solve

'''

    3. crate a class employee and add salary and increment peoperties to it.
        write a method salary after increment method with a @peoperty decorator
        with a setter which changes the calue of increment based on the salary
    4. write a class complex to represent complex numbers along eoth ocerloaded
        operators + and * which add and multiplies them
    5. weite a class vector representing a vector of n dimension. overload the 
        + and * operator which  calculate the sum and the dot product of htem
    6. writh  __str__ method to print the cector as follows: 
                    7i^ + 8g^ + 10r^ 
        assume vector of dimension 3 for this problem
    7. overide the __len__() method on vector of problem 5 to display the dimension
        of the vector.'''



''' 1. create a class 2d.vector and use it to creat another class representting
      a 3d.vector''' 

# class two_d_vector:
#     print("vectors")

#     def __init__(self,i, j):
#         self.ivalue = i
#         self.jvalue = j

#     def __str__(self):
#         return f"{self.ivalue}i + {self.jvalue}j \n"

# class three_d_vector(two_d_vector):

#     def __init__(self,i , j , k):

''' when we need to call the mother method this time we use to the super().method constractor'''

#         super().__init__(i, j)         ## also the example of super() constractor
#         self.kvalue = k
    
#     def __str__(self):
#         return f"{self.ivalue}i + {self.jvalue}j + {self.kvalue}k"


# vector_1 = two_d_vector(3, 4)
# print(vector_1)
# vector_2 = three_d_vector(1,2,3)
# print(vector_2)
        







'''2. crate a class pet's from a class animals and further create class dog
    from pets. add a method break to class dog.'''

# class animals:
#     def __init__(self, animal):
#         self.animal = animal

# class pets(animals):
#     def __init__(self, animal):
#         super().__init__(animal)
#         self.pet = animal[:2]


# ani = animals(["birds", "dog", "tiger", "banor", ])
# print(ani.)
# # pets()



'''Qs. Define a Circle class to create a circle with radius r using the constructor.

Define an Area() method of the class which calculates the area of the circle.

Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.'''

# class circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.1416 * self.radius **2

#     def parameter(self):
#         return 2 * 3.1416 * self.radius
    
#     def info(self):
#         print(f"area is: {c1.area()} \nparameter is: {c1.parameter()}")

# c1 = circle(44)
# print(c1.parameter())
# print(c1.area())
# c1.info()


"""Qs. Define a Employee class with attributes role, department & salary. 
This class should have a showDetails() method.
Create an Engineer class that inherits properties from Employee & has additional attributes: name & age."""

class employee():
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    # def showdetails(self):
    #     print(f"name: role: {self.role} \ndept: {self.dept} \nsalary: {self.salary}")

class eng(employee):
    def __init__(self,name, age):
        super().__init__("maneger", "seals", 2000)
        self.name = name
        self.age = age

    def showdetails(self):
        print(f"name: {self.name} \nage: {self.age} \nrole: {self.role} \ndept: {self.dept} \nsalary: {self.salary}")

e1 = eng('barun', 28)
print(e1.showdetails())

print(e1.__dict__) # take all attribuite and make a tuple 
print(help(e1)) # it said us details about in our class or anything which we need 

"""Qs. Create a class called Order which stores item & its price.

Use Dunder function __gt__() to convey that:

order1 > order2 if price of order1 > price of order2"""


# class order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
    
#     def __gt__(self, order2):
#         return self.price > order2.price 


# order1 = order("apple", 45)

# order2 = order("dalim", 64)
# print(order1>order2)


# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def line():
#     print("the number is")

# @log_function_call
# def my_function(a, b):
#     return a + b

# a = my_function(1,2)
# print(a)
