#Program to print value of pi 1 to n decimals
import math
pi = math.pi
n=int(input("Please enter the no. of decimal places: "))
for i in range(1,n+1):
	print("{:.{}f}".format(pi,i))
