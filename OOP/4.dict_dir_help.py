# x= [3,4,5,7,6,5,2]
# print(dir(x))
# print(x.__add__)



class li:
    name = "barun"
    cla = "d"
    # now write a function about len
    def __len__(self):
    #     return len(self.name)
        i = 0
        for i in self.name:
            i +=1
        return i

b = li()
print(b.name)
# print(b.__len__())
print(len(b.name))



