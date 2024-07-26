# Using Memoization Method
def fact(n):
    if n in d:
        return d[n]
    if n==0:
        return 1
    else:
        d[n]=n*fact(n-1)
    return d[n]
d={}
print(fact(int(input())))

#Using Tabulation Method
def factorial(n):
    d={0:1}
    for i in range(1,n+1):
        d[i]=d[i-1]*i
    return d[n]    
print(factorial(int(input())))
    