n=int(input("enter the limit:"))
lst=[]
for i in range(34,n):
      lst.append(i*i)
print("list of 4 digit perfect square upto",n,":\n",lst,"\n")
for i in lst:
      if(i%2!=0):
          lst.remove(i)
print("list after removing odd numbers:\n",lst)
