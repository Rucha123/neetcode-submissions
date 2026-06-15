import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mh=[]
        for i in stones:
            heapq.heappush(mh,-i)

        while len(mh)>1:
            a=heapq.heappop(mh)
            b=heapq.heappop(mh)

            if a!=b:
                heapq.heappush(mh,a-b)

        return -mh[0] if mh else 0

        