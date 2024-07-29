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
