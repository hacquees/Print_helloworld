from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    def addEdge(self,v,u):
        self.graph[u].append(v)                     # Directed graph
    def dfsUtil(self,v,visted):
        visted.add(v)
        print(v,end=" ")
        for i in self.graph[v]:
            if i not in visted:
                self.dfsUtil(i,visted)
    def dfs(self,v):
        visted=set()
        self.dfsUtil(v,visted)
        
        
gph=Graph()
gph.addEdge(1,2)
gph.addEdge(2,3)
gph.addEdge(3,4)
gph.addEdge(4,5)
gph.addEdge(5,6)
gph.addEdge(6,1)
gph.addEdge(5,7)
gph.addEdge(2,7)
gph.addEdge(4,7)
gph.dfs(1)



                