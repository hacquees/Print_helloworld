from collections import deque
def bfs(graph,start):
    q=deque([start])
    visted=set()
    visted.add(start)
    while q:
        front=q.popleft()
        print(front,end=" ")
        for i in graph[front]:      #i==Neighbours of Vertex 
            if i not in visted:
                visted.add(i)
                q.append(i)
                
graph={"A":["B","C"],"B":["A","D","E"],"C":["A","F"],"D":["B"],"E":["B","F"],"F":["C","E"]}
bfs(graph,"A")
    