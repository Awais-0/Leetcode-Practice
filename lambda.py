class BasicMath:
    def __init__(self,a,b):
        self.square = lambda:a**b
        self.sum_ = lambda :a+b
        self.diff = lambda :a-b
        self.product = lambda :a*b
        self.divide = lambda :a/b

my_obj = BasicMath(2,3)
print(my_obj.square())