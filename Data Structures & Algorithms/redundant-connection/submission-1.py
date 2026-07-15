class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n=len(edges)

        p=[]

        for i in range(n+1):
            p.append(i)

        def find(n):
            if p[n] != n:
                p[n]=find(p[n])
            return p[n]

        def union(u,v):
            root1=find(u)
            root2=find(v)

            if root1==root2:
                return False
            p[root2]=root1

            return True



        for u,v in edges:
            if not union(u,v):
                return [u,v]
        


        