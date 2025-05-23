class emp:
    name = "barun "

    def __init__(self, name):
        self.name = name

    def __len__(self):
    #     return len(self.name)
        i = 0
        for i in self.name:
            i +=1
        return i

    def __str__(self):
        return (f"your name is {self.name}")
    
    def __repr__(self):
        return (f"name is {self.name}")
    
    """ if we try to call this function in another file
     this time we are use this call function 
    """
    def __call__(self):
        print("i am good")
  