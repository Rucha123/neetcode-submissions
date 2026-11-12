class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj=defaultdict(list)
        d = [float('inf')] * (n+1)
        d[k] = 0

        for i,j,l in times:
            if i not in adj:
                adj[i]=[]
            adj[i].append([j,l])

        print(adj)
        mh=[(0,k)]
        while mh:
            c,node=heapq.heappop(mh)

            for neigh,wt in adj[node]:
                nd=wt+c

                if nd<d[neigh]:
                    d[neigh]=nd
                    heapq.heappush(mh,(nd,neigh))

        ans=max(d[1:])
        return ans if ans != float("inf") else -1


        
        
        