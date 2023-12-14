n1=int(input("enter the current year:"))
n2=int(input("enter the final year:"))
for i in range(n1,n2):
    if(i%400==0) or (i%4==0 and i%100!=0):
        print(i)
