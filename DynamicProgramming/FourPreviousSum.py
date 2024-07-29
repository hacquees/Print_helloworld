def fib(n):
    if n in d:
        return d[n]
    
    if n==1 or n==2 or n==3 or n==4:
        return n
    else:
        d[n]=fib(n-1)+fib(n-2)+fib(n-3)+fib(n-4)
        return d[n]
d={}
print(fib(int(input())))