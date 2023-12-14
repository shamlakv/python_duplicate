string=input("enter a string:")
lst=[]
for i in range(len(string)):
    unicode=ord(string[i])
    lst.append(unicode)
print(lst)
