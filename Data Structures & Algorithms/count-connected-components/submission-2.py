class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p=[]
        s=[1]*n
        for i in range(n):
            p.append(i)

        def find(u):
            if p[u]!=u:
                p[u]=find(p[u])
            return p[u]

        def union(u,v):
            r1=find(u)
            r2=find(v)
            if r1==r2:
                return False
            if s[r1]<s[r2]:
                r1,r2=r2,r1
            p[r2]=r1
            return True
        
        c=n
        for u,v in edges:
            if union(u,v):
                c-=1
        return c




        