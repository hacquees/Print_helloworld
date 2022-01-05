#Write a program to print the Floyd's Triangle
row=int(input("Enter the value of n: "))
c=1
for i in range(row):
	for j in range(i+1):
		print(c,end=" ")
		c+=1
	print()
