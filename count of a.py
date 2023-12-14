list=["shamla","shahala"]
count=0
print(list)
text=input("enter the letter:")
for i in list:
    for n in i:
        if n==text: 
            count=count+1
print("number is:",count)
