#change item value in list

thislist=["apple","banana","cherry"]
thislist[1]="orange"
print(thislist)
thislist[1:3]=["dates","grapes"]
print(thislist[-1])


#adding elements in list
list1=[]
list1.append(1)
list1.append(2)
list1.append(4)
print(list1)


thislist=["apple","banana","cherry"]
thislist.insert(2,"grapes")
print(thislist)



thislist=["apple","banana","cherry"]
thislist2=["kiwi","orange"]
thislist.extend(thislist2)


thislist=["apple","banana","cherry"]
thislist.remove("banana")
thislist.pop(1)
thislist.pop()
