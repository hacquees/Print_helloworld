def canCompleteCircuit(gas,cost):
    if sum(gas)<sum(cost):
        return -1
    t=0
    s=0
    for i in range(len(gas)):
        t=t+gas[i]-cost[i]
        if t<0:
            s=i+1
            t=0
    return s

g=list(map(int,input().split()))
c=list(map(int,input().split()))
print(canCompleteCircuit(g,c))

