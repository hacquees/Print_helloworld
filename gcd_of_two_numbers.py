x=int(input("Please enter an integer: "))
y=int(input("Please enter another integer: "))
m=min(x,y)
gcd=0
if x!=0 and y!=0:
	for i in range(1,abs(m)+1):
		if(x%i==0 and y%i==0):
			gcd=i
		
	
	print("The GCD of",x,"and",y,"is",gcd)
else:
	print("Numbers must be non zero")
