class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)

        p=[]
        
        for i in range(n+1):
            p.append(i)

        print(p)

        def find(n):
            if p[n]!=n:
                p[n]=find(p[n])
            return p[n]


        def union(u,v):
            rootA=find(u)
            rootB=find(v)

            if rootA==rootB:
                return False
            p[rootB]=rootA
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]

        