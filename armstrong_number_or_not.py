
n=int(input("Enter a number: "))
c=str(n)
b=n
s=0
while n>0:
	s=s+(n%10)**len(c)
	n//=10
print("The sum of the powers of the digits =",s)
if s==b:
	print("The given number",b,"is an armstrong number")
else:
	print("The given number",b,"is not an armstrong number")
