''' constractor-- its help to the object initialization'''
''' use it we pass the object's as a argument. 
    use __init__(self) keyword to write a constractor
    self is a autometica argument, when we define a.person this time it pass in the 
    function, it need not to call when we write code to see the result  
    
    which method are strat with "__" this mothod is called donder '''

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"my name is {self.name}. my age is {self.age}")

x = person("barun", 29)  # here we input only name and age argument
''' user input
    x = person(input("youe name & age: "), input("age: ")) '''
x.info()
y = person("rahim", 66)  # when we define x as a variable this time self argument is autometically pass
y.info()