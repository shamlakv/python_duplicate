string=input("enter a string with repeated string:")
print("the original string is:",string)
k="$"
res=string[0]+string[1:].replace(string[0],k)
print(res)
