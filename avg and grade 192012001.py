english=float(input('enter the marks'))
maths=float(input('enter the marks'))
physics=float(input('enter the marks'))
chemistry=float(input('enter the marks'))

total=english+maths+physics+chemistry

average=total/4
print('Average',average)

if average>=91 and average<=100:
    print("Your Grade is A1")
elif average>=81 and average<91:
    print("Your Grade is A2")
elif average>=71 and average<81:
    print("Your Grade is B1")
elif average>=61 and average<71:
    print("Your Grade is B2")
elif average>=51 and average<61:
    print("Your Grade is C1")
elif average>=41 and average<51:
    print("Your Grade is C2")
elif average>=33 and average<41:
    print("Your Grade is D")
elif average>=21 and average<33:
    print("Your Grade is E1")
elif average>=0 and average<21:
    print("Your Grade is E2")
