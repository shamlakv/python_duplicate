text=input("enter the list of words:")
longest=0
for word in text.split():
     if len(word)>longest:
         longest=len(word)
print("The longest word is with length",longest) 
