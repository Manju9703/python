a=int(input('enter thr no,of fresh loaves'))
e=int(input('enter the no.of old loaves'))
b=a*185
c=e*0.6
d=b-c
print("Regular price",185)
print("amoubt of new loaves",b)
print("amount of day old loaves",c)
print("total amount ",d)
if(a<=0):
    print("fresh no,of loaves must be in positive")
else:
   print("")
