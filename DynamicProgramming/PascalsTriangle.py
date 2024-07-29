def generate(numRows):
    l=[]
    for  i in range(numRows):
        r=[1]*(i+1)
        for j in range(1,i):
            r[j]=l[i-1][j]+l[i-1][j-1]
        l.append(r)

    return l
print(generate(int(input())))