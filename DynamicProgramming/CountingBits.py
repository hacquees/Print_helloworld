# This is O(n^2)
# n=int(input())
# l=[]
# for i in range(n+1):
#     c=0
#     while i:
#         if i&1:
#             c+=1
#         i=i>>1
#     l.append(c)
    
# print(l)
    
n=int(input())
l=[0]
for i in range(1,n+1):
    c=l[i>>1]+(i&1)
    l.append(c)
print(l)

# For i the no. of 1 will be same as in i//2 + check last digit
#   - if 1 then add 1 else 0  
# 6=110    12=1100       