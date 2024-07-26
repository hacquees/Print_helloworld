# Using Memoization Method
def fib(n):
    if n in d:
        return d[n]
    
    if n==0 or n==1:
        return n
    else:
        d[n]=fib(n-1)+fib(n-2)
        return d[n]
d={}
print(fib(int(input())))

# Using Tabulation Method
def fibo(n):
    d=[0]*(n+1)            #Can use Dictionary
    d[1]=1 
    for i in range(2,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]
        
n=int(input())    
print(fibo(n))