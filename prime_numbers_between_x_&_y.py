x=int(input("Enter lower limit: "))
y=int(input("Enter upper limit: "))
print("Prime numbers between {} and {} are:".format(x,y))
for i in range(x,y):
	for j in range(2,i):
		if i%j==0:
			break

	else:
		print(i)
