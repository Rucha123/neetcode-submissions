class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        p=[]
        for i in range(len(edges)+1):
            p.append(i)
        print(p)

        def find(u):
            if p[u]!=u:
                p[u]=find(p[u])
            return p[u]

        def union(u,v):
            r1=find(u)
            r2=find(v)
            if r1==r2:
                return False
            p[r2]=r1
            return True


        for u,v in edges:
            if not union(u,v):
                return [u,v]
           



        