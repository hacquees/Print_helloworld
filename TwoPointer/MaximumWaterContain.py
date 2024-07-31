def maxArea(height):
    i=0
    j=len(height)-1
    c=-float('inf')
    while i<j:
        if height[i]<=height[j]:
            c=max(height[i]*(j-i),c)
            i+=1
        
        else:
            c=max(height[j]*(j-i),c)
            j-=1

    return c

print(maxArea(list(map(int,input().split()))))



