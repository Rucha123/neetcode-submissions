class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        pr=[float("inf")]*n
        pr[src]=0

        for i in range(k+1):
            tp=pr.copy()

            for s,d,p in flights:
                if pr[s]==float("inf"):
                    continue
                if pr[s]+p < tp[d]:
                    tp[d]=pr[s]+p
                
            pr=tp

        return -1 if pr[dst]==float("inf") else pr[dst]

        