#Calculate Fibonacci numbers less than a given number and calculates the sum of all alternate numbers (even numbered) in the generated list
a=int(input("Please enter a number: "))
l=[]
b,c=0,1
l.extend([b,c])
print(b)
print(c)
for i in range(1,a-2):
	pre=b
	s=b+c
	if s>a:
		break
	l.append(s)
	print(s)
	b=c
	c=s
print("Sum =",sum(l[::2]))
