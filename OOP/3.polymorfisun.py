''' when we use a object or জিনিস in differet way , those object comes in the catagory of that topic.Oparator
    overloading is a example of this topics.

যদি একটা জিনিসকে বিভিন্ন ভাবে ব্যাবহার করা যায় তখন তা এই টপিকের ক্যাটাগরিতে পরে। '''

##      when the same oparator is allowed to have different meaning accoding to the context. 
''' ধরি আমাদের কাছে একটা অপারেটর আছে (+)। এটা আমরা কখন এবং কোথায় ব্যবহার করছি তার ওপর এটির মানে পরিবর্তন হয়ে যাবে। '''

# ## example 
# print(1+2)

# print("barun" + "kndu")

# print([1,2,3] + [4,5,6])


'''             now we see addition of two complex number using dunder function                   '''




class complex:
    def __init__(self, real, img):
        self.real = real
        self.img =img
    
    def result(self):
        print(self.real,"i +", self.img, "j")


    # def add(self, complex2):
    def __add__(self, complex2):
        nwereal= self.real + complex2.real
        newimg = self.img + complex2.img
        return complex(nwereal, newimg) 


complex1 = complex(1,3)
complex1.result()

complex2= complex(4 ,5 )
complex2.result()
        

# complex3 = complex1.add(complex2)     # this is general process 
# complex3.result()

complex3 = complex1 + complex2
complex3.result()

