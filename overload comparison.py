class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if(self.a>other.a):
           return True
        else:
            return False
obj1=A(4)
obj2=A(3)
if(obj1>obj2):
    print("object1 is greater then object2")
else:
    print("object2 is greater than object1")
