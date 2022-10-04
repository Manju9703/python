print("Enter * to exit... ")
string=[]
while True:
    ch=input("Enter any character: ")
    if(ch=='*'):
        break
    string.append(ch)
lower=upper=schar=digit=0
for i in string:
    if(i.islower()):
        lower=lower+1
    elif(i.isupper()):
        upper=upper+1
    elif(i.isdigit()):
        digit=digit+1
    else:
        schar=schar+1
print("Lower case= ",lower)
print("Upper case= ",upper)
print("Digit = ",digit)
print("Special Character= ",schar)
