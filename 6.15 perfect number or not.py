n=int(input("Given Number: "))
num=n
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==n):
    print("Its a Perfect Number")
else:
    print("Not a perfect Number")

