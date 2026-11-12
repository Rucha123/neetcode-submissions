class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj=defaultdict(list)
        t=0

        for u,v,d in times:
            adj[u].append((v,d))

        mh=[(0,k)]
        visit=set()
        while mh:
            d,s=heapq.heappop(mh)
            if s in visit:
                continue
            visit.add(s)
            t=d
            for i,j in adj[s]:
                if i not in visit:
                    heapq.heappush(mh,(t+j,i))

        return t if len(visit)==n else -1
        