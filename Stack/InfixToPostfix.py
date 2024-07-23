def precedence(i):
    if i=="+" or i== "-":
        return 1
    elif i=="/" or i=="*":
        return 2
    elif i=="^":
        return 3
    else:
        return 0
    
def postfix(exp):
    ans=""
    l=[]
    for i in exp:
        if i.isalnum():
            ans+=i
        elif i=="(":
            l.append(i)
        elif i==")":
            while len(l)!=0 and  l[-1]!="(":
                ans+=l.pop()
            l.pop()
        
        else:
            while len(l)!=0 and  precedence(l[-1])>=precedence(i):
                ans+=l.pop()
            l.append(i)
    while len(l) != 0:
        ans+=l.pop()
    return ans

exp=input()
print(postfix(exp))


# Using Dictionary

# def postfix(exp):
#     ans=""
#     d={"(":-1,"+":0, "-":0, "*":1, "/":1, "^":2}
#     l=[]
#     for i in exp:
#         if i.isalnum():
#             ans+=i
#         elif i=="(":
#             l.append(i)
#         elif i==")":
#             while len(l)!=0 and  l[-1]!="(":
#                 ans+=l.pop()
#             l.pop()
        
#         else:
#             while len(l)!=0 and  d[l[-1]]>=d[i]:
#                 ans+=l.pop()
#             l.append(i)
#     while len(l) != 0:
#         ans+=l.pop()
#     return ans

# exp=input()
# print(postfix(exp))
