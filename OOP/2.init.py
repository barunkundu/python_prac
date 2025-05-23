""" __init__ this is a constractor.   
    when we use class to make object this cons. autometicaly called. 
    this all time take a parameter called "self"
"""
# class person: # class

#     # defult constractor
#     def __init__(self): # if we don't write this,  python autometically call this 
#         pass

#     # parameterized constractor
#     # in our purpose we don't make defult cons.

#     def __init__(self, name, age): # constractor 
#         self.name = name # 1st name is variable, 2nd name is parameter 
#         self.age =age
#         # how many data we are stored in constractor this is called attribute (data/ variables)
#         # like (name, age, marks, etc)
#         print("name is: ")

# p1 = person('barun', 97) # this is object 
# print("worker name is", p1.name," and age is", p1.age)

# p2 = person("kundu", 8)
# print("worker name is", p2.name," and age is", p2.age)


class student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    def avg(self):
        self.avg_marks = ((self.sub1 + self.sub2 + self.sub3)/3)
        print("avg mark is: ",self.avg_marks)

s1 = student("rahim", 33,33,33)
print(s1.name)
s1.avg()

#another process
# using loop and list 

class student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(f"{self.name} your avg marks is:", sum/len(self.marks))

s1 = student("rahim", [22,22,22])
s1.avg()