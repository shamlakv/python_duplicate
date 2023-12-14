class car:
    def __init__(self,color,price,km):
        self.color=color
        self.price=price
        self.km=km
    def __gt__(self,other):
        if(self.price>other.price):
            return True
        else:
            return False
    def __add__(self,other):
         return self.km+other.km
car1=car("black",678000,350)
car2=car("blue",68000,500)
sum=car1.km+car2.km
print(sum)
if(car1.price>car2.price):
    print("car1 is more price than car2")
else:
    print("car2 is more price than car1")
