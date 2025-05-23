##                               inheritance
''' this is a way to create a new class from an existing class 

    --if previous class is worker , then the new class which we create is soil(worker)-this is also
    called child class.

    --into this child class we can use mother class methods and attribuit also add new methods and attribuit
    --three types of inheritance

            1. single -- child class made to used one mother class 
            2. multiple -- child class made to used more then one mother class 
            3. multilevel -- if a child class made to used another child class   ''' 


'''  now see a example also the example of single inh. '''

# class bikes:          # mother class

#     @staticmethod
#     def strat():
#         print("bike strat")
    
#     @staticmethod
#     def off():
#         print("bike off")

# class palsure(bikes):       # child class and call the mother class 
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print(f"bike name is {self.name} {self.off()}")


# bike1 = palsure("p-125cc")
# print(bike1.strat())
# bike1.info()

       


'''   example for a multiple inhe.'''

# class bikes():          # mother class

#     @staticmethod
#     def strat():
#         print("bike strat")
    
#     @staticmethod
#     def off():
#         print("bike off")

# class bajaj(bikes):       # child class call the mother class step-1
#     def __init__(self, name):
#         self.name = name

# class palsure(bajaj):       # child class call the mother class step-2
#     def __init__(self, type):
#         self.type = type
        

#     # def info(self):
#         # print(f"bike name is {self.name} {self.off()}")


# bike1 = palsure("p-125cc")
# # bike1.info()
# bike1.name


''' multilavle inhe. example '''

# class A:
#     name1 = "wellcome barun"
# class B:
#     name2 = "wellcome rahim"
# class C:
#     name3 = "wellcome karim"

# class D(A,B,C):
#     name = "all are wellcome"

# D1= D()
# print(D1.name)
# print(D1.name1)
# print(D1.name2)
# print(D1.name3)


'''                           super method   


    we are like to change the parent class attribute into child class. so this time we are use this method.

    '''

# class car:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type

#     @staticmethod
#     def strat():
#         print("bike strat")
    
#     @staticmethod
#     def off():
#         print("bike off")
    
# class barun(car):
#     def __init__(self, name, type, speed):
#         super().__init__(name, type)
#         self.speed = speed
#         super().strat()

#     def info(self):
#         print(f"car name: {self.name} \ntype is: {self.type} \nspeed is: {self.speed}")

# c1 = barun("barun", "bike", 150)
# #print(c1.name)
# c1.info()
    

















"""                                 class method                            """

''' under this method we see 3 type of methods
    1. @staticmethod
    2. @classmethod (cls)
    3. instance (self)'''

'''     A class method is bound to the class & recives the class as an implicit the 1st argument.
        Staticmethod do not change the and modify the main class object'''

    ##      when we need to change the class object or attribuite name this time we need this method

    ##      see some type to change the class attribute



# class perosn():
#     name = "barun"

#     def changename(self, name):
#         self.name = name    # instant change the name but not change the mother class name 

# man = perosn()
# man.changename("kundu")
# print(man.name)
# print(perosn.name)      # this said mother class name is not change 




''' now change the class name using different type'''

# class perosn():
#     name = "barun"

#     def changename(self, name):
#         perosn.name = name    # instant change the name also change the mother class name 

#         # self.__class__.name = name     # also use this logic

# man = perosn()
# man.changename("kundu")
# print(man.name)
# print(perosn.name)      # this said mother class name is change 




''' if we like to change any object into the class using method this time we use @classmethod'''

# class perosn():
#     name = "barun"

#     @classmethod
#     def changename(cls, name):
#         cls.name = name 

# man = perosn()
# man.changename("kundu")
# print(man.name)
# print(perosn.name)      # this said mother class name is change 





"""                                 property decorator                             """

''' when object value are not fixed and we need to change this value any time , this time we are use this
    method. when we use this method then the function autometicaly change that specific subject value and
    give us the result '''

### if a student subject marks is change any time this time we calculate percentage usig this method

''' this is a general method

class student():
    def __init__(self, bang, eng, math):
        self.bangla = bang
        self.eng = eng
        self.math= math
        self.percentage = str((self.math + self.eng + self.bangla)/3 ) + "%"

barun = student(4,4,4)
print(barun.percentage)'''



# class student():
#     def __init__(self, bang, eng, math):
#         self.bangla = bang
#         self.eng = eng
#         self.math= math

#     @property
#     def percentage(self):
#         return str((self.math + self.eng + self.bangla)/3 ) + "%"


# barun = student(4,4,4)
# print(barun.percentage)     # show the pesent value percentage

# barun.bangla = 8
# print(barun.percentage)     # show the change value percentage




    





## some decorators which we are generally ued
''' 1. @classmethod (using object is - cls)
    2. @property
    3. @(property function name).getter and @(property function name).setters
    4. @staticmethod  ((using object is no need)) 
    
    5. instance method (generaly which methods we are use this is called instance method )'''












