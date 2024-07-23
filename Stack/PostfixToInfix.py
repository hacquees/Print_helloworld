def Infix(exp):
    l=[]
    for i in exp:
        if i.isalnum():
            l.append(i)
        else: 
            a=l.pop()
            b=l.pop()
            l.append("("+b+i+a+")")
    return l[-1]
   
exp=input()
print(Infix(exp))