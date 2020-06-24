#greatest common diviser
def gcd(a,b):
	if(b==0):
		return a
	return gcd(b,a%b)
a=98
b=56
if(gcd(a,b)):
	print('GCD of',a,'and',b,'is',gcd(a,b))
else:
	print('not found')