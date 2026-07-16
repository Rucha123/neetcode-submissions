class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        q=deque()
        c=0

        adj=[]
        visit=set()

        for i in range(n):
            adj.append([])

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def bfs(node):
      
            q.append(node)
            visit.add(node)

            while q:
                cur=q.popleft()
                for nei in adj[cur]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)

        for i in range(n):
            if i not in visit:
                bfs(i)
                c+=1

        return c
        