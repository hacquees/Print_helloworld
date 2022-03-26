a=list(map(int,input().split()))
b=a[0]//2
for i in range(b,0,-1):
    for j in range(3*i):
        print("-",end="")
    for k in range((b-i)*2+1):
        print(".|.",end="")
    for j in range(3*i):
        print("-",end="")
    print()
print("WELCOME".center(a[1],"-")) 
for i in range(1,b+1):
    for j in range(3*i):
        print("-",end="")
    for k in range((b-i)*2+1):
        print(".|.",end="")
    for j in range(3*i):
        print("-",end="")
    print()   

