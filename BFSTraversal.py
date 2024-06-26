#User function Template for python3
#https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
from typing import List
from collections import deque 
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        
        visited=[False]*V
        q=deque([0])
        visited[0]=True
        bfs=[]
        
        while q:
            u=q.popleft()
            bfs.append(u)
            for i in adj[u]:
                if not visited[i]:
                    q.append(i)
                    visited[i]=True
                    
                    
        return bfs
        
