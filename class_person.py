class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Display(self):
        print("name:",self.name)
        print("age:",self.age)
class employee(person):
    def __init__(self,name,age,empno,address):
        super().__init__(name,age)
        self.empno=empno
        self.address=address
    def Display(self):
        super().Display()
        print("empno:",self.empno)
        print("address:",self.address)
el=employee("shamla",10,111,"pavittapuram")
el.Display()
