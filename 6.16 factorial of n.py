N=(input("N = "))

if(N.isdigit()):
    fact=1
    for i in range(1,int(N)+1):
        fact=fact*i
    print("%d Factorial = %d"%(int(N),fact))
else:
    print("Enter the Number.....")
