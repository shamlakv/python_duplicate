list1=[14,30,44,65,37]
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print("new list is:",list1)
