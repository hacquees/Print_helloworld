#Calculate Fibonacci numbers less than a given number and calculates the sum of all alternate numbers (even numbered) in the generated list
a=int(input("Please enter a number: "))
l=[]
b=-1
c=1
while True:
	s=b+c
	if s>=a:
		break
	l.append(s)
	print(s)
	b=c
	c=s
print("Sum =",sum(l[::2]))
