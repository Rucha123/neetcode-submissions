class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        p=[]
        for i in range(n):
            p.append(i)

        def find(u):
            if p[u]!=u:
                p[u]=find(p[u])
            return p[u]

        def union(u,v):
            p1=find(u)
            p2=find(v)
            if p1==p2:
                return False
            p[p2]=p1
            return True
  
        for u,v in edges:
            if not union(u,v):
                return False

        return True
        