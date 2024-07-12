# OOP means --> object orianted program
# it makes the program esier to understand & reduce time
''' that means , we create a from  (blueprint) . 
    and now user are fill up theri form (object [entity])
    
    shop form (blueprint)

    & who fillup this form
    barun --> er shop information related form (object [entity])
    rahim --> er shop information related form (object [entity])
    niten --> er shop information related form (object [entity])
    '''

# class person:   # this is a blueprint
#     name= "barun"
#     age= 26 
#     house= "kurigram"

# x= person()

# x.name= "niten" # change the blueprint name and age
# x.age= 25

''' now useing function and make it esaier'''
# class person:  # parent object
#     name= "barun"
#     age= 26 
#     house= "kurigram"
#     def info(self): # this is a donder method
#         print(f"name {self.name} & age{self.age} & house {self.house}")

# ## "self" argument must be used in any method when we define the method into the class


# x= person()
# y= person()
# z= person()

# x.name= "nitien" # this is instance attribute
# x.age= 25
# x.house= "ki jani"
# # print(x.info())

''' make many people which is call child object
    instance attribute which is properti of the particular object
    x,y,z is the particular object'''
# y.name= "mukes"
# y.age= 28
# y.house= "ki "

# z.name= "nin"
# z.age= 20
# z.house= "jani"

# x.info()
# y.info()
# z.info()




class person:  # parent object
    name= "barun"
    age= 26 
    house= "kurigram"
    def info(self): # this is method
        print(f"name {self.name} & age{self.age} & house {self.house}")

    @staticmethod
    # when a function we not need to any object property this time we use this 
    # decorator
    def sokal():
        print("good morning")

barun = person()
barun.info()

# working procedure in info(self)
# create person.info(barun)