#No of Ways to reach N stair provided we can take either 1 or 2 steps
def StairCase(n):
    if n in d:
        return d[n]
    if n ==0 or n==1:
        return 1
    else:
        d[n]=StairCase(n-1)+StairCase(n-2)
    return d[n]
 
d={}
print(StairCase(int(input())))
        