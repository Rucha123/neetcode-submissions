class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj=[]

        for i in range(n):
            adj.append([])

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        print(adj)

        q=deque([(0,-1)])

        visit=set()
        visit.add(0)

        while q:
            cur,p=q.popleft()

            for nei in adj[cur]:
                if nei == p:
                    continue
                if nei in visit:
                    return False
                q.append([nei,cur])
                visit.add(nei)

        return len(visit) == n