string = input("enter the string:")
if (string[-3:]=="ing"):
   string=string[:-3]+"ly"
else:
    string=string[:]+"ing"
print(string)
