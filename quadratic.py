
import math
def equationroots( a, b, c):

	
	dis = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis))
	
	
	if dis > 0:
		print(" real and different roots ")
		print((-b + sqrt_val)/(2 * a))
		print((-b - sqrt_val)/(2 * a))
	elif dis == 0:
		print(" real and same roots")
		print(-b / (2 * a))
	else:
		print("Complex Roots")
		print(- b / (2 * a), " + i", sqrt_val)
		print(- b / (2 * a), " - i", sqrt_val)
		
a =float(input('enter the co-efficient of x^2'))
b =float(input('enter the co-efficient of x'))
c =float(input('enter the co-efficient of constant'))

if a == 0:
    print("Input correct quadratic equation")

else:
    equationroots(a, b, c)
