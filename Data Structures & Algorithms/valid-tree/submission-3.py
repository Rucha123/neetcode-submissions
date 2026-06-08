class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        if len(edges)>n-1:
            return False

        adj=[]


        for i in range(n):
            adj.append([])

        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])

        print(adj)

        q=deque([(0,-1)])
        visit=set()

        visit.add(0)

    

        while q:
            node,p=q.popleft()

            for neigh in adj[node]:

                if neigh == p:
                    continue
                if neigh in visit:
                    return False
                visit.add(neigh)
                q.append([neigh,node])

        print(len(visit))

        return len(visit) == n




        