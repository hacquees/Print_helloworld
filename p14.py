#decimal to binary
n=int(input("Enter number:"))
i=0
s=0
p=0
while n>0:
    p=10**i
    i+=1
    s=s+(n%2)*p
    n//=2
print(s)



