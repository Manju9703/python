print("Enter -7 to exit... ")
a=[]
b=[]
while True:
    n=int(input("Enter the number "))
    if(n==-7):
        break
    if(n>0):
        a.append(n)
    else:
        b.append(n)

x=(sum(a)/len(a))
y=(sum(b)/len(b))
print("The average of negative number is: ",x)
print("The average of positive number is: ",y)
