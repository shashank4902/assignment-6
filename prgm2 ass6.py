#N number of fibonacci numbers
n =int(input("enter the nth value:"))
a=0
b=1
sum=0
print("fibonacci series:",end=" ")
while(sum<=n):
	    print(sum,end=" ")
	    a=b
	    b=sum
	    sum=a+b
	    