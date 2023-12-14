
class car:
    def __init__(self,name,year):
     self.name=name
     self.year=year
    def show(self):
        print("Name:",self.name,"year:",self.year)



class person:
    def __init__(self,name,age):
     self.name=name
     self.age=age
     person1=person("alice",30)
     person2=person("minu",20)
     print(person1.name)
     print(person1.age)
     print(person2.name)
     print(person1.age)
     


class student:
    school_name='ABC School'
    def __init__(self,name,age):
     self.name=name
     self.age=age
s1=student("harry",20)
print('student:',s1.name,s1.age)
print('schoolname:',student.school_name)
s1.name='jessa'
s1.age=19
print('studentnmae:',s1.name,s1.age)
student.school_name='XYZ School'
print('school name:',student.school_name)
