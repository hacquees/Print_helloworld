""" Find Sum of pairs between L and R 
    List = [1,2,3,4,5,6,7,8,9]
    Pair = [0,1 5,4,5]
    Example:
    (0,1) = 3
    (1,5) = 20                  
    (4,5) = 11                  Take Min as L and Max ad R 
    (4,5) = 11
    =============
            45 
"""

l=list(map(int,input().split()))
b=list(map(int,input().split()))
ps=[]
c=0
for i in l:
    c+=i
    ps.append(c)
sum=0
for j in range(len(b)-1):
    a=min(b[j],b[j+1])
    d=max(b[j],b[j+1])
    if a:
        sum+=ps[d]-ps[a-1]
    else:
        sum+=ps[d]
print(sum)
    