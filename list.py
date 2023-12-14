
n1=int(input("enter the number of integers in list_1:"))
list_1=[]
print("enter the element:")
for i in range(n1):
     list_1.append(int(input()))
print("elements in list_1:",list_1)
n2=int(input("enter the number of integers in list_2:"))
list_2=[]
print("enter the element:")
for i in range(n2):
     list_2.append(int(input()))
print("elements in list_2:",list_2)
if len(list_1)==len(list_2):
    print("list have same length")
else:
    print("list have different length")
if sum(list_1)==sum(list_2):
    print("the sum of the valuesbin two listare same")
else:
    print("sum are different ")
count=0
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_1[i]==list_2[j]:
            print("values present in both:", list_1[i])
            count=1
if count==0:
        print("there is no similarbvalues in both")

