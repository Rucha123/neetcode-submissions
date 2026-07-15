class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False


        p=[]

        for i in range(n):
            p.append(i)

        print(p)

        def find(n):
            if p[n] != n:
                p[n]=find(p[n])
            return p[n]


        def union(u,v):
            r1=find(u)
            r2=find(v)

            if r1==r2:
                return False
            p[r2]=r1
            return True

        for u,v in edges:
            if not union(u,v):
                return False

        return True




        