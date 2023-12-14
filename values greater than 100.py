a=int(input("enter the limit of list:"))
i=0
list=[]
while i<a:
    z=int(input("enter number:"))
    if z>100:
        list.append("over listed")
    else:
         list.append(z)
    i=i+1
    print(list)
