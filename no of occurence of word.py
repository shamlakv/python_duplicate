text=str(input("enter the text:"))
word=str(input("enter the word:"))
list=text.split()
count=0
for i in list:
    if i==word:
        count=count+1
print("number is",word,"is",count)
